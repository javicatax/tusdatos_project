import pytest
from sqlmodel import create_engine, SQLModel, Session
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db

# URL de la base de datos de pruebas
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/mis_eventos_db"
engine = create_engine(DATABASE_URL)

# Crear y eliminar tablas para pruebas
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)

# Fixture de la sesión de base de datos
@pytest.fixture
def session():
    with Session(engine) as session:
        yield session

# Fixture del cliente de pruebas
@pytest.fixture
def client(session):
    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()
