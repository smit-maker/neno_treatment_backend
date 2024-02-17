from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BranchModel(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # Define the back reference for the relationship
    user = relationship('UserModel', back_populates='branch', uselist=False)

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String)
    f_name = Column(String)
    l_name = Column(String)
    password = Column(String, index=True)
    gender = Column(String)
    dob = Column(DateTime)
    profile_picture = Column(String)
    disabled = Column(Boolean, default=False)

    # Define the one-to-one relationship with BranchModel
    branch_id = Column(Integer, ForeignKey('branches.id'))
    branch = relationship('BranchModel', back_populates='user', uselist=False)
