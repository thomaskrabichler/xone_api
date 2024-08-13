import re
from sqlalchemy.orm import Session, exc
from app.models.user import User
from app.models.workout_plan import WorkoutPlan
from app.schemas.user import UserCreate, UserUpdate
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import and_


def get_user(db: Session, user_id: str) -> User:
    try:
        return db.query(User).filter(User.id == user_id).one()
    except NoResultFound:
        raise HTTPException(
            status_code=404, detail='User with id {} not found'.format(user_id))


def update_selected_plan_after_workout_plan_deletion(db: Session, workout_plan_id: str):
    workout_plan = db.query(WorkoutPlan).get(workout_plan_id)
    if workout_plan:
        user = workout_plan.user
        next_workout_plan = db.query(WorkoutPlan).filter(
            and_(WorkoutPlan.user_id == user.id,
                 WorkoutPlan.id != workout_plan_id)
        ).first()
        if next_workout_plan:
            user.selected_plan = next_workout_plan
        else:
            user.selected_plan = None
        db.commit()


def get_user_by_email(db: Session, email: str):
    try:
        return db.query(User).filter(User.email == email).one()
    except NoResultFound:
        raise HTTPException(
            status_code=404, detail='User with email {} not found'.format(email))


def get_users(db: Session):
    return db.query(User).all()


def check_current_user(db: Session, user_id: str):
    pass


def set_selected_plan(db: Session, user_id: str, plan_id: int):
    user = get_user(db=db, user_id=user_id)
   
    try:
        workout_plan = db.query(WorkoutPlan).filter_by(id=plan_id).first()
        user.selected_plan = workout_plan

        db.commit()
        db.refresh(user)
    except HTTPException:
        raise HTTPException(
            status_code=400, detail=f"Failed to set selected_plan {plan_id} for user {user_id}")


def get_selected_plan(db: Session, user_id: str):
    user = get_user(user_id=user_id, db=db)
    selected_plan = user.selected_plan
    if selected_plan:
        return selected_plan.id
    else:
        return None

def delete_user(db: Session, user_id: str):
    # TODO: user_id parameter entfernen und stattdessen current user holen
    pass


def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, id=user.id, gender=user.gender,
                   birth_date=user.birth_date, height=user.height, weight=user.weight, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: UserUpdate, user_id: str):

    user_db = get_user(db, user_id)

    if not user_db:
        raise HTTPException(status_code=404, detail="User not found.")
    user_data = user.dict(exclude_unset=True)
    print(user_data)
    for key, value in user_data.items():
        setattr(user_db, key, value)

    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

    # user_db = user_db.__dict__
    # stored = UserUpdate(**user_db)
    # update_data =  user.dict(exclude_unset=True)
    # updated_user = stored.copy(update=update_data)
    # user_db = jsonable_encoder(updated_user)
    # user_db.email=user.email
    # user_db.name=user.name
    # db.commit()

    return user_db

    # if user_db:
    #     user_db.name = user.name
    #     user_db.weight = user.weight
    #     user_db.height = user.height
    #     user_db.birth_date = user.birth_date
    # db.commit()

    if not user_db:
        raise HTTPException(
            status_code=404, detail=f"user with it {user_id} not found.")

    return updated_user
