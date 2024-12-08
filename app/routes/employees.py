from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema import EmployeeCreate, EmployeeUpdate
from app.services.employees import EmployeeService

router = APIRouter()

@router.get("/employees/")
def get_all_employees(db: Session = Depends(get_db)):
    """
    Retrieve all employees.

    This endpoint retrieves all employees from the database.

    Parameters:
        db (Session): The database session.

    Returns:
        List[Employee]: A list of all employees.
    """
    service = EmployeeService(db)
    return service.get_all_employees()

@router.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: int, db: Session = Depends(get_db)):
    """
    Retrieve an employee by ID.

    This endpoint retrieves an employee from the database by their ID.

    Parameters:
        employee_id (int): The ID of the employee to retrieve.
        db (Session): The database session.

    Returns:
        Employee: The employee with the specified ID.
    """
    service = EmployeeService(db)
    return service.get_employee_by_id(employee_id)

@router.post("/employees/")
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """
    Create a new employee.

    This endpoint creates a new employee in the database.

    Parameters:
        employee (EmployeeCreate): The employee data to create.
        db (Session): The database session.

    Returns:
        Employee: The created employee.
    """
    service = EmployeeService(db)
    return service.create_employee(employee)

@router.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    """
    Update an employee.

    This endpoint updates an existing employee in the database.

    Parameters:
        employee_id (int): The ID of the employee to update.
        employee (EmployeeUpdate): The updated employee data.
        db (Session): The database session.

    Returns:
        dict: A message indicating the update status.
    """
    service = EmployeeService(db)
    return service.update_employee(employee_id, employee)

@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    """
    Delete an employee.

    This endpoint deletes an employee from the database.

    Parameters:
        employee_id (int): The ID of the employee to delete.
        db (Session): The database session.

    Returns:
        dict: A message indicating the deletion status.
    """
    service = EmployeeService(db)
    return service.delete_employee(employee_id)
