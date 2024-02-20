from typing import List
from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

# Database
from app.databaseutils import get_db

# Models
from app.model.users import AppointmentModel
# from app.model.appointment import AppointmentModel

# Schemas
from app.schema.users import CreateUserSchema
from app.schema.appointment import CreateAppointmentSchema, UpdateAppointmentSchema

# Router
from app.router.users import get_current_active_user

router = APIRouter(prefix='/appointments', tags=['Appointments'])


@router.get("/appointment") #, response_model=List[])
def get_appointment(current_user: CreateUserSchema = Depends(get_current_active_user), db: Session = Depends(get_db)):
    appointments = db.query(AppointmentModel).all()
    return appointments

@router.post("/create_appointment")
def create_appointment(appointment: CreateAppointmentSchema, db: Session = Depends(get_db), current_user: CreateUserSchema = Depends(get_current_active_user)):
    db_appointment = AppointmentModel(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return "Create Success"


@router.put("/update_appointment")
def update_appointment(appointment: UpdateAppointmentSchema, db: Session = Depends(get_db), current_user: CreateUserSchema = Depends(get_current_active_user)):
    db_appointment = db.query(AppointmentModel).filter(AppointmentModel.id == appointment.id).update({
        "user_id": appointment.user_id,
        "sub_treatment_id": appointment.sub_treatment_id,
        "appointment_time": appointment.appointment_time,
        "status": appointment.status
    })
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return "Update Success"



@router.delete("/delete_appointment")
def delete_appointment(id: int, db: Session = Depends(get_db), current_user: CreateUserSchema = Depends(get_current_active_user)):
    db_appointment = db.query(AppointmentModel).filter(AppointmentModel.id == id).delete()
    db.commit()
    db.refresh(db_appointment)
    return "Deleted Success"