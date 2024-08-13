from typing import List, Union
from .exercise import Exercise
from pydantic import BaseModel
# from schemas.workout_plan import WorkoutPlan

class WorkoutBase(BaseModel):
    title: str

class WorkoutCreate(BaseModel):
    title: str
    

class Workout(WorkoutBase):
    id: int
    exercises: List[Exercise] = []

    class Config:
        orm_mode = True

class WorkoutUpdate(WorkoutBase):
    pass