from fastapi import APIRouter
import app.crud.crud_workout_plan as crud_workout_plan
from app.schemas.workout_plan_workout import *
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app.api import deps
from app.api.security import auth
from app.crud.crud_user import get_user
router = APIRouter()


@router.get("/workout-plans",  response_model=List[WorkoutPlan])
def read_workout_plans(db: Session = Depends(deps.get_db), user_id: str = Depends(auth.verify_token)):
    """
     Returns all Workout Plans from the user.
    """
    try:

        return crud_workout_plan.get_workout_plans(db, user_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to retrieve workout plans: {str(e)}")
    


@router.get("/workout-plans/{workout_plan_id}",  response_model=WorkoutPlan)
def read_workout_plan(workout_plan_id: int,  db: Session = Depends(deps.get_db)):
    """
     Returns a single workout plan.
    """
    try:
        return crud_workout_plan.get_workout_plan(db, workout_plan_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to retrieve workout plan: {str(e)}")


@router.post("/workout-plans", response_model=WorkoutPlan)
def create_workout_plan(
    workout_plan: WorkoutPlanCreate, uid: str = Depends(auth.verify_token), db: Session = Depends(deps.get_db)
):
    try:
        return crud_workout_plan.create_workout_plan(db=db, workout_plan=workout_plan, user_id=uid)

    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to create workout plan: {str(e)}")

@router.patch("/workout-plans/{workout_plan_id}", response_model=WorkoutPlan)
def update_workout_plan(workout_plan_id: int, workout_plan: WorkoutPlanUpdate,  db: Session = Depends(deps.get_db)):
    return crud_workout_plan.update_workout_plan(db, workout_plan_id, workout_plan)


@router.delete("/workout-plans/{workout_plan_id}")
def delete_workout_plan(workout_plan_id: int, db: Session = Depends(deps.get_db)):
    """
     Delete a workout_plan
    """
    return crud_workout_plan.delete_workout_plan(db, workout_plan_id)
