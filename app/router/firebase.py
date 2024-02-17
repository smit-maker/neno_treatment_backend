from app.auth.firebase_auth import signUp, signIn, Users
from pydantic import BaseModel

from fastapi import Depends, APIRouter, HTTPException, status, Query

# Database
from app.databaseutils import get_db

router = APIRouter(prefix='/firebase', tags=['Firebase'])


@router.get("/firebase_signup")
async def firebase_signup(email:str, password:str):
    data = signUp(email, password)
    return data

class User(BaseModel):
    email: str
    password: str

@router.post("/firebase_signin")
def firebase_signin(user: User):
    data = signIn(user.email, user.password)
    return data

@router.get("/firebase_users")
async def firebase_users():
    data = Users()
    return data
