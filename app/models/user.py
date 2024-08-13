from enum import unique
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.elements import Null

from app.db.session import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    weight = Column(String, index=True)
    height = Column(String, index=True)
    birth_date = Column(String, index=True)
    gender = Column(String, index=True)
    is_active = Column(Boolean, default=True)

    workout_plans = relationship("WorkoutPlan", cascade="all, delete")
    selected_plan = relationship(
        "WorkoutPlan", uselist=False, cascade="all, delete-orphan")
