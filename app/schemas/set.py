from pydantic import BaseModel


class SetBase(BaseModel):
    reps: int
    weight: float


class SetCreate(SetBase):
    pass


class Set(SetBase):
    id: int
    is_done: bool
    position: int
    class Config:
        orm_mode = True


class SetUpdate(SetBase):
    position:int
    pass


class SetDelete(SetBase):
    pass

