from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import  String
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    nama = Column(String(250), nullable=True)
    password = Column(String(250), nullable=False)
    role = Column(String(250), nullable=False)
    records = relationship("MedicRecord", back_populates="user")