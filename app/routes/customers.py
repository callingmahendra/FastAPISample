from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema import CustomerCreate, CustomerUpdate
from app.services.customer_service import CustomerService

router = APIRouter()

@router.get("/customers/")
def get_all_customers(db: Session = Depends(get_db)):
    customer_service = CustomerService(db)
    return customer_service.get_all_customers()

@router.get("/customers/{customer_id}")
def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    customer_service = CustomerService(db)
    customer = customer_service.get_customer_by_id(customer_id)
    if customer:
        return customer
    raise HTTPException(status_code=404, detail="Customer not found")

@router.post("/customers/")
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    customer_service = CustomerService(db)
    db_customer = customer_service.create_customer(customer)
    return db_customer

@router.put("/customers/{customer_id}")
def update_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    customer_service = CustomerService(db)
    db_customer = customer_service.update_customer(customer_id, customer)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer updated successfully"}

@router.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer_service = CustomerService(db)
    db_customer = customer_service.delete_customer(customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer deleted successfully"}
