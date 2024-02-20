from typing import List
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

# Auth
from app.auth.auth import authenticate_user, create_access_token

# Database
from app.databaseutils import get_db

# Model
from app.model.users import UserModel, BranchModel

# Schemas
from app.schema.users import BranchSchema, Token, TokenData, CurrentUser, CreateUserSchema, UpdateUserSchema, CreateBranchSchema, UpdateBranchSchema

router = APIRouter(prefix='/users', tags=['Users'])

# To get a string like this run:
SECRET_KEY  = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM   = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
password_hashing = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ------------------------------------- Methods ----------------------------------------------------

# Users ============================================================================================
def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    
    except JWTError:
        raise credentials_exception
    
    user = db.query(UserModel).filter(UserModel.username == token_data.username).first()

    data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "password": user.password,
        "disabled": user.disabled,
    }

    if user is None:
        raise credentials_exception
    
    return user


def get_user_by_id(user_id: int, db: Session):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def create_user(user: str, db: Session):
    if db.query(UserModel).filter(UserModel.username == user.username).first():
        return {"code": 409, "data": "", "msg": "User already exists"}

    hashed_password = password_hashing.hash(user.password)
    db_user = UserModel(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"code": 200, "data": db_user, "msg": "success"}


def update_user(user_id: int, updated_user: CreateUserSchema, db: Session):
    db_user = get_user_by_id(user_id, db)
    if db_user:
        print(f" --- updated_user.dob : {updated_user.dob}")
        print(f" --- updated_user.dob type : {type(updated_user.dob)}")
        # date_obj = datetime.strptime(db_user.dob, "%d-%m-%Y hh:mm:ss") # updated_user.dob
        # print(f" --- date_obj : {date_obj}")
        # print(f" --- date_obj type : {type(date_obj)} ")

        if updated_user.username : db_user.username = updated_user.username
        if updated_user.password : db_user.password = password_hashing.hash(updated_user.password)
        if updated_user.f_name   : db_user.f_name = updated_user.f_name
        if updated_user.l_name   : db_user.l_name = updated_user.l_name
        if updated_user.profile_picture: db_user.profile_picture = updated_user.profile_picture
        if updated_user.dob      : db_user.dob = updated_user.dob
        if updated_user.gender   : db_user.gender = updated_user.gender
        if updated_user.email    : db_user.email = updated_user.email
        if updated_user.branch_id: db_user.branch_id = updated_user.branch_id

        db.commit()
        db.refresh(db_user)
        return {"code": 200, "data": db_user, "msg": "success"}
    

def get_current_active_user(current_user: CurrentUser = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# ----------------------------------------- Routers ------------------------------------------------

# ////// Users

@router.get("/me", response_model=CurrentUser)
def me(current_user: CurrentUser = Depends(get_current_active_user)):
    return current_user


@router.get("/")
def get_users(current_user: CreateUserSchema = Depends(get_current_active_user), db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users


@router.post("/signin", response_model=Token)
def sign_in(form_data: CreateUserSchema, db: Session = Depends(get_db)): # OAuth2PasswordRequestForm = Depends()
    # user = db.query(UserModel).filter(UserModel.username == form_data.username).first()

    # if user == None:
    #     return {"code": 400, "data": "", "msg": "User Not Found"}

    user = authenticate_user(form_data.username, form_data.password, db)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signup")
def sign_up(user: CreateUserSchema, db: Session = Depends(get_db)):
    
    return create_user(user, db)
    

@router.put("/profile_update")
def profile_update(user: UpdateUserSchema, current_user: CreateUserSchema = Depends(get_current_active_user), db: Session = Depends(get_db)):
    
    return update_user(user.id, user, db)
    

# /////// branches

@router.get("/branches", response_model=List[BranchSchema])
def get_branches(current_user: CreateUserSchema = Depends(get_current_active_user), db: Session = Depends(get_db)):
    branches = db.query(BranchModel).all()
    return branches


@router.post("/create_branch")
def create_branch(branch: CreateBranchSchema, db: Session = Depends(get_db)):
    db_branch = BranchModel(name=branch.name)
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    return "success"
    

@router.put("/update_branch")
def update_branch(branch: UpdateBranchSchema, db: Session = Depends(get_db)):
    db_branch = db.query(BranchModel).filter(BranchModel.id == branch.id).first()
    if branch.name: db_branch.name = branch.name
    
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    
    return "success"

# Routers ------------------------------------------------------------------------------------------


