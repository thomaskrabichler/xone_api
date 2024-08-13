from fastapi import Request, Depends
from app.config import firebase_config as admin
from fastapi import Request, HTTPException


def get_current_user(request: Request):
    jwt = request.headers.get('authorization')
    decoded_user = admin.auth.verify_id_token(jwt)
    if decoded_user:
        return decoded_user


def get_uid(request: Request) -> str: 
    user = get_current_user(request)
    if user:
        print('huhu{}'.format(user['uid']))
        return user['uid']
    else:
        return ''

def check_user(request: Request, user_id:str):



    if not (get_uid(request) == user_id):
        raise HTTPException(
            status_code=401, detail= "Unauthorized. Please provide your own User ID.")

def verify_token(request: Request):
    jwt = request.headers.get('authorization')
    decoded_token = admin.auth.verify_id_token(jwt)
    if (decoded_token):
        uid = decoded_token['uid']
        return uid
    else:
        raise HTTPException(status_code=401, detail="Not authorized")
