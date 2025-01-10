import jwt
import hashlib
from datetime import datetime, timedelta

SECRET_KEY = "supersecretkey"

# Hash password using SHA256
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Create a new user
def create_user(user_data):
    hashed_password = hash_password(user_data.password)
    return {"username": user_data.username, "hashed_password": hashed_password}

# Authenticate user and generate JWT
def authenticate_user(user_data, db):
    hashed_password = hash_password(user_data.password)
    user = db.get(user_data.username)
    if not user or user["hashed_password"] != hashed_password:
        return None

    token = jwt.encode(
        {"username": user_data.username, "exp": datetime.utcnow() + timedelta(hours=24)},
        SECRET_KEY,
        algorithm="HS256"
    )
    return token
