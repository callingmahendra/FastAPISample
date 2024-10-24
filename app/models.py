from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.database import engine

Base = declarative_base()

class User(Base):
    """
    Represents a user in the system.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
    """
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(50), index=True)
    email: str = Column(String(50), unique=True, index=True)
    password: str = Column(String(50))

class Customer(Base):
    """
    Represents a customer in the system.

    Attributes:
        id (int): The unique identifier for the customer.
        name (str): The name of the customer.
        email (str): The email address of the customer.
        phone (str): The phone number of the customer.
        address (str): The address of the customer.
    """
    __tablename__ = "customers"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(50), index=True)
    email: str = Column(String(50), unique=True, index=True)
    phone: str = Column(String(15))
    address: str = Column(String(100))

Base.metadata.create_all(engine)
