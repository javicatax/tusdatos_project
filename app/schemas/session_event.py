from pydantic import BaseModel

from app.schemas.speaker import SpeakerResponseModel
from .common import ResponseModel
from datetime import datetime


class SessionRequestModel(BaseModel):
    """
    Session request model
    """
    event_id: int
    nombre: str
    start_date: datetime
    end_date: datetime
    presenter_id: int

class SessionResponseModel(ResponseModel):
    """
    Session response model
    """
    event_id: int
    nombre: str
    start_date: datetime
    end_date: datetime
    presenter_id: SpeakerResponseModel

class SessionRequestPutModel(BaseModel):
    """
    Session request model
    """
    presenter_id: int
