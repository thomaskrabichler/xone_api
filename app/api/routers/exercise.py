from fastapi import APIRouter
import app.crud.crud_exercise as crud_exercise
from app.schemas.exercise import *
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app.api import deps
from app.crud.crud_workout import get_workout

router = APIRouter()


@router.post("/exercises/{workout_id}", response_model=Exercise)
def create_exercise(
    workout_id: int, exercise: ExerciseCreate, db: Session = Depends(deps.get_db),
):
    try:
        if not get_workout(db, workout_id):
            raise HTTPException(
                status_code=404, detail=f"Workout with id {workout_id} not found.")
        return crud_exercise.create_exercise(db=db, exercise=exercise, workout_id=workout_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to create exercise: {str(e)}")



@router.get("/exercises/{exercise_id}/sets", response_model=List[Set])
def read_sets(exercise_id: int, db: Session = Depends(deps.get_db)):
    try:
        return crud_exercise.get_sets(db, exercise_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to retrieve sets: {str(e)}")

@router.patch("/exercises/{exercise_id}", response_model=Exercise)
def update_exercise(exercise_id: int, exercise: ExerciseUpdate, db: Session = Depends(deps.get_db)):
    # Updates title, detail only. not sets/weight...
    try:
     return crud_exercise.update_exercise(db, exercise_id, exercise)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to update exercise: {str(e)}")


@router.delete("/exercises/{exercise_id}")
def delete_exercise(exercise_id: int, db: Session = Depends(deps.get_db)):
    """
     Delete a exercise
    """
    try:
        return crud_exercise.delete_exercise(db, exercise_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to delete exercise: {str(e)}")
