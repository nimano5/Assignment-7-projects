import pytest
import os
import tempfile
from DAL import create_tables

@pytest.fixture(scope='session')
def test_db():
    """Create a temporary test database."""
    db_fd, db_path = tempfile.mkstemp()
    
    # Override the DB_PATH in DAL
    import DAL
    original_db_path = DAL.DB_PATH
    DAL.DB_PATH = db_path
    
    # Create tables
    create_tables()
    
    yield db_path
    
    # Clean up
    os.close(db_fd)
    os.unlink(db_path)
    DAL.DB_PATH = original_db_path