import sqlite3
from sqlite3 import Connection
from typing import List, Dict, Optional
import os
from datetime import datetime

# Path to the database file (in the project root)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'projects.db')


def get_connection() -> Connection:
    """Return a new SQLite connection with foreign keys enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON')
    return conn


def init_db() -> None:
    """Create the projects table if it doesn't exist."""
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        Description TEXT,
        ImageFileName TEXT,
        Url TEXT,
        created_at TEXT NOT NULL
    );
    '''
    conn = get_connection()
    try:
        conn.execute(create_table_sql)
        conn.commit()
    finally:
        conn.close()


def row_to_dict(row: sqlite3.Row) -> Dict:
    return {k: row[k] for k in row.keys()}


def get_all_projects() -> List[Dict]:
    """Return list of all projects as dicts."""
    conn = get_connection()
    try:
        cur = conn.execute('SELECT * FROM projects ORDER BY created_at DESC')
        rows = cur.fetchall()
        return [row_to_dict(r) for r in rows]
    finally:
        conn.close()


def get_project_by_id(project_id: int) -> Optional[Dict]:
    conn = get_connection()
    try:
        cur = conn.execute('SELECT * FROM projects WHERE id = ?', (project_id,))
        row = cur.fetchone()
        return row_to_dict(row) if row else None
    finally:
        conn.close()


def add_project(title: str, description: str = '', image_filename: str = '', url: str = '') -> int:
    """Insert a new project and return its id."""
    conn = get_connection()
    try:
        now = datetime.utcnow().isoformat()
        cur = conn.execute(
            'INSERT INTO projects (Title, Description, ImageFileName, Url, created_at) VALUES (?, ?, ?, ?, ?)',
            (title, description, image_filename, url, now)
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()


def update_project(project_id: int, title: str, description: str, image_filename: str = '', url: str = '') -> bool:
    """Update a project. Returns True if a row was updated."""
    conn = get_connection()
    try:
        cur = conn.execute(
            'UPDATE projects SET Title = ?, Description = ?, ImageFileName = ?, Url = ? WHERE id = ?',
            (title, description, image_filename, url, project_id)
        )
        conn.commit()
        return cur.rowcount > 0
    finally:
        conn.close()


def delete_project(project_id: int) -> bool:
    """Delete a project by id. Returns True if a row was deleted."""
    conn = get_connection()
    try:
        cur = conn.execute('DELETE FROM projects WHERE id = ?', (project_id,))
        conn.commit()
        return cur.rowcount > 0
    finally:
        conn.close()


if __name__ == '__main__':
    # Simple self-test: initialize DB and print current projects
    init_db()
    print('Database initialized at', DB_PATH)
    projects = get_all_projects()
    print('Projects count:', len(projects))
