
from fastapi import APIRouter
import app.crud.crud_set as crud_set
import app.crud.crud_set_history as crud_set_history
from app.schemas.set_history import *
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends, HTTPException
from app.api import deps

router = APIRouter()


@router.get("/exercises/{exercise_id}/archived_sets", response_model=List[SetHistory])
def read_archived_sets(exercise_id: int, db: Session = Depends(deps.get_db)):
    """
     Returns all archived sets.
    """

    try:
        return crud_set_history.get_archived_sets(db, exercise_id)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to retrieve archived set: {str(e)}")

