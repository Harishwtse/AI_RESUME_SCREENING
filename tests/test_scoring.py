from src.agents.scoring_agent import normalize_score
def test_score_clamped_and_review_flag():
    x=normalize_score({"score":120})
    assert x["score"]==100
    assert x["review_status"]=="Human review required"
