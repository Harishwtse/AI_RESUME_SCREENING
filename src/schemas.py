from typing import TypedDict, List
from pydantic import BaseModel, Field
class ResumeAnalysis(BaseModel):
    summary: str = Field(description="Brief professional summary based only on resume evidence")
    strengths: List[str] = Field(description="Relevant skills/experience explicitly supported")
    gaps: List[str] = Field(description="Job requirements missing or not evidenced; do not infer absence")
    evidence: List[str] = Field(description="Short resume snippets supporting matches")
    score: int = Field(ge=0,le=100,description="Job-related match score; not a hiring probability")
    review_status: str = Field(description="Always 'Human review required'")
class ScreeningState(TypedDict, total=False):
    resume_text: str
    job_description: str
    role: str
    analysis: dict
    validation_errors: list
    retry_count: int
