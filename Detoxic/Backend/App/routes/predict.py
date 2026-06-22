from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict
from ..ml_model import get_model
from ..ml_model.predictor import ModelWrapper

router = APIRouter()

class PredictIn(BaseModel):
    text: str

class PredictOut(BaseModel):
    toxic: float
    severe_toxic: float
    obscene: float
    threat: float
    insult: float
    identity_hate: float

@router.post("/predict", response_model=PredictOut)
async def predict(payload: PredictIn):
    model: ModelWrapper = get_model()
    try:
        cleaned = payload.text
        # Optionally run preprocessor here
        result = model.predict(cleaned)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
