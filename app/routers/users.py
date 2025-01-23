from fastapi import status
from fastapi import APIRouter, Depends
from fastapi import HTTPException
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.orm import Session
from ..models.models import User
from ..schemas.user import UserRequest, UserResponse
from ..database import get_session, get_db
from ..services.auth import authenticate_user
from ..services.user import create_user
from ..common import create_access_token

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/users", response_model=UserResponse)
async def create_user_endpoint(user: UserRequest, db: Session = Depends(get_db)):
    """
    Create a new user
    :param user:
    :param db:
    :return: User response
    """
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db, user)

@router.post("/login", response_model=dict)
async def login(credentials: HTTPBasicCredentials = HTTPBasicCredentials, db: Session = Depends(get_db)):
    """
    Login a user
    :param credentials:
    :param db:
    :return: access token
    """
    user = db.query(User).filter(User.username == credentials.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Username not found")

    user = authenticate_user(db=db, username=user.username, user_password=user.password, credential_password=credentials.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    return {
        'access_token': create_access_token(user),
        'token_type': 'bearer',
    }