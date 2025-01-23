from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi import HTTPException

from ..schemas.attendee import AttendeeRequestModel
from ..schemas.event import EventCreate, EventResponseModel, EventRequestPutModel
from app.models.models import Event, Attendee
from ..database import get_db
from ..services.event import create_event, update_event, delete_event, add_attendees

router = APIRouter(prefix="/events", tags=["events"])

@router.post("", response_model=EventResponseModel)
async def create_event_endpoint(event: EventCreate, db: Session = Depends(get_db)):
    """
    Create an event endpoint.
    :param event:
    :param db:
    :return: Event created
    """
    db_event = db.query(Event).filter(Event.name == event.name).first()
    if db_event:
        raise HTTPException(status_code=400, detail="Event name already registered")
    return create_event(db, event)

@router.post("/{event_id}/attendees/", response_model=EventResponseModel)
def add_attendees_endpoint(event_id: int, attendees: List[AttendeeRequestModel], db: Session = Depends(get_db)):
    """
    Add attendees endpoint.
    :param event_id:
    :param attendees:
    :param db:
    :return: Event updated
    """
    return add_attendees(db, event_id, attendees)

@router.get("", response_model=List[EventResponseModel])
def get_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get all events
    :param db:
    :return: List of events
    """
    # Get all events
    events = db.query(Event).offset(skip).limit(limit).all()
    if not events:
        raise HTTPException(status_code=404, detail="No events found")

    return [event for event in events]

@router.get("/{event_id}", response_model=EventResponseModel)
def get_event(event_id: int, db: Session = Depends(get_db)):
    """
    Get an event.
    :param event_id:
    :param db:
    :return: Event
    """
    event = db.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/{event_id}", response_model=EventResponseModel)
async def update_event_endpoint(event_id: int, event_update: EventRequestPutModel, db: Session = Depends(get_db)):
    """
    Update an event.
    :param event_id:
    :param event_update:
    :param db:
    :return: Event updated
    """
    return update_event(db, event_id, event_update)

@router.delete("/{event_id}", response_model=dict)
async def delete_event_endpoint(event_id: int, db: Session = Depends(get_db)):
    """
    Delete an event.
    :param event_id:
    :param db:
    :return: Deleted event
    """
    return delete_event(db, event_id)