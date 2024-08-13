from sqlalchemy.orm import Session
from app.models.workout import Workout
from app.models.exercise import Exercise
from typing import List

from app.schemas.workout_plan_workout import WorkoutCreate
from app.schemas.workout import WorkoutUpdate
from app.crud.crud_workout_plan import get_workout_plan
from fastapi import HTTPException, Request


def get_workout(db: Session, workout_id: int):
    return db.query(Workout).filter(Workout.id == workout_id).first()


def get_workouts(db: Session, workout_plan_id: int) -> List[Workout]:
    if not get_workout_plan(db, workout_plan_id):
        raise HTTPException(
            status_code=404, detail=f"Workout Plan with id {workout_plan_id} not found.")
    plan_db = get_workout_plan(db, workout_plan_id)
    return plan_db.workouts


def get_exercises_by_workout(db: Session, workout_id: int):
    return db.query(Exercise).filter(Exercise.workout_id == workout_id).all()

def create_workout(db: Session, workout: WorkoutCreate, workout_plan_id: int):

    if not get_workout_plan(db, workout_plan_id):
        raise HTTPException(
            status_code=404, detail=f"Workout Plan with id {workout_plan_id} not found.")

# TODO: Hier wird 2 mal get_workout_plan aufgerufen. Aendern sodass nur 1 mal angerufen wird
    db_workout = Workout(title=workout.title)
    db_plan = get_workout_plan(db, workout_plan_id)
    db_workout.workout_plans.append(db_plan)
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

def update_workout(db: Session,  workout_id: int, workout: WorkoutUpdate):
    workout_db = get_workout(db, workout_id)

    if not workout_db:
        raise HTTPException(status_code=404, detail="Workout not found.")

    workout_data = workout.dict(exclude_unset=True)

    for key, value in workout_data.items():
        setattr(workout_db, key, value)

    db.add(workout_db)
    db.commit()
    db.refresh(workout_db)
    return workout_db



def delete_workout(db:Session, workout_id: int):
    workout_db =get_workout(db,  workout_id)

    if not workout_db:
        raise HTTPException(status_code=404, detail='workout not found')

    db.delete(workout_db)
    db.commit()
    return workout_db
