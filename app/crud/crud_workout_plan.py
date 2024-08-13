from http.client import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from app.models.workout_plan import WorkoutPlan
from app.crud.crud_user import get_user
from app.schemas.workout_plan_workout import WorkoutPlanCreate, WorkoutPlanUpdate
from fastapi import HTTPException, Request
from typing import List, Optional

from app.api.security import auth


def get_workout_plan(db: Session, workout_plan_id: int):

    try:
        workout_plan = db.query(WorkoutPlan).filter(
            WorkoutPlan.id == workout_plan_id).one()
        return workout_plan
    except NoResultFound:
        raise HTTPException(
            status_code=400, detail=f'no workout plan found with id {workout_plan_id}')


def get_workout_plans(db: Session, user_id: str) -> List[WorkoutPlan]:

    return db.query(WorkoutPlan).filter(WorkoutPlan.user_id == user_id).all()


def create_workout_plan(db: Session, workout_plan: WorkoutPlanCreate, user_id: str):

    
    db_workout_plan = WorkoutPlan(title=workout_plan.title, user_id=user_id)
    db.add(db_workout_plan)
    db.commit()
    db.refresh(db_workout_plan)
    return db_workout_plan


def update_workout_plan(db: Session,  workout_plan_id: int, workout_plan: WorkoutPlanUpdate):
    workout_plan_db = get_workout_plan(db, workout_plan_id)

    if not workout_plan_db:
        raise HTTPException(status_code=400, detail="No plan found")

    workout_plan_data = workout_plan.dict(exclude_unset=True)

    for key, value in workout_plan_data.items():
        setattr(workout_plan_db, key, value)

    db.add(workout_plan_db)
    db.commit()
    db.refresh(workout_plan_db)
    return workout_plan_db


def delete_workout_plan(db: Session, plan_id: int):
    plan_db = get_workout_plan(db,  plan_id)

    if not plan_db:
        raise HTTPException(status_code=404, detail='set not found')

    db.delete(plan_db)
    db.commit()
    return plan_db
