from app import app
from DAL import get_all_projects

def main():
    with app.test_client() as c:
        # Get projects to find an id
        projects = get_all_projects()
        if not projects:
            print('No projects in DB')
            return
        pid = projects[0]['id']
        print('Using project id:', pid)

        # Post image selection
        resp = c.post(f'/projects/{pid}/edit', data={'image':'headshot.jpg'}, follow_redirects=True)
        print('POST edit status:', resp.status_code)

        # Check projects page
        res = c.get('/projects')
        data = res.get_data(as_text=True)
        print('Projects page contains headshot.jpg ->', 'headshot.jpg' in data)

if __name__ == '__main__':
    main()
