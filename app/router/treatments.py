from typing import List
from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

# Database
from app.databaseutils import get_db

# Models
from app.model.users import SubTreatmentModel, TreatmentModel
# from app.model.treatments import SubTreatmentModel, TreatmentModel

# Schemas
from app.schema.users import CreateUserSchema
from app.schema.treatments import TreatmentSchema, CreateTreatmentSchema, UpdateTreatmentSchema, CreateSubTreatmentSchema, UpdateSubTreatmentSchema

# Router
from app.router.users import get_current_active_user

router = APIRouter(prefix='/treatments', tags=['Treatments'])

# Treatments
@router.get("/treatment", response_model=List[TreatmentSchema])
def get_treatments(current_user: CreateUserSchema = Depends(get_current_active_user), db: Session = Depends(get_db)):
    treatments = db.query(TreatmentModel).all()

    return treatments

@router.post("/create_treatment")
def create_treatment(treatment: CreateTreatmentSchema, db: Session = Depends(get_db), current_user: CreateUserSchema = Depends(get_current_active_user)):
    db_treatment = TreatmentModel(name=treatment.name, treatments_picture=treatment.treatments_picture)
    db.add(db_treatment)
    db.commit()
    db.refresh(db_treatment)
    return "success"
    
@router.put("/update_treatment")
def update_treatment(treatment: UpdateTreatmentSchema, db: Session = Depends(get_db)):
    db_treatment = db.query(TreatmentModel).filter(TreatmentModel.id == treatment.id).first()
    if treatment.name: db_treatment.name = treatment.name
    
    db.add(db_treatment)
    db.commit()
    db.refresh(db_treatment)
    
    return "success"


# Sub Treatments
@router.get("/sub_treatments")
def get_sub_treatments(current_user: CreateUserSchema = Depends(get_current_active_user), db: Session = Depends(get_db)):
    treatments = db.query(SubTreatmentModel).all()

    return treatments

@router.post("/create_sub_treatments")
def create_sub_treatment(sub_treatment: CreateSubTreatmentSchema, db: Session = Depends(get_db), current_user: CreateUserSchema = Depends(get_current_active_user)):
    db_sub_treatment = SubTreatmentModel(
        name=sub_treatment.name, 
        treatments_picture=sub_treatment.treatments_picture,
        price=sub_treatment.price,
        mrp=sub_treatment.mrp,
        discount=sub_treatment.discount,
        description=sub_treatment.description,
        treatment_time=sub_treatment.treatment_time,
        treatment_id=sub_treatment.treatment_id
    )
    db.add(db_sub_treatment)
    db.commit()
    db.refresh(db_sub_treatment)
    return "success"
    
@router.put("/update_sub_treatments")
def update_sub_treatment(sub_treatment: UpdateSubTreatmentSchema, db: Session = Depends(get_db)):
    db_sub_treatment = db.query(SubTreatmentModel).filter(SubTreatmentModel.id == sub_treatment.id).first()
    if sub_treatment.name: db_sub_treatment.name = sub_treatment.name
    if sub_treatment.treatments_picture: db_sub_treatment.treatments_picture = sub_treatment.treatments_picture
    if sub_treatment.price: db_sub_treatment.price = sub_treatment.price
    if sub_treatment.mrp: db_sub_treatment.mrp = sub_treatment.mrp
    if sub_treatment.discount: db_sub_treatment.discount = sub_treatment.discount
    if sub_treatment.description: db_sub_treatment.description = sub_treatment.description
    if sub_treatment.treatment_time: db_sub_treatment.treatment_time = sub_treatment.treatment_time
    if sub_treatment.treatment_id: db_sub_treatment.treatment_id = sub_treatment.treatment_id
    
    db.add(db_sub_treatment)
    db.commit()
    db.refresh(db_sub_treatment)
    
    return "success"

