from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from config.database import Base

class Password(Base):
    __tablename__ = "keychain"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    title = Column(String, index=True)
    URL = Column(String, nullable=True)
    password = Column(Text, nullable=False)
    unlock = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    # relacion con el modelo User
    user = relationship("User", back_populates="passwords")