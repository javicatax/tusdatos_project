from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi import status

from ..models.models import User
from ..schemas.user import UserRequest

def verify_password(user_password: str, credential_password: str):
    if user_password != User.create_password(credential_password):
        return False
    return True

def authenticate_user(db: Session, username: str, user_password: str, credential_password: str):
    user = db.query(User).filter(User.username == username).first()
    if user is None or not verify_password(user_password=user.password, credential_password=credential_password, ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user