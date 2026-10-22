from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=500)
    top_k: int = Field(default=3, ge=1, le=10)


class AskResponse(BaseModel):
    question: str
    answer: str
    top_k: int