
from pydantic import BaseModel

from datetime import datetime

class SetHistoryBase(BaseModel):
    reps: int
    weight: float


class SetHistoryCreate(SetHistoryBase):
    pass


class SetHistory(SetHistoryBase):
    id: int
    position: int
    created_at: datetime
    class Config:
        orm_mode = True


class SetHistoryUpdate(SetHistoryBase):
    pass


class SetHistoryDelete(SetHistoryBase):
    pass

