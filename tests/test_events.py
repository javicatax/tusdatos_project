from app.models.models import Event
from datetime import datetime

URL_EVENTS = "/api/v1/events/"

# Test create event
def test_create_event(client):
    response = client.post(
        URL_EVENTS,
        json={
            "name": "Test Event",
            "description": "Test Event description",
            "start_date": "2025-01-23T03:15:52.860Z",
            "end_date": "2025-01-23T03:15:52.860Z",
            "capacity_total": 10,
            "capacity_actual": 0,
            "status": "planned"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Event"
    assert data["capacity_actual"] == 0

# Test get all events
def test_get_events(client):
    # Create an event
    response = client.post(
        URL_EVENTS,
        json={
            "name": "Test Event GET events",
            "description": "Test Event description",
            "start_date": "2025-01-23T03:15:52.860Z",
            "end_date": "2025-01-23T03:15:52.860Z",
            "capacity_total": 15,
            "capacity_actual": 0,
            "status": "planned"
        },
    )
    assert response.status_code == 200
    response = client.get(URL_EVENTS)
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

# Test get event
def test_get_event(client):
    # Create an event
    response = client.post(
        URL_EVENTS,
        json={
            "name": "Test Event GET",
            "description": "Test Event description",
            "start_date": "2025-01-23T03:15:52.860Z",
            "end_date": "2025-01-23T03:15:52.860Z",
            "capacity_total": 15,
            "capacity_actual": 0,
            "status": "planned"
        },
    )
    assert response.status_code == 200
    event_id = response.json()["id"]

    # Get event
    update_response = client.get(
        f"{URL_EVENTS}{event_id}",
    )
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["name"] == "Test Event GET"
    assert data["capacity_total"] == 15

# Test update event
def test_update_event(client):
    # Create an event
    response = client.post(
        URL_EVENTS,
        json={
            "name": "Updated Event Name",
            "description": "Test Event description",
            "start_date": "2025-01-23T03:15:52.860Z",
            "end_date": "2025-01-23T03:15:52.860Z",
            "capacity_total": 20,
            "capacity_actual": 0,
            "status": "planned"
        },
    )
    assert response.status_code == 200
    event_id = response.json()["id"]

    # Update event
    update_response = client.put(
        f"{URL_EVENTS}{event_id}",
        json={
            "description": "Updated description",
            "status": "completed",
            "capacity_total": 200,
        },
    )
    assert update_response.status_code == 200
    updated_data = update_response.json()
    assert updated_data["name"] == "Updated Event Name"
    assert updated_data["capacity_total"] == 200

# Test delete event
def test_delete_event(client):
    # Create event
    response = client.post(
        URL_EVENTS,
        json={
            "name": "Test Event Delete",
            "description": "Test Event description",
            "start_date": "2025-01-23T03:15:52.860Z",
            "end_date": "2025-01-23T03:15:52.860Z",
            "capacity_total": 10,
            "capacity_actual": 0,
            "status": "planned"
        },
    )
    assert response.status_code == 200
    event_id = response.json()["id"]

    # Delete event
    delete_response = client.delete(f"{URL_EVENTS}{event_id}")
    assert delete_response.status_code == 200
    delete_data = delete_response.json()
    assert delete_data["message"] == f"Event with id {event_id} successfully deleted"

    # Verify event is removed
    get_response = client.get(f"/events/{event_id}")
    assert get_response.status_code == 404
