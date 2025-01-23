from typing import Optional
from pydantic import BaseModel

from .common import ResponseModel


class AttendeeRequestModel(BaseModel):
    """
    Attendee request model
    """
    name: str

class AttendeeResponseModel(ResponseModel):
    """
    Attendee response model
    """
    name: str
    event_id: Optional[int]

class AttendeeRequestPutModel(BaseModel):
    """
    Attendee request put model
    """
    event_id: int