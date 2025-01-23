from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi import HTTPException

from ..schemas.session_event import SessionRequestModel, SessionResponseModel
from app.models.models import SessionEvent
from ..database import get_db
from ..services.session_event import create_session_event

router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.post("", response_model=SessionResponseModel)
async def create_session_event_endpoint(session_event: SessionRequestModel, db: Session = Depends(get_db)):
    """
    Creates a new session event
    :param session_event:
    :param db:
    :return: Session event
    """
    db_event = db.query(SessionEvent).filter(SessionEvent.name == session_event.name).first()
    if db_event:
        raise HTTPException(status_code=400, detail="Session event name already registered")
    return create_session_event(db, session_event)

@router.get("/{session_event_id}", response_model=SessionResponseModel)
def get_event(session_event_id: int, db: Session = Depends(get_db)):
    """
    Get a session event.
    :param session_event_id:
    :param db:
    :return: Session event
    """
    event = db.get(SessionEvent, session_event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Session event not found")
    return event
