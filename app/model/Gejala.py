from sqlalchemy import Column
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import  String
from sqlalchemy import  Text
from sqlalchemy.orm import relationship
from .base import Base

class Gejala(Base):
    __tablename__ = 'gejala'
    id = Column(Integer, primary_key=True)
    nama = Column(String(250), nullable=False)
    keterangan = Column(Text)
    deleted = Column(Boolean, default=False, nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'nama': self.nama,
            'keterangan': self.keterangan
        }
