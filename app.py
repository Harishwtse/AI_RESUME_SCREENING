import streamlit as st
from src.services.screening_service import screen_resume
from src.ingestion.resume_parser import extract_text

st.set_page_config(page_title="AI Resume Screener", page_icon="HK", layout="wide")
st.title( " AI Resume Screener")
st.caption("Evidence-based candidate matching | Human review required")

with st.sidebar:
    st.header("Job requirements")
    role=st.text_input("Role title", "AI Engineer")
    jd=st.text_area("Job description", height=260, placeholder="Paste the job description...")
    st.info("Use only job-related criteria. Do not rank on protected or sensitive attributes.")

uploads=st.file_uploader("Upload resumes (PDF/DOCX/TXT)", type=["pdf","docx","txt"], accept_multiple_files=True)
if st.button("Screen candidates", type="primary", disabled=not (uploads and jd.strip())):
    results=[]
    bar=st.progress(0)
    for i,f in enumerate(uploads):
        try:
            text=extract_text(f.getvalue(), f.name)
            result=screen_resume(text, jd, role)
            result["filename"]=f.name
            results.append(result)
        except Exception as e:
            st.error(f"{f.name}: {e}")
        bar.progress((i+1)/len(uploads))
    st.session_state["results"]=results

if "results" in st.session_state:
    results=st.session_state["results"]
    st.subheader("Screening results")
    if results:
        st.dataframe([{"Resume":r.get("filename"),"Match score":r.get("score"),"Review":r.get("review_status"),"Strengths":", ".join(r.get("strengths",[]))} for r in results], use_container_width=True)
        for r in results:
            with st.expander(f"{r.get('filename')} — {r.get('score','N/A')}/100"):
                st.write("**Summary:**",r.get("summary",""))
                st.write("**Evidence-based strengths:**",r.get("strengths",[]))
                st.write("**Gaps / unclear evidence:**",r.get("gaps",[]))
                st.write("**Evidence:**",r.get("evidence",[]))
                st.warning("AI output is advisory. A qualified recruiter must review the original resume and verify claims.")
        st.download_button("Download results JSON", __import__("json").dumps(results,indent=2), "screening_results.json")
