from DAL import get_all_projects, update_project
import os, json
BASE=os.path.dirname(os.path.abspath(__file__))
ps=get_all_projects()
changed=[]
missing=[]
for p in ps:
    img=p.get('ImageFileName')
    if not img:
        continue
    # normalize backslashes
    img_norm=img.replace('\\','/').replace('static/','')
    if not img_norm.startswith('images/'):
        img_norm='images/'+img_norm.lstrip('/')
    if img_norm!=img:
        update_project(p['id'],p['Title'],p['Description'],img_norm,p.get('Url',''))
        changed.append((p['id'],img_norm))
    file_path=os.path.join(BASE,'static', img_norm)
    if not os.path.exists(file_path):
        missing.append((p['id'],img_norm))
print('changed:',json.dumps(changed,ensure_ascii=False))
print('missing:',json.dumps(missing,ensure_ascii=False))
