from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import User
from app.schema import UserCreate, UserUpdate

class UserService:
    def __init__(self, db: Session):
        """
        Initialize the UserService with a database session.

        Parameters:
            db (Session): The database session.
        """
        self.db = db
        
    def get_all_users(self):
        """
        Retrieve all users from the database.

        Returns:
            List[User]: A list of all users.
        """
        return self.db.query(User).all()

    
    def get_user_by_user_id(self,user_id: int):
        """
        Retrieve a user by ID.

        Parameters:
            user_id (int): The ID of the user to retrieve.

        Returns:
            User: The user with the specified ID.

        Raises:
            HTTPException: If the user is not found.
        """
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            return user
        raise HTTPException(status_code=404, detail="User not found")

    
    def create_user(self, user: UserCreate):
        """
        Create a new user in the database.

        Parameters:
            user (UserCreate): The user data to create.

        Returns:
            User: The created user.
        """
        db_user = User(name=user.name, email=user.email, password=user.password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    
    def update_user_by_email(self, user_id: int, user: UserUpdate):
        """
        Update an existing user in the database.

        Parameters:
            user_id (int): The ID of the user to update.
            user (UserUpdate): The updated user data.

        Returns:
            dict: A message indicating the update status.

        Raises:
            HTTPException: If the user is not found.
        """
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        db_user.name = user.name
        db_user.email = user.email
        self.db.commit()
        return {"message": "User updated successfully"}

    
    def delete_user_by_email(self,user_id: int):
        """
        Delete a user from the database.

        Parameters:
            user_id (int): The ID of the user to delete.

        Returns:
            dict: A message indicating the deletion status.

        Raises:
            HTTPException: If the user is not found.
        """
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        self.db.delete(db_user)
        self.db.commit()
        return {"message": "User deleted successfully"}
