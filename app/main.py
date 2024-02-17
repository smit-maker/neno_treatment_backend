from typing import Union

from fastapi import FastAPI
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


    