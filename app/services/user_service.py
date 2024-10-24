from sqlalchemy.orm import Session
from app.models import User
from app.schema import UserCreate, UserUpdate

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self):
        return self.db.query(User).all()

    def get_user_by_user_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def create_user(self, user: UserCreate):
        db_user = User(name=user.name, email=user.email, password=user.password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user_by_email(self, user_id: int, user: UserUpdate):
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if not db_user:
            return None
        db_user.name = user.name
        db_user.email = user.email
        self.db.commit()
        return db_user

    def delete_user_by_email(self, user_id: int):
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if not db_user:
            return None
        self.db.delete(db_user)
        self.db.commit()
        return db_user
