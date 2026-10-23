
from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=500)
    top_k: int = Field(default=3, ge=1, le=10)


class SourceInfo(BaseModel):
    source: str
    page: int | str | None = None
    distance: float


class AskResponse(BaseModel):
    question: str
    answer: str
    top_k: int
    sources: list[SourceInfo]
