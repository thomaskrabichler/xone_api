from app.db.session import Base
from sqlalchemy import Boolean, DateTime, Column, Integer, Float, ForeignKey
from datetime import datetime

class SetHistory(Base):
    __tablename__ = "set_histories"
    id = Column(Integer, primary_key=True, index=True)
    set_id = Column(Integer, ForeignKey("sets.id"))
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    position = Column(Integer, nullable=True)
    reps = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
