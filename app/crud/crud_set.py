from sqlalchemy.orm import Session

from app.models.set import Set
from app.models.set_history import SetHistory
from app.schemas.set import SetCreate, SetUpdate
from app.crud.crud_exercise import get_exercise
from fastapi import HTTPException


def get_set(db: Session, set_id: int):
    return db.query(Set).filter(Set.id == set_id).first()


def get_sets(db: Session, exercise_id: int):

    db_exercise = get_exercise(db, exercise_id)

    if not db_exercise:
        raise HTTPException(
            status_code=404, detail=f"exercise with id {exercise_id} not found.")

    return db_exercise.sets


def create_set(db: Session, set: SetCreate, exercise_id: int):
    exercise = get_exercise(db, exercise_id)
    if not exercise:
        raise HTTPException(
            status_code=404, detail=f"exercise with id {exercise_id} not found.")

    last_set = db.query(Set).filter(Set.exercise_id ==
                                    exercise_id).order_by(Set.position.desc()).first()

    if last_set:
        position = last_set.position + 1
    else:
        position = 1

    db_set = Set(reps=set.reps, weight=set.weight,
                 exercise_id=exercise_id, is_done=False, position=position)

    db.add(db_set)
    db.commit()
    db.refresh(db_set)

    set_history = SetHistory(
        set_id=db_set.id, exercise_id=exercise_id, reps=set.reps, weight=set.weight, position=position)

    db.add(set_history)
    db.commit()
    db.refresh(set_history)

    return db_set


def update_set(db: Session,  set_id: int, set: SetUpdate):
    set_db = get_set(db, set_id)

    if not set_db:
        raise HTTPException(status_code=404, detail="Set not found.")

    set_data = set.dict(exclude_unset=True)

    for key, value in set_data.items():
        setattr(set_db, key, value)

    db.add(set_db)
    db.commit()
    db.refresh(set_db)

    set_history = SetHistory(
        set_id=set_db.id, exercise_id=set_db.exercise_id, reps=set.reps, weight=set.weight, position=set.position)

    db.add(set_history)
    db.commit()
    db.refresh(set_history)

    return set_db


def delete_set(db: Session, set_id: int):
    set_db = get_set(db, set_id)

    if not set_db:
        raise HTTPException(status_code=404, detail='set not found')

    db.delete(set_db)
    db.commit()
    return set_db
