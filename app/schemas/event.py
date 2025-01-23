from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from app.schemas.attendee import AttendeeResponseModel
from .common import ResponseModel

class EventValidator():

    pass
    # @validator('score')
    # def score_validator(cls, score):
    #     if score < 1 or score > 5:
    #         raise ValueError('score must be between 1 and 5')
    #     return score

class EventStatus(str, Enum):
    planned = "planned"
    ongoing = "ongoing"
    completed = "completed"
    cancelled = "cancelled"

class EventResponseModel(ResponseModel):
    """
    Event response schema
    """
    name: str = Field(..., description="Event name")
    description: str = Field(..., description="Event description")
    start_date: datetime
    end_date: datetime
    capacity_total: int = Field(..., description="Event capacity available")
    capacity_actual: int = Field(..., description="Event capacity available")
    status: EventStatus
    attendees: Optional[List["AttendeeResponseModel"]]

class EventRequestPutModel(BaseModel, EventValidator):
    """
    Event request schema
    """
    description: str = Field(..., description="Event description")
    capacity_total: int
    status: str = Field(..., description="Event status")

class EventCreate(BaseModel):
    """
    Event create schema
    """
    name: str = Field(..., description="Event name")
    description: Optional[str] = None
    start_date: datetime = Field(..., description="Event start date")
    end_date: datetime = Field(..., description="Event end date")
    capacity_total: int = Field(..., description="Event capacity available")
    capacity_actual: int = Field(..., description="Event capacity available")
    status: EventStatus = EventStatus.planned

    class Config:
        orm_mode = True
