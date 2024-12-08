from pydantic import BaseModel


class UserCreate(BaseModel):
    """
    Schema for creating a new user.

    Attributes:
        name (str): The name of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
    """
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    """
    Schema for updating an existing user.

    Attributes:
        name (str): The name of the user.
        email (str): The email address of the user.
    """
    name: str
    email: str

class CustomerCreate(BaseModel):
    """
    Schema for creating a new customer.

    Attributes:
        name (str): The name of the customer.
        email (str): The email address of the customer.
        phone (str): The phone number of the customer.
        address (str): The address of the customer.
    """
    name: str
    email: str
    phone: str
    address: str

class CustomerUpdate(BaseModel):
    """
    Schema for updating an existing customer.

    Attributes:
        name (str): The name of the customer.
        email (str): The email address of the customer.
        phone (str): The phone number of the customer.
        address (str): The address of the customer.
    """
    name: str
    email: str
    phone: str
    address: str

class EmployeeCreate(BaseModel):
    """
    Schema for creating a new employee.

    Attributes:
        name (str): The name of the employee.
        department (str): The department of the employee.
        gender (str): The gender of the employee.
    """
    name: str
    department: str
    gender: str

class EmployeeUpdate(BaseModel):
    """
    Schema for updating an existing employee.

    Attributes:
        name (str): The name of the employee.
        department (str): The department of the employee.
        gender (str): The gender of the employee.
    """
    name: str
    department: str
    gender: str
