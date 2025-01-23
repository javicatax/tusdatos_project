from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# URL de conexión a PostgreSQL
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/mis_eventos_db"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

def test_db_connection():
    try:
        # Intenta conectar a la base de datos
        with engine.connect() as connection:
            print("Conexión exitosa a la base de datos.")
        return True
    except SQLAlchemyError as e:
        print(f"Error de conexión: {e}")
        return False

if __name__ == "__main__":
    test_db_connection()
