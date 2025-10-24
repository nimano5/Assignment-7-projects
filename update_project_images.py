from DAL import update_project, get_all_projects

# Map project titles to their corresponding image files
IMAGE_MAPPING = {
    '🌟 AI Feedback Form Prototype': 'AI Feedback Form.jpg',
    '🧮 Agile Front-End System Design': 'Agile Front-End.jpg',
    '📊 Automated Dashboard Development': 'Automated.jpg'
}

def update_project_images():
    projects = get_all_projects()
    for project in projects:
        if project['Title'] in IMAGE_MAPPING:
            # Update project keeping same title and description but adding image
            update_project(
                project['id'],
                project['Title'],
                project['Description'],
                IMAGE_MAPPING[project['Title']],
                project.get('Url', '')
            )
            print(f"Updated {project['Title']} with image {IMAGE_MAPPING[project['Title']]}")

if __name__ == '__main__':
    update_project_images()