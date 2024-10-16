from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    name: str
    email: str

class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class CustomerUpdate(BaseModel):
    name: str
    email: str
    phone: str
    address: str
