from typing import List, Union
from app.schemas.exercise import Exercise
from pydantic import BaseModel
from app.schemas.workout import Workout

class WorkoutPlanBase(BaseModel):
    title: str
    workouts: List[Workout]

class WorkoutPlanCreate(WorkoutPlanBase):
    title: str


class WorkoutPlan(WorkoutPlanBase):
    id: int
    user_id: str

    class Config:
        orm_mode = True

