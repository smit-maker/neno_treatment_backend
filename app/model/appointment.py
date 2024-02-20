from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Schema
from app.schema.appointment import AppointmentStatus

# Model
from app.model.treatments import SubTreatmentModel
from app.model.users import UserModel

Base = declarative_base()

# class AppointmentModel(Base):
#     __tablename__ = "appointments"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     sub_treatment_id = Column(Integer, ForeignKey('sub_treatments.id'))
#     appointment_time = Column(DateTime, default=datetime.utcnow)
#     status = Column(String, default=AppointmentStatus.scheduled)

#     # user = relationship('UserModel', back_populates='appointment_list')
#     # sub_treatment = relationship('SubTreatmentModel', back_populates='appointments_list')
