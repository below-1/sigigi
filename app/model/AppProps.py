from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import  String
from sqlalchemy import JSON
from .base import Base

class AppProps(Base):
    __tablename__ = 'app_props'
    id = Column(Integer, primary_key=True)
    nama = Column(String(250), nullable=False)
    value = Column(JSON)

    def as_dict(self):
        return {
            'id': self.id,
            'value': self.value
        }
