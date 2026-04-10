import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Create a TestClient for the FastAPI app"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to initial state before each test for isolation"""
    # Store original state
    original_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Competitive basketball team for varsity and JV players",
            "schedule": "Mondays, Wednesdays, Fridays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["james@mergington.edu", "alex@mergington.edu"]
        },
        "Tennis Club": {
            "description": "Learn and practice tennis skills with coached tournaments",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 16,
            "participants": ["ryan@mergington.edu", "mia@mergington.edu"]
        },
        "Art Club": {
            "description": "Explore painting, drawing, and visual art techniques",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 25,
            "participants": ["sarah@mergington.edu", "lucas@mergington.edu"]
        },
        "Drama Club": {
            "description": "Theatre production, acting, and stage performance",
            "schedule": "Thursdays, 3:30 PM - 5:30 PM",
            "max_participants": 20,
            "participants": ["isabella@mergington.edu", "ethan@mergington.edu"]
        },
        "Science Club": {
            "description": "Explore scientific concepts through experiments and projects",
            "schedule": "Mondays, 4:00 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["noah@mergington.edu", "ava@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop public speaking and critical thinking through debate",
            "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
            "max_participants": 14,
            "participants": ["mason@mergington.edu", "chloe@mergington.edu"]
        }
    }
    
    # Clear and repopulate activities with fresh data
    activities.clear()
    activities.update(original_activities)
    
    yield
    
    # Cleanup after test
    activities.clear()
    activities.update(original_activities)
