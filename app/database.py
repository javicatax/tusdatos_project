from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from sqlmodel import SQLModel, Session

# URI PostgreSQL connection
DATABASE_URL = settings.DATABASE_URL

# DB engine
engine = create_engine(DATABASE_URL)

# Create Base
Base = declarative_base()

# Sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Get db function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create session
def get_session():
    """
    Creates a new database session

    Yields:
        Session: Session of Data base.
    """
    with Session(engine) as session:
        yield session

# Create tables
def create_db():
    SQLModel.metadata.create_all(bind=engine)

# Base de SQLModel
def init_db():
    SQLModel.metadata.create_all(bind=engine)