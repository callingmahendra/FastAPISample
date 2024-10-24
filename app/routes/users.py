from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema import UserCreate, UserUpdate
from app.services.users import UserService

router = APIRouter()

@router.get("/users/")
def get_all_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_users()

@router.get("/users/{user_id}")
def get_user_by_user_id(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_user_by_user_id(user_id, db)

@router.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user, db)

@router.put("/users/{user_id}")
def update_user_by_email(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.update_user_by_email(user_id, user, db)

@router.delete("/users/{user_id}")
def delete_user_by_email(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.delete_user_by_email(user_id, db)
