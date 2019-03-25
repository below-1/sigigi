from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import  String
from sqlalchemy import  Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class MedicRecord(Base):
    __tablename__ = 'medic_record'
    id = Column(Integer, primary_key=True)
    waktu = Column(DateTime)
    keterangan = Column(Text)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="records")
