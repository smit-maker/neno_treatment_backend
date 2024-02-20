from datetime import date
from typing import List
from pydantic import BaseModel

from app.schema.appointment import AppointmentSchema

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

# Branch Schema
class BranchSchema(BaseModel):
    id: int | None = None
    name: str | None = None

    # class Config:
    #     from_attributes = True

class CreateBranchSchema(BaseModel):
    name: str | None = None

class UpdateBranchSchema(BaseModel):
    id: int | None = None
    name: str | None = None

# User Schema
class CurrentUser(BaseModel):
    id: int | None = None
    username: str | None = None
    email: str | None = None
    f_name: str | None = None
    l_name: str | None = None
    # password: str | None = None
    gender: str | None = None
    dob: date | None = None
    profile_picture: str | None = None
    # disabled: bool | None = None
    # branch_id: int | None = None
    branch: CreateBranchSchema | None = None
    # appointment_list: List[Appointment] | None = None

class CreateUserSchema(BaseModel):
    username: str | None = None
    email: str | None = None
    f_name: str | None = None
    l_name: str | None = None
    password: str | None = None
    gender: str | None = None
    dob: str | None = None
    profile_picture: str | None = None
    disabled: bool | None = None
    branch_id: int | None = None

class UpdateUserSchema(BaseModel):
    id: int | None = None
    username: str | None = None
    email: str | None = None
    f_name: str | None = None
    l_name: str | None = None
    password: str | None = None
    gender: str | None = None
    dob: date | None = None
    profile_picture: str | None = None
    disabled: bool | None = None
    branch_id: int | None = None
