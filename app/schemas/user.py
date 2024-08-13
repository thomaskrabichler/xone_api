from typing import List, Optional

from app.schemas.workout_plan import WorkoutPlan
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    id: str
    name: str
    weight: str
    height: str
    birth_date: str
    gender: str


class UserUpdate(BaseModel):
    # email: Optional[str] = None
    name: Optional[str] = None
    weight: Optional[str] = None
    height: Optional[str] = None
    birth_date: Optional[str] = None
    gender: Optional[str] = None
    selected_plan: Optional[int] = None

class UserRead(UserBase):
    name:str

class User(UserCreate):
    # id: str
    is_active: bool
    # items: List[Item] = []
    workout_plans: List[WorkoutPlan] = []
    selected_plan: Optional[WorkoutPlan] = None
    class Config:
        orm_mode = True

# TODO: Don't return email and id in response model
