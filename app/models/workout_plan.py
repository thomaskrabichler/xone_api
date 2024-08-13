from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.db.session import Base

workout_plan_workouts = Table("workout_plan_workouts",
                          Base.metadata,
                          Column("workout_plans_id",
                                 ForeignKey("workout_plans.id")),
                          Column("workouts_id", ForeignKey("workouts.id")),
                          )


class WorkoutPlan(Base):
    __tablename__ = "workout_plans"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64), nullable=False)
    user_id = Column(String, ForeignKey("users.id"))
    workouts = relationship("Workout", secondary="workout_plan_workouts", back_populates="workout_plans", cascade="all, delete")
