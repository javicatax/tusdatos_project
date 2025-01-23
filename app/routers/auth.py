from fastapi import Depends, HTTPException
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import status

from app.models.models import User
from ..common import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/auth")
async def auth(data: OAuth2PasswordRequestForm = Depends()):
    """
    Function to authenticate the user
    :param data:
    :return: access token
    """
    user = User.authenticate(data.username, data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    return {
        'access_token': create_access_token(user),
        'token_type': 'bearer',
    }