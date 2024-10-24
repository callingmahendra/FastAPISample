from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema import CustomerCreate, CustomerUpdate
from app.services.customers import CustomerService

router = APIRouter()

@router.get("/customers/")
def get_all_customers(db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.get_all_customers()

@router.get("/customers/{customer_id}")
def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.get_customer_by_id(customer_id)

@router.post("/customers/")
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.create_customer(customer)

@router.put("/customers/{customer_id}")
def update_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.update_customer(customer_id, customer)

@router.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.delete_customer(customer_id)
