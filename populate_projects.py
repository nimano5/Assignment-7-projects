from DAL import init_db, get_all_projects, add_project

def load_existing_titles():
    projects = get_all_projects()
    return {p['Title'] for p in projects}

def main():
    # Ensure DB and table exist
    init_db()

    existing = load_existing_titles()

    # Projects extracted from templates/projects.html
    projects_to_add = [
        {
            'Title': '🌟 AI Feedback Form Prototype',
            'Description': 'Designed an interactive mobile feedback form that made app reviews quick and fun using emoji ratings and tap-based "chips." This project focused on improving user engagement through innovative design thinking principles.',
            'ImageFileName': ''
        },
        {
            'Title': '🧮 Agile Front-End System Design',
            'Description': 'Led a four-member Agile team as Product Manager to develop a responsive website prototype for a university client. This project demonstrated end-to-end system design from requirements gathering to prototype delivery.',
            'ImageFileName': ''
        },
        {
            'Title': '📊 Automated Dashboard Development',
            'Description': 'Developed automated dashboards for project performance tracking and resource allocation optimization during my time at Khimji Ramdas and Sadik and Partners in Oman.',
            'ImageFileName': ''
        }
    ]

    added = []
    skipped = []
    for p in projects_to_add:
        if p['Title'] in existing:
            skipped.append(p['Title'])
            continue
        rowid = add_project(p['Title'], p['Description'], p['ImageFileName'])
        added.append((rowid, p['Title']))

    print('Added:', added)
    print('Skipped (already exist):', skipped)

if __name__ == '__main__':
    main()
