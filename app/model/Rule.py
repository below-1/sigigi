from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Rule(Base):
    __tablename__ = "rule"
    id = Column(Integer, primary_key=True)
    penyakit_id = Column(Integer, ForeignKey("penyakit.id"))

    penyakit = relationship("Penyakit", back_populates="rules")
    slots = relationship("GejalaSlot", back_populates="rule", cascade="all, delete, delete-orphan")

    def as_dict(self):
        return {
            'id': self.id,
            'penyakit_id': self.penyakit_id
        }