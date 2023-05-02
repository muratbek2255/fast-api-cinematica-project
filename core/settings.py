import os

from core.local_config import *


PROJECT_NAME = "Scooter_KG"
SERVER_HOST = 'http://127.0.0.1:8080'

# Secret key
SECRET_KEY = b"awubsyb872378t^*TG8y68&*&&*8y8yg9POB)*896ft7CR^56dfYUv"

# BASE DIR
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# HOW TO START API
API_V1_STR = "/api/v1"

# Token 60 minutes * 24 hours * 8 days = 8 days
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

# CORS
BACKEND_CORS_ORIGINS = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:8080",
]

# Data Base
SQLALCHEMY_DATABASE_URI = (
    f'postgresql://{POSTGRES_USER}:'
    f'{POSTGRES_PASSWORD}@'
    f'{POSTGRES_SERVER}/'
    f'{POSTGRES_DB}'
)

USERS_OPEN_REGISTRATION = True
