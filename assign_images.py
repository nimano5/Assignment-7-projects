from DAL import get_all_projects, update_project
import os

IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images')

# Images to ignore (like headshots)
IGNORE = {'headshot.jpg'}

# Simple token match: if image filename (without extension) contains a token from project title, assign it

def tokens(s):
    return {t.lower() for t in s.replace('-', ' ').replace('_',' ').split()}


def main():
    images = [f for f in os.listdir(IMAGES_DIR) if os.path.isfile(os.path.join(IMAGES_DIR, f))]
    images = [f for f in images if f not in IGNORE]
    print('Found images to consider:', images)

    projects = get_all_projects()
    for p in projects:
        title_tokens = tokens(p['Title'])
        matched = None
        for img in images:
            name = os.path.splitext(img)[0].lower()
            img_tokens = set(name.replace('-', ' ').replace('_',' ').split())
            # if intersection of tokens is non-empty, assign
            if title_tokens & img_tokens:
                matched = img
                break
        if matched:
            print(f"Assigning {matched} to project {p['id']} - {p['Title']}")
            update_project(p['id'], p['Title'], p['Description'], matched, p.get('Url',''))
        else:
            print(f"No match for project {p['id']} - {p['Title']}")

if __name__ == '__main__':
    main()
