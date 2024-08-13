from fastapi import APIRouter
from datetime import datetime
from sqlalchemy.orm import Session
from app.models import Exercise, User, Set, SetHistory, Workout, WorkoutPlan, workout_plan_workouts
from app.db import engine, Base


router = APIRouter()


@router.get("/test/init_db")
def init_db():

    db = Session(bind=engine)
    user = User(id="1", email="test@test.com", name="John Doe",
                weight="75", height="180", birth_date="1990-01-01", gender="male")
    db.add(user)
    db.commit()

    # create a test workout plan for the user
    workout_plan = WorkoutPlan(title="Test Workout Plan", user_id=user.id)
    db.add(workout_plan)
    db.commit()

    # create a test workout for the workout plan
    workout = Workout(title="Test Workout", user_id=user.id)
    workout_plan.workouts.append(workout)
    db.commit()

    # create some test exercises for the workout
    exercise1 = Exercise(title="Bench Press",
                         details="Barbell", user_id=user.id)
    exercise2 = Exercise(
        title="Squats", details="Rack", user_id=user.id)
    workout.exercises.extend([exercise1, exercise2])
    db.commit()

    # create some test sets for the exercises
    set1 = Set(reps=8, weight=100.0, is_done=False,
               exercise_id=exercise1.id, user_id=user.id, position=1)
    set2 = Set(reps=8, weight=80.0, is_done=False,
               exercise_id=exercise2.id, user_id=user.id, position=2)
    db.add_all([set1, set2])
    db.commit()

    # create some test set histories for the sets
    set_history1 = SetHistory(
        set_id=set1.id, exercise_id=exercise1.id, reps=8, weight=100.0, position=1)
    set_history2 = SetHistory(
        set_id=set2.id, exercise_id=exercise2.id, reps=8, weight=80.0, position=2)
    db.add_all([set_history1, set_history2])
    db.commit()
    return 'success'
