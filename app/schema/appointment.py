from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class AppointmentStatus(str, Enum):
    scheduled = "Scheduled"
    pending = "Pending"
    confirmed = "Confirmed"
    cancelled = "Cancelled"

class CreateAppointmentSchema(BaseModel):
    user_id: int
    sub_treatment_id: int
    appointment_time: datetime
    status: AppointmentStatus
    
class UpdateAppointmentSchema(BaseModel):
    id: int
    user_id: int
    sub_treatment_id: int
    appointment_time: datetime
    status: AppointmentStatus

class AppointmentSchema(BaseModel):
    id: int
    user_id: int
    sub_treatment_id: int
    appointment_time: datetime
    status: AppointmentStatus
