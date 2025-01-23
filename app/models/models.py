import hashlib

from sqlalchemy.dialects.mysql import DATETIME
from sqlmodel import Field, Relationship
from sqlalchemy.orm import relationship, sessionmaker
from typing import List, Optional
from datetime import datetime
from sqlmodel import SQLModel
from enum import Enum
from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime

Base = SQLModel.metadata

class EventStatus(str, Enum):
    """
    Event status enum options
    """
    planned = "planned"
    ongoing = "ongoing"
    completed = "completed"
    cancelled = "cancelled"

class User(SQLModel, table=True):
    """
    Represents a user in the database.
    """
    id: int = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, max_length=60)
    password: str = Field(index=True, unique=True, max_length=60)
    created_at: datetime = Field(default=func.now(), sa_column=Column(DateTime, default=func.now()))
    # datetime = Field(DATETIME, default=datetime.now)

    def __str__(self):
        return self.username

    @classmethod
    def authenticate(cls, username, password):
        user = cls.select().where(cls.username == username).first()

        if user and user.password == cls.create_password(password):
            return user

    @classmethod
    def create_password(cls, password):
        h = hashlib.md5()
        h.update(password.encode('utf-8'))
        return h.hexdigest()

class Event(SQLModel, table=True):
    """
    Represents an event in the database.
    """
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True, max_length=80)
    description: Optional[str] = Field(default=None)
    start_date: datetime
    end_date: datetime
    capacity_total: int
    capacity_actual: int = 0
    status: EventStatus = Field(default=EventStatus.planned, index=True)  # Status
    attendees: Optional[list["Attendee"]] = Relationship(back_populates="event")
    # attendees: list["Attendee"] = relationship("Attendee", back_populates="event")
    # attendees: List["Attendee"] = Relationship(back_populates="event")
    owner: Optional[int] = Field(default=None, foreign_key="user.id")

    def __str__(self) -> str:
        return self.name

    def add_attendee(self, quantity: int):
        if self.capacity_actual + quantity <= self.capacity_total:
            self.capacity_actual += quantity
        else:
            raise ValueError("maximum capacity achieved")

    def delete_attendee(self, quantity: int):
        if self.capacity_actual - quantity >= 0:
            self.capacity_actual -= quantity
        else:
            raise ValueError("It is not possible to delete attendees")

class SessionEvent(SQLModel, table=True):
    """
    Represents a session event in the database.
    """
    id: int = Field(default=None, primary_key=True)
    event_id: int = Field(foreign_key="event.id")
    name: str = Field(index=True, unique=True, max_length=80)
    start_date: datetime
    end_date: datetime
    speaker_id: Optional[int] = Field(default=None, foreign_key="speaker.id")
    speaker: Optional["Speaker"] = Relationship(back_populates="sessions_event")

    def __str__(self) -> str:
        return self.name

    def schedule_is_valid(self):
        return self.start_date < self.end_date

class Speaker(SQLModel, table=True):
    """
    Represents a speaker in the database.
    """
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True, max_length=80)
    biography: Optional[str] = None
    sessions_event: Optional[list["SessionEvent"]]= Relationship(back_populates="speaker")
    #sessions_event: list["SessionEvent"] = relationship("SessionEvent", back_populates="speaker")

    def __str__(self) -> str:
        return self.name

class Attendee(SQLModel, table=True):
    """
    Represents an attendee in the database.
    """
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True, max_length=80)
    event_id: Optional[int] = Field(default=None, foreign_key="event.id")
    # event: Event = relationship("Event", back_populates="attendee")
    event: Event = Relationship(back_populates="attendees")

    def __str__(self) -> str:
        return self.name
