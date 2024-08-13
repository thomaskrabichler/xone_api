from typing import List
from pydantic import BaseModel

from app.schemas.set import Set
from app.schemas.set_history import SetHistory

class ExerciseBase(BaseModel):
    title: str
    details: str


class ExerciseCreate(ExerciseBase):
    pass


class Exercise(ExerciseBase):
    id: int
    sets: List[Set] = []
    archived_sets: List[SetHistory] = []

    class Config:
        orm_mode = True

class ExerciseUpdate(ExerciseBase):
    pass
