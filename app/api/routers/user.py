from fastapi import Request
from fastapi import APIRouter
import app.crud.crud_user as crud_user
from app.schemas.user import *
from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException
from app.api import deps
from time import sleep
from app.api.security import auth
router = APIRouter()


@router.get("/users/", response_model=List[User])
def read_users(db: Session = Depends(deps.get_db)):
    #! For testing purposes only.
    users = crud_user.get_users(db)
    return users


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: str, db: Session = Depends(deps.get_db)):
#def read_user(user_id: str, uid: str = Depends(auth.verify_token), db: Session = Depends(deps.get_db)):
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user


@router.get("/users/{user_id}/workout_plan")
def read_selected_plan(user_id: str,  uid: str = Depends(auth.verify_token), db: Session = Depends(deps.get_db)):
    if user_id != uid:
        raise HTTPException(
            status_code=401, detail="Unauthorized.")
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    selected_plan = crud_user.get_selected_plan(db=db, user_id=user_id)
    return selected_plan


@router.put("/users/{user_id}/workout_plan/{plan_id}")
async def set_selected_plan(user_id: str, plan_id: int,  uid: str = Depends(auth.verify_token), db: Session = Depends(deps.get_db)):
    if user_id != uid:
        raise HTTPException(
            status_code=401, detail="Unauthorized.")
    try:
        crud_user.set_selected_plan(user_id=user_id, db=db, plan_id=plan_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"message": f"Selected plan {plan_id} has been set for user {user_id}."}


@router.post("/users", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(deps.get_db)):
    sleep(3)
    try:
        return crud_user.create_user(db=db, user=user)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to create user: {str(e)}")


@router.patch("/users/{user_id}", response_model=User)
def update_user(user: UserUpdate, user_id: str, uid: str = Depends(auth.verify_token), db: Session = Depends(deps.get_db)):
    if user_id != uid:
        raise HTTPException(
            status_code=401, detail="Unauthorized.")
    try:
        return crud_user.update_user(db, user, user_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to update user: {str(e)}")

