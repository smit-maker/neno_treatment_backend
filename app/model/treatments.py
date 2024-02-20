from datetime import datetime
from app.schema.appointment import AppointmentStatus
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class TreatmentModel(Base):
#     __tablename__ = "treatments"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)
#     treatments_picture = Column(String)

#     # Define the back reference for the relationship
#     sub_treatment = relationship('SubTreatmentModel', back_populates='treatment')

# class SubTreatmentModel(Base):
#     __tablename__ = "sub_treatments"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)
#     treatments_picture = Column(String)
#     price = Column(Float)
#     mrp = Column(Float)
#     discount = Column(Float)
#     description = Column(String)
#     treatment_time = Column(String)
#     treatment_id = Column(Integer, ForeignKey('treatments.id'))

#     treatment = relationship('TreatmentModel', back_populates='sub_treatment', uselist=False)
#     # appointments_list = relationship('AppointmentModel', back_populates='sub_treatment', uselist=False)


# class AppointmentModel(Base):
#     __tablename__ = "appointments"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     sub_treatment_id = Column(Integer, ForeignKey('sub_treatments.id'))
#     appointment_time = Column(DateTime, default=datetime.utcnow)
#     status = Column(String, default=AppointmentStatus.scheduled)

#     # user = relationship('UserModel', back_populates='appointment_list')
#     # sub_treatment = relationship('SubTreatmentModel', back_populates='appointments_list')
