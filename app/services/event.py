from typing import List
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from ..models.models import Event, Attendee
from ..schemas.event import EventRequestPutModel, EventCreate
from app.schemas.attendee import AttendeeRequestModel

def create_event(db: Session, event: EventCreate):
    """
    Create an event
    :param db:
    :param event:
    :return: Event
    """
    try:
        db_event = Event.from_orm(event)
        db.add(db_event)
        db.commit()
        db.refresh(db_event)
        return db_event

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while saving the event: {str(e)}"
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"An unexpected error occurred: {str(e)}"
        )

def add_attendees(db: Session, event_id: int, attendees: List[AttendeeRequestModel]):
    """
    Add attendees
    :param db:
    :param event_id:
    :param attendees:
    :return: Event updated
    """
    try:
        event = db.get(Event, event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")

        if len(attendees) + event.capacity_actual > event.capacity_total:
            raise HTTPException(
                status_code=400,
                detail="Exceeding event capacity"
            )

        for attendee_data in attendees:
            attendee = Attendee(
                name=attendee_data.name,
                event_id=event.id
            )
            db.add(attendee)

        event.capacity_actual += len(attendees)
        db.commit()
        db.refresh(event)
        return event
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while add attendees: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"An unexpected error occurred: {str(e)}"
        )

def update_event(db: Session, event_id: int, event_update: EventRequestPutModel):
    """
    Update an event
    :param db:
    :param event_id:
    :param event_update:
    :return: Event updated
    """
    try:
        # Get event
        event: Event = db.query(Event).filter(Event.id == event_id).first()
        if not event:
            raise HTTPException(status_code=404, detail=f"Event with id {event_id} not found")

        # Update event
        for key, value in event_update.dict(exclude_unset=True).items():
            setattr(event, key, value)

        db.add(event)
        db.commit()
        db.refresh(event)
        return event

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while updating the event: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"An unexpected error occurred: {str(e)}"
        )

def delete_event(db: Session, event_id: int):
    """
    Delete an event
    :param db:
    :param event_id:
    :return: Event deleted
    """
    try:
        # Get event
        event: Event = db.query(Event).filter(Event.id == event_id).first()
        if not event:
            raise HTTPException(status_code=404, detail=f"Event with id {event_id} not found")

        # Delete event
        db.delete(event)
        db.commit()

        return {"message": f"Event with id {event_id} successfully deleted"}

    except SQLAlchemyError as e:
        db.rollback()  # Revertir la transacción en caso de error
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while deleting the event: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"An unexpected error occurred: {str(e)}"
        )