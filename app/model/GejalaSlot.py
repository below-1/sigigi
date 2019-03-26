from sqlalchemy import Column
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import  String
from sqlalchemy import  Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class GejalaSlot(Base):
    __tablename__ = 'gejala_slot'
    id = Column(Integer, primary_key=True)
    gejala_id = Column(Integer, ForeignKey("gejala.id"))
    rule_id = Column(Integer, ForeignKey("rule.id"))
    weight = Column(Float, nullable=False)
    vorder = Column(Integer, nullable=False)

    gejala = relationship("Gejala")
    rule = relationship("Rule", back_populates="slots")

    def as_dict(self):
        return {
            'id': self.id,
            'gejala_id': self.gejala_id,
            'weight': self.weight,
            'vorder': self.vorder
        }

    def __repr__(self):
        return f"GejalaSlot(id={self.id}, gejala={self.gejala_id}, rule={self.rule_id}, weight={self.weight}, vorder={self.vorder})"