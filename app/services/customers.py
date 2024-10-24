from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Customer
from app.schema import CustomerCreate, CustomerUpdate

class CustomerService:
    def __init__(self, db: Session):
        """
        Initialize the CustomerService with a database session.

        Parameters:
            db (Session): The database session.
        """
        self.db = db

    def get_all_customers(self):
        """
        Retrieve all customers from the database.

        Returns:
            List[Customer]: A list of all customers.
        """
        return self.db.query(Customer).all()

    def get_customer_by_id(self, customer_id: int):
        """
        Retrieve a customer by ID.

        Parameters:
            customer_id (int): The ID of the customer to retrieve.

        Returns:
            Customer: The customer with the specified ID.

        Raises:
            HTTPException: If the customer is not found.
        """
        customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
        if customer:
            return customer
        raise HTTPException(status_code=404, detail="Customer not found")

    def create_customer(self, customer: CustomerCreate):
        """
        Create a new customer in the database.

        Parameters:
            customer (CustomerCreate): The customer data to create.

        Returns:
            Customer: The created customer.
        """
        db_customer = Customer(name=customer.name, email=customer.email, phone=customer.phone, address=customer.address)
        self.db.add(db_customer)
        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer

    def update_customer(self, customer_id: int, customer: CustomerUpdate):
        """
        Update an existing customer in the database.

        Parameters:
            customer_id (int): The ID of the customer to update.
            customer (CustomerUpdate): The updated customer data.

        Returns:
            dict: A message indicating the update status.

        Raises:
            HTTPException: If the customer is not found.
        """
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
        """
        Delete a customer from the database.

        Parameters:
            customer_id (int): The ID of the customer to delete.

        Returns:
            dict: A message indicating the deletion status.

        Raises:
            HTTPException: If the customer is not found.
        """
        db_customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
        if not db_customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        self.db.delete(db_customer)
        self.db.commit()
        return {"message": "Customer deleted successfully"}
