from fastapi import FastAPI
from app.config import firebase_config as admin
from app.api.routers import exercise, set, user, workout_plan, workout, set_history
from fastapi import Request, Depends
from app.api.routers.test.initialize_test_db import  router as test_router
from fastapi.security import OAuth2PasswordBearer
import sys, os

from app.models.set_history import SetHistory
from app.db.session import Base, engine

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


#Base.metadata.create_all(bind=engine)


#CZyfp9apZFZhRVqXrqpTOcyppl43 
#CZyfp9apZFZhRVqXrqpTOcyppl43 
#CZyfp9apZFZhRVqXrqpTOcyppl43 
#CZyfp9apZFZhRVqXrqpTOcyppl43 
#CZyfp9apZFZhRVqXrqpTOcyppl43 
#1PukcXgTAOTrFRz9a4GdY5kb5j73 
#1PukcXgTAOTrFRz9a4GdY5kb5j73 
#1PukcXgTAOTrFRz9a4GdY5kb5j73 
#1PukcXgTAOTrFRz9a4GdY5kb5j73 
#1PukcXgTAOTrFRz9a4GdY5kb5j73 
#1PukcXgTAOTrFRz9a4GdY5kb5j73 
#1PukcXgTAOTrFRz9a4GdY5kb5j73 
#1PukcXgTAOTrFRz9a4GdY5kb5j73 
#1PukcXgTAOTrFRz9a4GdY5kb5j73 
app = FastAPI()

'''TODO: BEI ALLEN ROUTERN, die user_id als Parameter entfernen (Siehe WorkoutPlan Router read-all).
Im Frontend muss man also nicht mehr die Userid ubergeben.!!!
    Der Token wird direkt bei jeder function in den routern als dependency ubergeben, so erhält man die uid und kann diese
    der DB-Query übergeben. 

    Allerdings erst zum Schluss implementieren, ansonsten wird das Testen in den Docs umständlich.
'''

# TODO: Bei allen feldern wie workoutTitle, planTitle, checken ob der name nicht schon verwendet worden ist
#! Aktuell wurde die middleware als dependency outgesourced, n
# @app.middleware("http")
# async def check_jwt(request: Request, call_next):
#     jwt = request.headers.get('authorization')
#     decoded_token = admin.auth.verify_id_token(jwt)
#     # print(decoded_token)
#     if (decoded_token) :
#        return await call_next(request)
#     else:
#         print('not auto')

#     return {"message": "not authorized"}


#TODO: evtl dependency hier entfernen, da wir sie jetzt bei jeder router function aufrufen
#app.include_router(user.router, dependencies=[Depends(auth.verify_token)])
#
#app.include_router(workout_plan.router, dependencies=[
#                   Depends(auth.verify_token)])
#
#app.include_router(workout.router, dependencies=[Depends(auth.verify_token)])
#
#app.include_router(exercise.router, dependencies=[Depends(auth.verify_token)])
#
#app.include_router(set.router, dependencies=[Depends(auth.verify_token)])


#! uncomment, to test it in the docs
app.include_router(user.router)

app.include_router(workout_plan.router)

app.include_router(workout.router)

app.include_router(exercise.router)

app.include_router(set.router)

app.include_router(set_history.router)
app.include_router(test_router)

#Base.metadata.create_all(bind=engine)

@app.get("/")
async def root(request: Request):

    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8080)
