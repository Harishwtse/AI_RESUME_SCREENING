from src.graph.workflow import build_graph
def screen_resume(resume_text: str, job_description: str, role: str):
    graph=build_graph()
    out=graph.invoke({"resume_text":resume_text,"job_description":job_description,"role":role,"retry_count":0})
    return out["analysis"]
