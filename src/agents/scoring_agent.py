def normalize_score(result: dict) -> dict:
    # LLM relevance score is advisory; this function only normalizes/labels it.
    result["score"]=max(0,min(100,int(result.get("score",0))))
    result["review_status"]="Human review required"
    return result
