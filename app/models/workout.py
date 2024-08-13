from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base

class Workout(Base):
     __tablename__ = "workouts"
     id = Column(Integer, primary_key=True, index=True)
     title = Column(String(64), nullable=False)
     exercises = relationship("Exercise")
     workout_plans = relationship("WorkoutPlan", secondary="workout_plan_workouts", back_populates = "workouts")
     user_id = Column(String, ForeignKey("users.id"))

