from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import  Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from .base import Base
import json

class MedicRecord(Base):
    __tablename__ = 'medic_record'
    id = Column(Integer, primary_key=True)
    waktu = Column(DateTime)
    keterangan = Column(Text)
    meta = Column(Text)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="records")
    list_gejala = relationship("GejalaMedicRecord", back_populates="medic_record", cascade="all, delete, delete-orphan")

    @hybrid_property
    def meta_dict(self):
        if (isinstance(self.meta, str)):
            return json.loads(self.meta)
        return self.meta

    def as_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'waktu': self.waktu.isoformat(),
            'meta': self.meta
        }