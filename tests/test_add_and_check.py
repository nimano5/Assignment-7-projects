from app import app
from DAL import get_all_projects

def main():
    with app.test_client() as c:
        # Post a new project
        resp = c.post('/projects/new', data={
            'title': 'Test Project From Script',
            'description': 'This is a test project added by an automated script.',
            'image': ''
        }, follow_redirects=True)
        print('POST status:', resp.status_code)

        # Get projects page
        res = c.get('/projects')
        data = res.get_data(as_text=True)
        print('Projects page status:', res.status_code)
        print('Contains Test Project ->', 'Test Project From Script' in data)

        # Print count from DB
        projects = get_all_projects()
        print('DB count:', len(projects))

if __name__ == '__main__':
    main()
