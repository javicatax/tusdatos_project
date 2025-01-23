import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load file .env
load_dotenv()

class Settings(BaseSettings):
    """
    Define global settings
    """
    # Access environment variables
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    PROJECT_VERSION: str = os.getenv("PROJECT_VERSION")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    URL_USER_GET_TOKEN: str = '/api/v1/users/login'

settings = Settings()