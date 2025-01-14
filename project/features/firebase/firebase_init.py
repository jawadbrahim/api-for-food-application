import firebase_admin
from firebase_admin import credentials
from project.config.development import Development

def init_credential():
    cred=credentials.Certificate(Development.FIREBASE_PATH)
    firebase_admin.initialize_app(cred)