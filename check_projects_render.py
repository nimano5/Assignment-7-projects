from app import app

def main():
    with app.test_client() as c:
        res = c.get('/projects')
        print('Status:', res.status_code)
        data = res.get_data(as_text=True)
        # Check for titles (without emojis to simplify matching)
        checks = [
            'AI Feedback Form Prototype',
            'Agile Front-End System Design',
            'Automated Dashboard Development'
        ]
        for t in checks:
            print(f"{t} in page ->", t in data)

if __name__ == '__main__':
    main()
