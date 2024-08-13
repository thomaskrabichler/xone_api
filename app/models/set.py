from app.db.session import Base
from sqlalchemy import Boolean, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship


class Set(Base):
    __tablename__ = "sets"
    id = Column(Integer, primary_key=True, index=True)
    reps = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    position = Column(Integer, nullable=True)
    is_done = Column(Boolean, nullable=False, default=False)
    is_new = Column(Boolean, nullable=True, default=False)
    set_name = Column(String, nullable=True, default=False)

    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    user_id = Column(String, ForeignKey("users.id"))
    sets_history = relationship("SetHistory", backref="set")
