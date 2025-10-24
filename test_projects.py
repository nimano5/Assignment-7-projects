import pytest
from flask.testing import FlaskClient
from app import app
import json
from DAL import init_db, add_project

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def init_test_projects():
    """Initialize the database with test projects."""
    init_db()
    projects = [
        {
            'title': 'Test Project 1',
            'description': 'A test project description',
            'image': 'test1.jpg'
        },
        {
            'title': 'Test Project 2',
            'description': 'Another test project',
            'image': 'test2.jpg'
        }
    ]
    
    for p in projects:
        add_project(p['title'], p['description'], p['image'])
    
    return projects

def test_index_route(client):
    """Test the home page route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Nikitha Manoj Thomas' in response.data

def test_about_route(client):
    """Test the about page route."""
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About Me' in response.data

def test_projects_route(client, init_test_projects):
    """Test the projects page route."""
    response = client.get('/projects')
    assert response.status_code == 200
    # Check if test projects are displayed
    assert b'Test Project 1' in response.data
    assert b'Test Project 2' in response.data

def test_add_project_get(client):
    """Test the add project form page."""
    response = client.get('/projects/new')
    assert response.status_code == 200
    # Template shows header "Add a New Project"
    assert b'Add a New Project' in response.data

def test_add_project_post(client):
    """Test adding a new project."""
    data = {
        'title': 'New Test Project',
        'description': 'A new project added through tests',
        'image': 'new_test.jpg'
    }
    response = client.post('/projects/new', data=data)
    assert response.status_code == 302  # Redirect after successful addition
    
    # Verify project appears in projects list
    response = client.get('/projects')
    assert b'New Test Project' in response.data

def test_edit_project(client, init_test_projects):
    """Test editing a project."""
    # Get first project
    response = client.get('/projects')
    assert response.status_code == 200
    
    # Submit edit form for project id 1
    data = {
        'image': 'edited.jpg'
    }
    response = client.post('/projects/1/edit', data=data)
    assert response.status_code == 302  # Redirect after successful edit
    
    # Verify changes in projects list
    response = client.get('/projects')
    assert b'edited.jpg' in response.data

def test_contact_form(client):
    """Test the contact form submission."""
    data = {
        'firstName': 'Test',
        'lastName': 'User',
        'email': 'test@example.com',
        'password': 'testpass123',
        'confirmPassword': 'testpass123',
        'message': 'Test message'
    }
    response = client.post('/contact', data=data)
    assert response.status_code == 302  # Redirect to thank you page
    
    # Check thank you page
    response = client.get('/thank-you')
    assert response.status_code == 200
    assert b'Thank You' in response.data

def test_invalid_contact_form(client):
    """Test contact form validation."""
    # Missing required fields
    data = {
        'firstName': '',
        'lastName': 'User',
        'email': 'invalid-email',
        'password': 'short',
        'confirmPassword': 'different',
        'message': 'Test message'
    }
    response = client.post('/contact', data=data)
    assert response.status_code == 200  # Stay on form page
    assert b'error' in response.data.lower()

def test_resume_download(client):
    """Test the resume download route."""
    response = client.get('/resume/download')
    assert response.status_code == 200
    assert response.mimetype == 'application/pdf'

def test_404_handling(client):
    """Test handling of nonexistent routes."""
    response = client.get('/nonexistent-page')
    assert response.status_code == 404

# Add error simulation tests
def test_projects_db_error(client, monkeypatch):
    """Test projects page handling of database errors."""
    def mock_get_all_projects():
        raise Exception("Database error")
    
    # Patch the function used by the Flask app (app imports get_all_projects)
    import app as app_module
    monkeypatch.setattr(app_module, "get_all_projects", mock_get_all_projects)
    # When testing error handling, Flask's TESTING mode propagates exceptions
    # (so the test would see the exception instead of a 500 response). Disable
    # exception propagation for this request so Flask produces a 500 response.
    client.application.config['TESTING'] = False
    client.application.config['PROPAGATE_EXCEPTIONS'] = False

    response = client.get('/projects')
    assert response.status_code == 500  # Should return internal server error