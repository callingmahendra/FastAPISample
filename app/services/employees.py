from http.client import HTTPException
from sqlalchemy.orm import Session
from app.models import Employee
from app.schema import EmployeeCreate, EmployeeUpdate

class EmployeeService:
    def __init__(self, db: Session):
        """
        Initialize the EmployeeService with a database session.

        Parameters:
            db (Session): The database session.
        """
        self.db = db

    def get_all_employees(self):
        """
        Retrieve all employees from the database.

        Returns:
            List[Employee]: A list of all employees.
        """
        return self.db.query(Employee).all()

    def get_employee_by_id(self, employee_id: int):
        """
        Retrieve an employee by ID.

        Parameters:
            employee_id (int): The ID of the employee to retrieve.

        Returns:
            Employee: The employee with the specified ID.

        Raises:
            HTTPException: If the employee is not found.
        """
        employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        if employee:
            return employee
        raise HTTPException(status_code=404, detail="Employee not found")

    def create_employee(self, employee: EmployeeCreate):
        """
        Create a new employee in the database.

        Parameters:
            employee (EmployeeCreate): The employee data to create.

        Returns:
            Employee: The created employee.
        """
        db_employee = Employee(name=employee.name, department=employee.department, gender=employee.gender)
        self.db.add(db_employee)
        self.db.commit()
        self.db.refresh(db_employee)
        return db_employee

    def update_employee(self, employee_id: int, employee: EmployeeUpdate):
        """
        Update an existing employee in the database.

        Parameters:
            employee_id (int): The ID of the employee to update.
            employee (EmployeeUpdate): The updated employee data.

        Returns:
            dict: A message indicating the update status.

        Raises:
            HTTPException: If the employee is not found.
        """
        db_employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        if not db_employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        db_employee.name = employee.name
        db_employee.department = employee.department
        db_employee.gender = employee.gender
        self.db.commit()
        return {"message": "Employee updated successfully"}

    def delete_employee(self, employee_id: int):
        """
        Delete an employee from the database.

        Parameters:
            employee_id (int): The ID of the employee to delete.

        Returns:
            dict: A message indicating the deletion status.

        Raises:
            HTTPException: If the employee is not found.
        """
        db_employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        if not db_employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        self.db.delete(db_employee)
        self.db.commit()
        return {"message": "Employee deleted successfully"}
