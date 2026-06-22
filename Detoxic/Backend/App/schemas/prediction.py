from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PredictionBase(BaseModel):
    toxic: float
    severe_toxic: float
    obscene: float
    threat: float
    insult: float
    identity_hate: float

class PredictionCreate(PredictionBase):
    submission_id: int

class PredictionOut(PredictionBase):
    id: int
    predicted_at: datetime

    class Config:
        orm_mode = True
