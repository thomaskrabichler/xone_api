from fastapi import APIRouter
import app.crud.crud_set as crud_set
from app.schemas.set import *
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends, HTTPException
from app.api import deps
from app.api.security import auth
from app.crud.crud_exercise import get_exercise

router = APIRouter()
#!: Uncomment auth.check_user() when testing with flutter


@router.post("/sets/{exercise_id}", response_model=Set)
def create_set(
    set: SetCreate, exercise_id: int, db: Session = Depends(deps.get_db)
):
    """
     Creates a single Set to the specified exercise_id.
    """
    #try:
    if not get_exercise(db, exercise_id):
            raise HTTPException(
                status_code=404, detail=f"Exercise with id {exercise_id} not found.")
    return crud_set.create_set(db=db, set=set, exercise_id=exercise_id)
    #except Exception as e:
    #    raise HTTPException(
           # status_code=400, detail=f"Failed to create set: {str(e)}")


# Returns a single set
@router.get("/sets/{set_id}", response_model=Set)
def read_set(set_id: int, db: Session = Depends(deps.get_db)):
    """
     Returns a single Set from the specified set_id.
    """
    try:
        return crud_set.get_set(db, set_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to retrieve set: {str(e)}")

# Returns all sets from the exercise with {exercise_id}


@router.get("/sets/{exercise_id}", response_model=List[Set])
def read_sets(exercise_id: int, db: Session = Depends(deps.get_db)):
    """
     Returns all Sets from the specified Exercise.
    """

    try:
        return crud_set.get_sets(db, exercise_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to retrieve sets: {str(e)}")


@router.patch("/sets/{set_id}", response_model=Set)
def update_set(set_id: int, set: SetUpdate,  db: Session = Depends(deps.get_db)):
    """
     Update weight and reps of a set.
    """
    try:
        return crud_set.update_set(db, set_id, set)

    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to update set: {str(e)}")


@router.delete("/sets/{set_id}")
def delete_set(set_id: int, db: Session = Depends(deps.get_db)):
    """
     Delete a set.
    """
    try:
        return crud_set.delete_set(db, set_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to delete set: {str(e)}")
