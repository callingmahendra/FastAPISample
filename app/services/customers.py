from http.client import HTTPException
from sqlalchemy.orm import Session
from app.models import Customer
from app.schema import CustomerCreate, CustomerUpdate

class CustomerService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_customers(self):
        return self.db.query(Customer).all()

    def get_customer_by_id(self, customer_id: int):
        customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
        if customer:
            return customer
        raise HTTPException(status_code=404, detail="Customer not found")

    def create_customer(self, customer: CustomerCreate):
        db_customer = Customer(name=customer.name, email=customer.email, phone=customer.phone, address=customer.address)
        self.db.add(db_customer)
        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer

    def update_customer(self, customer_id: int, customer: CustomerUpdate):
        db_customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
        if not db_customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        db_customer.name = customer.name
        db_customer.email = customer.email
        db_customer.phone = customer.phone
        db_customer.address = customer.address
        self.db.commit()
        return {"message": "Customer updated successfully"}

    def delete_customer(self, customer_id: int):
        db_customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
        if not db_customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        self.db.delete(db_customer)
        self.db.commit()
        return {"message": "Customer deleted successfully"}
