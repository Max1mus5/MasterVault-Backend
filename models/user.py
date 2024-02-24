from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.password import Password
from config.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    passwords = relationship("Password", back_populates="user")