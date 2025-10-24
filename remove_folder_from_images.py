from DAL import get_all_projects, update_project
import os
ps = get_all_projects()
changed = []
for p in ps:
    img = p.get('ImageFileName')
    if img:
        # Remove any folder references
        img_name = os.path.basename(img.replace('\\','/'))
        if img_name != img:
            update_project(p['id'], p['Title'], p['Description'], img_name, p.get('Url',''))
            changed.append((p['id'], img_name))
print('Updated:', changed)
