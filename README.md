# AI Resume Screener | FDE Portfolio Project

A recruiter-assist prototype for resume parsing, evidence-based job matching, structured AI analysis, workflow validation, and human review.

## Stack
Python, Streamlit, LangChain, LangGraph, GroqCloud (`openai/gpt-oss-20b`), Hugging Face Sentence Transformers, FAISS.

## Quick start
1. Python 3.11+
2. `python -m venv .venv`
3. Activate the environment
4. `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and add your Groq API key
6. `streamlit run app.py`

## Docker
`docker compose up --build`

## Workflow
Upload → parse PDF/DOCX/TXT → LangGraph analysis node → structured output validation → retry once if invalid → score normalization → recruiter review.

## FDE extensions (recommended)
- Add PostgreSQL candidate/job tables, audit trail, tenant isolation, authentication/RBAC.
- Add resume redaction and secure deletion/retention controls.
- Add LangSmith tracing, latency/token/cost dashboards, prompt/version tracking.
- Create a labeled golden dataset and evaluate extraction accuracy, evidence precision, score calibration, fairness, and reviewer agreement.
- Add human approval/edit/reject state and recruiter feedback loop.
- Deploy behind authentication; use object storage with encryption and signed URLs.
- Add API endpoints and ATS integration (Greenhouse/Lever) using sandbox credentials.
- Add tests, CI, observability, alerting, rate limits, and load tests.

## Responsible use
This tool is decision support only. Do not auto-reject or auto-hire. Scores are not probabilities.
Exclude protected/sensitive attributes and proxies. Provide explanations, human review, accessibility,
candidate notice/consent, data minimization, retention/deletion, and bias monitoring.
Never upload real candidate data to a demo without authorization and appropriate safeguards.
