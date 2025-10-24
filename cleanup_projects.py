from DAL import init_db, get_all_projects, delete_project

def cleanup_projects():
    """Keep only the first three specific projects and remove others."""
    # The three projects to keep (exact titles)
    projects_to_keep = [
        "🌟 AI Feedback Form Prototype",
        "🧮 Agile Front-End System Design",
        "📊 Automated Dashboard Development"
    ]
    
    # Get all projects
    all_projects = get_all_projects()
    
    # Delete projects not in our keep list
    for project in all_projects:
        if project['Title'] not in projects_to_keep:
            print(f"Deleting project: {project['Title']}")
            delete_project(project['id'])
        else:
            print(f"Keeping project: {project['Title']}")

if __name__ == '__main__':
    cleanup_projects()