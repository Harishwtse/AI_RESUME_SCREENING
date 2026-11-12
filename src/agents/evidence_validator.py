def validate_analysis(result: dict) -> list[str]:
    errors=[]
    score=result.get("score")
    if not isinstance(score,int) or not 0<=score<=100: errors.append("Score must be integer 0-100")
    if result.get("review_status")!="Human review required": errors.append("Human review flag missing")
    if not isinstance(result.get("evidence"),list): errors.append("Evidence must be a list")
    if len(result.get("summary",""))>1500: errors.append("Summary too long")
    return errors
