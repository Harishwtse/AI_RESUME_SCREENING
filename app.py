
import os
import json
import streamlit as st
from dotenv import load_dotenv

# Streamlit configuration
st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="HK",
    layout="wide"
)

# Load local .env file
load_dotenv()

# Load Groq API key from Streamlit Cloud Secrets
try:
    cloud_key = st.secrets["GROQ_API_KEY"]
    if cloud_key:
        os.environ["GROQ_API_KEY"] = str(cloud_key).strip()
except Exception:
    pass

# Check API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Import services only after loading the API key
from src.services.screening_service import screen_resume
from src.ingestion.resume_parser import extract_text


# Application UI
st.title("AI Resume Screener")
st.caption("Evidence-based candidate matching | Human review required")

if not GROQ_API_KEY:
    st.warning(
        "Groq API key is missing. Configure GROQ_API_KEY "
        "in your local .env file or Streamlit Cloud Secrets."
    )

with st.sidebar:
    st.header("Job requirements")

    role = st.text_input("Role title", "AI Engineer")

    jd = st.text_area(
        "Job description",
        height=260,
        placeholder="Paste the job description..."
    )

    st.info(
        "Use only job-related criteria. "
        "Do not rank on protected or sensitive attributes."
    )


uploads = st.file_uploader(
    "Upload resumes (PDF/DOCX/TXT)",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)


if st.button(
    "Screen candidates",
    type="primary",
    disabled=not (uploads and jd.strip())
):

    if not GROQ_API_KEY:
        st.error("Please configure GROQ_API_KEY before screening.")
        st.stop()

    results = []

    bar = st.progress(0)

    for i, f in enumerate(uploads):

        try:
            # Extract resume text
            text = extract_text(f.getvalue(), f.name)

            # AI resume screening
            result = screen_resume(text, jd, role)

            result["filename"] = f.name

            results.append(result)

        except Exception as e:
            st.error(f"{f.name}: {e}")

        bar.progress((i + 1) / len(uploads))

    st.session_state["results"] = results


# Display screening results
if "results" in st.session_state:

    results = st.session_state["results"]

    st.subheader("Screening results")

    if results:

        st.dataframe(
            [
                {
                    "Resume": r.get("filename"),
                    "Match score": r.get("score"),
                    "Review": r.get("review_status"),
                    "Strengths": ", ".join(r.get("strengths", []))
                }
                for r in results
            ],
            use_container_width=True
        )

        for r in results:

            with st.expander(
                f"{r.get('filename')} — {r.get('score', 'N/A')}/100"
            ):

                st.write("**Summary:**", r.get("summary", ""))

                st.write(
                    "**Evidence-based strengths:**",
                    r.get("strengths", [])
                )

                st.write(
                    "**Gaps / unclear evidence:**",
                    r.get("gaps", [])
                )

                st.write(
                    "**Evidence:**",
                    r.get("evidence", [])
                )

                st.warning(
                    "AI output is advisory. A qualified recruiter "
                    "must review the original resume and verify claims."
                )

        st.download_button(
            "Download results JSON",
            json.dumps(results, indent=2),
            "screening_results.json",
            mime="application/json"
        )

    else:
        st.info("No successful screening results. Check the errors above.")
