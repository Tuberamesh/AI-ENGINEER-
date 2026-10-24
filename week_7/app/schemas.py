from pydantic import BaseModel, Field, field_validator


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=500)
    top_k: int = Field(default=3, ge=1, le=10)

    @field_validator("question", mode="before")
    @classmethod
    def clean_question(cls, value):
        if isinstance(value, str):
            return value.strip()
        return value


class SourceInfo(BaseModel):
    source: str
    page: int | str | None = None
    distance: float


class AskResponse(BaseModel):
    question: str
    answer: str
    top_k: int
    sources: list[SourceInfo]
