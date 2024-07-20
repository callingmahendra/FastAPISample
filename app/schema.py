from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    name: str
    email: str
class DepartmentCreate(BaseModel):
    name: str

class DepartmentUpdate(BaseModel):
    name: str
