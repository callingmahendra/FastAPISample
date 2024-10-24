from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema import UserCreate, UserUpdate
from app.services.users import UserService

router = APIRouter()

@router.get("/users/")
def get_all_users(db: Session = Depends(get_db)):
    """
    Retrieve all users.

    This endpoint retrieves all users from the database.

    Parameters:
        db (Session): The database session.

    Returns:
        List[User]: A list of all users.
    """
    service = UserService(db)
    return service.get_all_users()

@router.get("/users/{user_id}")
def get_user_by_user_id(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a user by ID.

    This endpoint retrieves a user from the database by their ID.

    Parameters:
        user_id (int): The ID of the user to retrieve.
        db (Session): The database session.

    Returns:
        User: The user with the specified ID.
    """
    service = UserService(db)
    return service.get_user_by_user_id(user_id)

@router.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.

    This endpoint creates a new user in the database.

    Parameters:
        user (UserCreate): The user data to create.
        db (Session): The database session.

    Returns:
        User: The created user.
    """
    service = UserService(db)
    return service.create_user(user)

@router.put("/users/{user_id}")
def update_user_by_email(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    """
    Update a user.

    This endpoint updates an existing user in the database.

    Parameters:
        user_id (int): The ID of the user to update.
        user (UserUpdate): The updated user data.
        db (Session): The database session.

    Returns:
        dict: A message indicating the update status.
    """
    service = UserService(db)
    return service.update_user_by_email(user_id, user)

@router.delete("/users/{user_id}")
def delete_user_by_email(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user.

    This endpoint deletes a user from the database.

    Parameters:
        user_id (int): The ID of the user to delete.
        db (Session): The database session.

    Returns:
        dict: A message indicating the deletion status.
    """
    service = UserService(db)
    return service.delete_user_by_email(user_id)
