from wsgiref.validate import validator
from pydantic import BaseModel, Field
from sqlmodel import SQLModel

from .common import ResponseModel

# -- user --

class UserRequest(BaseModel):
    """
    User request model
    """
    username: str = Field(..., description="Username")
    password: str = Field(..., description="Password")
    # @validator('username')
    # def username_validator(self, username):
    #     if len(username) < 3 or len(username) > 50:
    #         raise ValueError('Username must be between 3 and 50 characters')
    #     return username

class UserResponse(ResponseModel):
    """
    User response model
    """
    username: str = Field(..., description="Username")
    password: str = Field(..., description="Password")