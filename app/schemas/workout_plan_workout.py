from typing import List, Union
from .exercise import Exercise
from pydantic import BaseModel
# from schemas.workout_plan import WorkoutPlan


class WorkoutBase(BaseModel):
    title: str

class WorkoutUpdate(WorkoutBase):
    pass

class WorkoutPlanBase(BaseModel):
    title: str


class Workout(WorkoutBase):
    id: int
    exercises: List[Exercise] = []

    class Config:
        orm_mode = True


class WorkoutPlanCreate(WorkoutPlanBase):
    title: str
    workouts: List[Workout] = []

class WorkoutPlanUpdate(WorkoutPlanBase):
    pass


class WorkoutPlan(WorkoutBase):
    id: int
    # user_id: str #TODO: is user_id needed here?
    workouts: List[Workout] = []

    class Config:
        orm_mode = True


class WorkoutCreate(BaseModel):
    title: str
    workout_plans: List[WorkoutPlan] = []
