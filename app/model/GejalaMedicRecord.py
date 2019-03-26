from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class GejalaMedicRecord(Base):
    __tablename__ = 'gejala_medic_record'
    id = Column(Integer, primary_key=True)
    gejala_id = Column(Integer, ForeignKey("gejala.id"))
    medic_record_id = Column(Integer, ForeignKey("medic_record.id"))

    gejala = relationship("Gejala")
    medic_record = relationship("MedicRecord", back_populates="list_gejala")