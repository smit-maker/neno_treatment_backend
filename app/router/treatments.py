from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

# Database
from app.databaseutils import get_db

# Schemas
from app.schema.users import CreateUserSchema

# Router
from app.router.users import get_current_active_user

router = APIRouter(prefix='/treatments', tags=['Treatments'])



@router.get("/")
def get_treatments(db: Session = Depends(get_db)): # current_user: CreateUserSchema = Depends(get_current_active_user),
    pass
    # users = db.query(UserModel).all()
    # return users
