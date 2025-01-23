from typing import List
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.models import SessionEvent
from ..schemas.session_event import SessionRequestModel
from app.schemas.attendee import AttendeeRequestModel

def create_session_event(db: Session, session_event: SessionRequestModel):
    """
    Creates a session event
    :param db:
    :param session_event:
    :return: SessionEvent
    """
    try:
        db_event = Session.from_orm(Session)
        db.add(db_event)
        db.commit()
        db.refresh(db_event)
        return db_event

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while saving the session event: {str(e)}"
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"An unexpected error occurred: {str(e)}"
        )