from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, String
from .base import Base
import datetime

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    comment_text = Column(Text, nullable=False)
    submission_date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
