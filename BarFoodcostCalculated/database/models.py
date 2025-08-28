from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AlcoInfo(Base):
    __tablename__ = 'Alcohol_info'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    volume = Column(Integer)
    price = Column(Integer)

