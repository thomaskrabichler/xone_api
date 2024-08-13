from fastapi import APIRouter
import app.crud.crud_workout as crud_workout
from app.schemas.workout import *
from sqlalchemy.orm import Session

from app.schemas.workout_plan_workout import WorkoutCreate
from fastapi import Depends, Request, HTTPException
from app.api import deps
from app.crud.crud_workout_plan import get_workout_plan
router = APIRouter()

#!: Uncomment auth.check_user() when testing with flutter


@router.get("/workout-plans/{workout_plan_id}/workouts", response_model=List[Workout])
def read_workouts(workout_plan_id: int,   db: Session = Depends(deps.get_db)):
    try:
        return crud_workout.get_workouts(db,  workout_plan_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to retrieve workouts: {str(e)}")

@router.get("/workouts/{workout_id}", response_model=Workout)
def read_workout(workout_id: int, db: Session = Depends(deps.get_db)):
    try:
        return crud_workout.get_workout(db, workout_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to retrieve workout: {str(e)}")


@router.get("/workouts/{workout_id}/exercises", response_model=List[Exercise])
def read_exercises_by_workout(workout_id: int, db: Session = Depends(deps.get_db)):
    try:
        return crud_workout.get_exercises_by_workout(db, workout_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to retrieve exercises: {str(e)}")

@router.post("/workouts/{workout_plan_id}", response_model=Workout)
def create_workout(
    workout_plan_id: int, workout: WorkoutCreate, request: Request, db: Session = Depends(deps.get_db),
):
    try:
        if not get_workout_plan(db, workout_plan_id):
            raise HTTPException(
                status_code=404, detail=f"Workout Plan with id {workout_plan_id} not found.")

        return crud_workout.create_workout(db=db, workout=workout, workout_plan_id=workout_plan_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to create workout: {str(e)}")


@router.patch("/workouts/{workout_id}", response_model=Workout)
def update_workout(workout_id: int, workout: WorkoutUpdate, db: Session = Depends(deps.get_db)):
    try:
        return crud_workout.update_workout(db, workout_id, workout)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to update workout: {str(e)}")


@router.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int, db: Session = Depends(deps.get_db)):
    """
     Delete a workout
    """
    try:
        return crud_workout.delete_workout(db, workout_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to delete workout: {str(e)}")
