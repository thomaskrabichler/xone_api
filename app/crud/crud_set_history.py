from sqlalchemy.orm import Session
from app.models.set_history import SetHistory


def get_set(db: Session, set_id: int):
    return db.query(SetHistory).filter(SetHistory.id == set_id).first()


def get_archived_sets(db: Session, exercise_id: int):
    return db.query(SetHistory).filter(SetHistory.exercise_id == exercise_id).all()


def delete_archived_set(db: Session, set_id: int):
    return db.query(SetHistory).filter(SetHistory.id == set_id).delete()
