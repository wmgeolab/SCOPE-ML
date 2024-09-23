from pydantic import BaseModel


class GEFRagRequest(BaseModel):
    questions: list[str]
    project_id: str


class GEFRagResponse(BaseModel):
    answers: dict[str, str]
