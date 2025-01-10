from fastapi import FastAPI
from app.models import User
from app.schemas import UserCreate, UserLogin
from app.auth import create_user, authenticate_user

app = FastAPI()

# In-memory database for simplicity
db = {}

# Register endpoint
@app.post("/register")
async def register(user: UserCreate):
    if user.username in db:
        return {"error": "User already exists"}
    db[user.username] = create_user(user)
    return {"message": "User registered successfully"}

# Login endpoint
@app.post("/login")
async def login(user: UserLogin):
    token = authenticate_user(user, db)
    if not token:
        return {"error": "Invalid credentials"}
    return {"access_token": token}
