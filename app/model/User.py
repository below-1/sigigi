from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import  String
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=True)
    nama = Column(String(250), nullable=True)
    alamat = Column(String(250), nullable=True)
    umur = Column(Integer, nullable=True)
    jk = Column(Boolean, nullable=True)
    password = Column(String(250), nullable=True)
    role = Column(String(250), nullable=True)
    records = relationship("MedicRecord", back_populates="user")

    def as_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'nama': self.nama
        }