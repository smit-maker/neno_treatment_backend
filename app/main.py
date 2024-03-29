import os
import subprocess
from app.schema.appointment import AppointmentSchema
from app.schema.treatments import TreatmentSchema
from pydantic import BaseModel
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Database
from .database import engine, Base
from .databaseutils import get_db

# Routers
from app.router.users import get_branches, get_current_active_user, get_users
from app.router.users import router as usersRouter

from app.router.treatments import get_treatments
from app.router.treatments import router as treatmentsRouter

from app.router.appointment import get_appointment
from app.router.appointment import router as appointmentsRouter

from app.router.firebase import router as firebaseRouter

# Schema
from app.schema.users import BranchSchema, CurrentUser

# Models
# from .model import UserModel
from app.model.users import UserModel # BranchModel

def create_app():
    Base.metadata.create_all(bind=engine)
    # Base.metadata.drop_all(bind=engine)

    app = FastAPI(debug=True)
    
    # Set up CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Add the origin of your React app | "http://localhost:5173", "https://fastapi-on-koyeb-smitinfotech.koyeb.app",
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )

    app.include_router(usersRouter)
    app.include_router(treatmentsRouter)
    app.include_router(appointmentsRouter)
    app.include_router(firebaseRouter)

    return app

app = create_app()

class Master(BaseModel):
    branches: List[BranchSchema]

class MainSchema(BaseModel):
    me: Optional[CurrentUser]
    users: Optional[List[CurrentUser]]
    master: Optional[Master]
    # master: Optional[List[BranchSchema]]
    treatments: Optional[List[TreatmentSchema]]
    appointment: Optional[List[AppointmentSchema]]

    # class Config:
    #     from_attributes = True


@app.get("/", response_model=MainSchema)
def main(current_user: CurrentUser = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = {
        "me": current_user,
        "users": get_users(current_user, db),
        "master": {
            "branches": get_branches(current_user, db),
        },
        "treatments": get_treatments(current_user, db),
        "appointment": get_appointment(current_user, db),
    }
    return data

@app.post("/run_command/")
async def run_command(command: str):
    try:
        # Run the command using subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        # Check if the command was successful
        if result.returncode == 0:
            return {"output": result.stdout}
        else:
            # If the command failed, raise an HTTPException with the error message
            raise HTTPException(status_code=500, detail=result.stderr)
    except Exception as e:
        # Handle any other exceptions
        raise HTTPException(status_code=500, detail=str(e))

def find_alembic_ini(start_dir):
    # Walk through the directory tree to find alembic.ini file
    for root, dirs, files in os.walk(start_dir):
        if 'alembic.ini' in files:
            return os.path.join(root, 'alembic.ini')
    raise FileNotFoundError("alembic.ini not found")

@app.post("/upgrade_alembic")
async def upgrade_alembic():
    try:
        # Find alembic.ini file in the current directory
        alembic_ini_path = find_alembic_ini(os.getcwd())
        # Run the command using subprocess
        result = subprocess.run(["alembic", "--config", alembic_ini_path, "upgrade", "head"], capture_output=True, text=True)
        # Check if the command was successful
        if result.returncode == 0:
            return {"message": "Alembic upgrade successful"}
        else:
            # If the command failed, raise an HTTPException with the error message
            raise HTTPException(status_code=500, detail=result.stderr)
    except Exception as e:
        # Handle any other exceptions
        raise HTTPException(status_code=500, detail=str(e))
    
