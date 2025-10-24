from DAL import get_all_projects, update_project
import os

placeholders = [
    'project_placeholder_1.svg',
    'project_placeholder_2.svg',
    'project_placeholder_3.svg'
]


def main():
    projects = get_all_projects()
    idx = 0
    for p in projects:
        if not p.get('ImageFileName'):
            img = placeholders[idx % len(placeholders)]
            print(f"Assigning {img} to project {p['id']} - {p['Title']}")
            update_project(p['id'], p['Title'], p['Description'], img, p.get('Url',''))
            idx += 1

if __name__ == '__main__':
    main()
