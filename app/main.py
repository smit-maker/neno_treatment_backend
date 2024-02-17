import os
import subprocess

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Database
from .database import engine, Base

# Routers
from app.router.users import router as usersRouter
from app.router.treatments import router as treatmentsRouter
from app.router.firebase import router as firebaseRouter

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
    app.include_router(firebaseRouter)

    return app

app = create_app()

@app.get("/")
def read_root():
    return {"Hello": "World"}



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