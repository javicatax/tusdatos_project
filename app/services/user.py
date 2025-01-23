from sqlalchemy.orm import Session
from ..models.models import User
from ..schemas.user import UserRequest

def create_user(db: Session, user: UserRequest):
    hash_password = User.create_password(user.password)
    db_user = User(
        username=user.username,
        password=hash_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user