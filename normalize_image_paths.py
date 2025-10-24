from DAL import get_all_projects, update_project

projects = get_all_projects()
changed = []
for p in projects:
    img = p.get('ImageFileName')
    if img and '/' not in img:
        new = f'images/{img}'
        update_project(p['id'], p['Title'], p['Description'], new, p.get('Url',''))
        changed.append((p['id'], new))

print('Updated:', changed)
