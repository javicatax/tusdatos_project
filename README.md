# Proyecto Tusdatos FastAPI

Este es un proyecto backend que permita administrar de manera eficiente todo el
ciclo de vida de un evento, desde su creación y configuración hasta la gestión de
asistentes, demostrando conocimientos en FastAPI, SQLAlchemy,
Elasticsearch y Docker.

---

## **Instalación**

### **Requisitos previos**
- Python 3.12
- PostgreSQL instalado y configurado

### **Pasos**
1. Clona este repositorio:
   ```bash
   git clone https://github.com/usuario/proyecto-eventos.git
   cd proyecto-eventos
   
2. Crea un entorno virtual e instala dependencias:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Crea un archivo .env con las variables de entorno:
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/database_name
SECRET_KEY=tu_secreto
```

5. Ejecuta las migraciones de la base de datos:
```bash
alembic upgrade head
```
 
5. Inicia el servidor:
```bash
uvicorn app.main:app --reload
```


## **Características**

- CRUD de Eventos: Crear, leer, actualizar y eliminar eventos.
- Autenticación: Uso de JWT para proteger endpoints.
- Relaciones: Relaciones 1 a muchos y muchos a muchos gestionadas con SQLAlchemy y SQLModel.

## **Uso**

Documentación de la API
Accede a la documentación interactiva en:

Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc

## **Pruebas**

Cobertura de pruebas
Ejecuta los tests unitarios y genera un reporte de cobertura:

coverage run -m pytest
coverage report

## **Licencia**

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.




