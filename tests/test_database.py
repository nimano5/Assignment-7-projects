import os
import pytest
import tempfile
from DAL import create_tables, add_project, get_all_projects, get_project_by_id, update_project, delete_project, DB_PATH

@pytest.fixture
def temp_db():
    """Create a temporary database for testing."""
    # Create a temporary file
    fd, temp_path = tempfile.mkstemp()
    # Close the file descriptor so SQLite can open the file on Windows
    os.close(fd)
    
    # Store original DB path
    original_db = DB_PATH
    
    # Override the DB_PATH in DAL
    import DAL
    DAL.DB_PATH = temp_path
    
    # Initialize the test database
    create_tables()
    
    yield temp_path  # Provide the temp db path to the test
    
    # Cleanup: restore original DB path and remove temp file
    DAL.DB_PATH = original_db
    os.unlink(temp_path)

def test_database_initialization(temp_db):
    """Test that database can be initialized."""
    # Simply check that the database file exists
    assert os.path.exists(temp_db)

def test_add_project(temp_db):
    """Test adding a project."""
    # Add a test project
    project_title = "Test Project"
    project_desc = "Test Description"
    project_image = "test.jpg"
    
    project_id = add_project(project_title, project_desc, project_image)
    
    # Verify project was added
    assert project_id > 0
    
    # Retrieve and verify project
    project = get_project_by_id(project_id)
    assert project is not None
    assert project['Title'] == project_title
    assert project['Description'] == project_desc
    assert project['ImageFileName'] == project_image

def test_get_all_projects(temp_db):
    """Test retrieving all projects."""
    # Add multiple test projects
    projects_data = [
        ("Project 1", "Desc 1", "img1.jpg"),
        ("Project 2", "Desc 2", "img2.jpg"),
        ("Project 3", "Desc 3", "img3.jpg")
    ]
    
    for title, desc, img in projects_data:
        add_project(title, desc, img)
    
    # Retrieve all projects
    projects = get_all_projects()
    
    # Verify projects count
    assert len(projects) == len(projects_data)
    
    # Verify projects are returned in reverse chronological order (newest first)
    assert projects[0]['Title'] == "Project 3"
    assert projects[1]['Title'] == "Project 2"
    assert projects[2]['Title'] == "Project 1"

def test_update_project(temp_db):
    """Test updating a project."""
    # Add a project
    project_id = add_project("Original Title", "Original Desc", "original.jpg")
    
    # Update the project
    new_title = "Updated Title"
    new_desc = "Updated Description"
    new_image = "updated.jpg"
    
    success = update_project(project_id, new_title, new_desc, new_image)
    assert success is True
    
    # Verify update
    updated_project = get_project_by_id(project_id)
    assert updated_project['Title'] == new_title
    assert updated_project['Description'] == new_desc
    assert updated_project['ImageFileName'] == new_image

def test_delete_project(temp_db):
    """Test deleting a project."""
    # Add a project
    project_id = add_project("To Delete", "Will be deleted", "delete.jpg")
    
    # Verify project exists
    assert get_project_by_id(project_id) is not None
    
    # Delete project
    success = delete_project(project_id)
    assert success is True
    
    # Verify project no longer exists
    assert get_project_by_id(project_id) is None

def test_nonexistent_project(temp_db):
    """Test handling of nonexistent project ID."""
    nonexistent_id = 9999
    project = get_project_by_id(nonexistent_id)
    assert project is None

def test_invalid_update(temp_db):
    """Test updating a nonexistent project."""
    success = update_project(9999, "Title", "Description", "image.jpg")
    assert success is False