from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from .base import Base
import datetime

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(Integer, ForeignKey("submissions.id"), nullable=False)
    toxic = Column(Float, default=0.0)
    severe_toxic = Column(Float, default=0.0)
    obscene = Column(Float, default=0.0)
    threat = Column(Float, default=0.0)
    insult = Column(Float, default=0.0)
    identity_hate = Column(Float, default=0.0)
    predicted_at = Column(DateTime, default=datetime.datetime.utcnow)
