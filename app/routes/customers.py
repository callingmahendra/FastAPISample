from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema import CustomerCreate, CustomerUpdate
from app.services.customers import CustomerService

router = APIRouter()

@router.get("/customers/")
def get_all_customers(db: Session = Depends(get_db)):
    """
    Retrieve all customers.

    This endpoint retrieves all customers from the database.

    Parameters:
        db (Session): The database session.

    Returns:
        List[Customer]: A list of all customers.
    """
    service = CustomerService(db)
    return service.get_all_customers()

@router.get("/customers/{customer_id}")
def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a customer by ID.

    This endpoint retrieves a customer from the database by their ID.

    Parameters:
        customer_id (int): The ID of the customer to retrieve.
        db (Session): The database session.

    Returns:
        Customer: The customer with the specified ID.
    """
    service = CustomerService(db)
    return service.get_customer_by_id(customer_id)

@router.post("/customers/")
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    """
    Create a new customer.

    This endpoint creates a new customer in the database.

    Parameters:
        customer (CustomerCreate): The customer data to create.
        db (Session): The database session.

    Returns:
        Customer: The created customer.
    """
    service = CustomerService(db)
    return service.create_customer(customer)

@router.put("/customers/{customer_id}")
def update_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    """
    Update a customer.

    This endpoint updates an existing customer in the database.

    Parameters:
        customer_id (int): The ID of the customer to update.
        customer (CustomerUpdate): The updated customer data.
        db (Session): The database session.

    Returns:
        dict: A message indicating the update status.
    """
    service = CustomerService(db)
    return service.update_customer(customer_id, customer)

@router.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    """
    Delete a customer.

    This endpoint deletes a customer from the database.

    Parameters:
        customer_id (int): The ID of the customer to delete.
        db (Session): The database session.

    Returns:
        dict: A message indicating the deletion status.
    """
    service = CustomerService(db)
    return service.delete_customer(customer_id)
