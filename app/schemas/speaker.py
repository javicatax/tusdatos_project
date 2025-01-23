from typing import Optional, List

from pydantic import BaseModel
from .common import ResponseModel


class SpeakerRequestModel(BaseModel):
    """
    Speaker request model
    """
    nombre: str
    biography: Optional[str]
    sessions: List[str]

class SpeakerResponseModel(ResponseModel):
    """
    Speaker response model
    """
    nombre: str
    biography: Optional[str]
    sessions: List[str]

class SpeakerRequestPutModel(BaseModel):
    """
    Speaker request PUT model
    """
    biography: str