import sqlite3
from DAL import create_tables, add_project

def init_database():
    # Create tables
    create_tables()
    
    # Add initial projects
    initial_projects = [
        {
            'Title': '🌟 AI Feedback Form Prototype',
            'Description': 'Developed an AI-powered feedback form that provides real-time suggestions.',
            'Image': 'images/project1.jpg'
        },
        {
            'Title': '🧮 Agile Front-End System Design',
            'Description': 'Created a responsive front-end system using agile methodologies.',
            'Image': 'images/project2.jpg'
        },
        {
            'Title': '📊 Automated Dashboard Development',
            'Description': 'Built an automated dashboard for real-time data visualization.',
            'Image': 'images/project3.jpg'
        }
    ]
    
    for project in initial_projects:
        try:
            add_project(project['Title'], project['Description'], project['Image'])
        except sqlite3.IntegrityError:
            # Skip if project already exists
            pass

if __name__ == '__main__':
    init_database()