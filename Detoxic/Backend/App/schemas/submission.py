from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SubmissionBase(BaseModel):
    comment_text: str

class SubmissionCreate(SubmissionBase):
    user_id: Optional[int] = None

class SubmissionOut(SubmissionBase):
    id: int
    submission_date: datetime
    status: str

    class Config:
        orm_mode = True
