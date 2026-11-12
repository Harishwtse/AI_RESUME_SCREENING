from src.agents.resume_analyzer import analyze
from src.agents.evidence_validator import validate_analysis
from src.agents.scoring_agent import normalize_score
def analyze_node(state):
    result=analyze(state["resume_text"],state["job_description"],state.get("role",""))
    return {"analysis":result,"validation_errors":validate_analysis(result)}
def score_node(state):
    return {"analysis":normalize_score(state["analysis"])}
def route_validation(state):
    return "retry" if state.get("validation_errors") and state.get("retry_count",0)<1 else "score"
def retry_node(state):
    return {"retry_count":state.get("retry_count",0)+1}
