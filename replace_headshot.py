from DAL import get_all_projects, update_project

placeholders = [
    'project_placeholder_1.svg',
    'project_placeholder_2.svg',
    'project_placeholder_3.svg'
]


def main():
    projects = get_all_projects()
    idx = 0
    changed = []
    for p in projects:
        if p.get('ImageFileName') == 'headshot.jpg':
            new_img = placeholders[idx % len(placeholders)]
            update_project(p['id'], p['Title'], p['Description'], new_img, p.get('Url',''))
            changed.append((p['id'], new_img))
            idx += 1
    print('Updated:', changed)

if __name__ == '__main__':
    main()
