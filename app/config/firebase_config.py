import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import os 
data = os.path.abspath(os.path.dirname(__file__)) + "/service_account.json"
cred = credentials.Certificate(data)
firebase_admin.initialize_app(cred)

