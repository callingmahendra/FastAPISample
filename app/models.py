from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.database import engine
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(50), index=True)
    email: str = Column(String(50), unique=True, index=True)
    password: str = Column(String(50))

class Customer(Base):
    __tablename__ = "customers"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(50), index=True)
    email: str = Column(String(50), unique=True, index=True)
    phone: str = Column(String(15))
    address: str = Column(String(100))

Base.metadata.create_all(engine)
