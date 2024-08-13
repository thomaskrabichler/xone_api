from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base

class Exercise(Base):
     __tablename__ = "exercises"
     id = Column(Integer, primary_key=True, index=True)
     title = Column(String(64), nullable=False)
     details = Column(String(64), nullable=False)
     workout_id = Column(Integer, ForeignKey("workouts.id"))
     sets = relationship("Set", cascade='all, delete')
     user_id = Column(String, ForeignKey("users.id"))
     sets_history = relationship("SetHistory")
