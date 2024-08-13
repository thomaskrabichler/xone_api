from sqlalchemy.orm import Session
from app.models.exercise import Exercise
from fastapi import HTTPException
from app.schemas.exercise import ExerciseCreate, ExerciseUpdate
from app.crud.crud_workout import get_workout


def get_exercise(db: Session, exercise_id: int):
    return db.query(Exercise).filter(Exercise.id == exercise_id).first()


def get_exercises(db: Session, workout_id: int):
    return db.query(Exercise).filter(Exercise.workout_id == workout_id).all()


def get_sets(db: Session, exercise_id: int):

    db_exercise = get_exercise(db, exercise_id)

    if not db_exercise:
        raise HTTPException(
            status_code=404, detail=f"exercise with id {exercise_id} not found.")

    return db_exercise.sets


def create_exercise(db: Session, exercise: ExerciseCreate, workout_id: int):

    if not get_workout(db, workout_id):
        raise HTTPException(
            status_code=404, detail=f"workout_id {workout_id} not found.")

    db_exercise = Exercise(title=exercise.title,
                           workout_id=workout_id, details=exercise.details)
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise


def update_exercise(db: Session,  exercise_id: int, exercise: ExerciseUpdate):
    exercise_db = get_exercise(db, exercise_id)

    if not exercise_db:
        raise HTTPException(status_code=404, detail="Exercise not found.")

    exercise_data = exercise.dict(exclude_unset=True)

    for key, value in exercise_data.items():
        setattr(exercise_db, key, value)

    db.add(exercise_db)
    db.commit()
    db.refresh(exercise_db)
    return exercise_db


def delete_exercise(db: Session, exercise_id: int):
    exercise = get_exercise(db,  exercise_id)

    if not exercise:
        raise HTTPException(status_code=404, detail='exercise not found')

    db.delete(exercise)
    db.commit()
    return exercise
