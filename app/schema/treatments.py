from datetime import date
from pydantic import BaseModel
from typing import List, Optional


# Sub Treatments
class CreateSubTreatmentSchema(BaseModel):
    name: str | None = None
    treatments_picture: str | None = None
    price: float | None = None
    mrp: float | None = None
    discount: float | None = None
    description: str | None = None
    treatment_time: date | None = None
    treatment_id: int | None = None

class UpdateSubTreatmentSchema(CreateSubTreatmentSchema):
    id: int | None = None

class SubTreatmentSchema(BaseModel):
    id: int
    name: str
    treatments_picture: Optional[str]
    price: float
    mrp: float
    discount: float
    description: str
    treatment_time: str

    # class Config:
    #     from_attributes = True

# Treatments
class CreateTreatmentSchema(BaseModel):
    name: str | None = None
    treatments_picture: str | None = None

class UpdateTreatmentSchema(CreateTreatmentSchema):
    id: int | None = None

class TreatmentSchema(BaseModel):
    id: int
    name: str
    treatments_picture: Optional[str]
    sub_treatment: Optional[List[SubTreatmentSchema]]
    
    class Config:
        from_attributes = True