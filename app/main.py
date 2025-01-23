from fastapi import FastAPI
from fastapi import APIRouter
import json
from app.core.config import settings
from .database import SessionLocal, create_db, engine
from .routers import auth_router
from .routers import users_router
from .routers import events_router
from .routers import sessions_router

# Create instance FastAPI
app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

# Create API router
api_v1 = APIRouter(prefix="/api/v1")

# include API routers
api_v1.include_router(auth_router)
api_v1.include_router(users_router)
api_v1.include_router(events_router)
api_v1.include_router(sessions_router)

app.include_router(api_v1)

@app.on_event('startup')
def startup():
    create_db()  # Create tables

@app.on_event("shutdown")
async def shutdown_event():
    print("closing db")
    engine.dispose()  # Close connection

@app.get("/")
async def index():
    return {"message": "Index page"}