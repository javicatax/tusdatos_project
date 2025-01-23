import jwt

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime
from datetime import timedelta
from http.client import HTTPException

from app.core.config import settings
from .models.models import User

# Define oauth schema
oauth2_schema = OAuth2PasswordBearer(tokenUrl=settings.URL_USER_GET_TOKEN)

def create_access_token(user, minutes=60):
    """
    Function to create access token
    :param user:
    :param minutes:
    :return: jwt token
    """
    data = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(minutes=minutes),
    }
    return jwt.encode(data, settings.SECRET_KEY, algorithm='HS256')

def decode_token(token):
    """
    Function to decode access token
    :param token:
    :return: jwt token decoded
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException("Token Expired")
    except jwt.InvalidTokenError:
        raise HTTPException("Token Invalid")
    except jwt.DecodeError:
        raise HTTPException("Token Decode error")

def get_current_user(token: str = Depends(oauth2_schema)) -> User:
    """
    Function to get current user
    :param token:
    :return: User
    """
    decoded_token = decode_token(token)
    if not decoded_token:
        raise HTTPException("Token Invalid")
    return User.select().where(User.id == decoded_token['user_id']).first()