# Personal Website - Flask Application

A modern, responsive personal portfolio website built with Flask, showcasing Nikitha Manoj Thomas's professional experience, projects, and skills.

## Features

- **Responsive Design**: Mobile-first approach with modern CSS
- **Dynamic Navigation**: Active page highlighting
- **Contact Form**: Server-side validation and form handling
- **Project Showcase**: Detailed project descriptions with skills tags
- **Resume Download**: PDF resume download functionality
- **Professional Layout**: Clean, modern design with floating particles background

## Project Structure

```
personal-website/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # Jinja2 templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   ├── projects.html     # Projects showcase
│   ├── resume.html       # Resume page
│   ├── contact.html      # Contact form
│   └── thankyou.html     # Thank you page
├── static/               # Static assets
│   ├── css/
│   │   └── styles.css    # Main stylesheet
│   ├── images/
│   │   └── headshot.jpg  # Profile image
│   └── Thomas_Nikitha_Resume_updated.pdf
└── venv/                 # Virtual environment
```

## Installation & Setup

1. **Clone or download the project**
2. **Activate the virtual environment**:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```powershell
   python app.py
   ```

5. **Open your browser** and navigate to `http://localhost:5000`

## Available Routes

- `/` - Home page
- `/about` - About page
- `/projects` - Projects showcase
- `/resume` - Resume page
- `/contact` - Contact form
- `/thank-you` - Thank you page
- `/resume/download` - Resume PDF download

## Technologies Used

- **Backend**: Flask 2.3.3
- **Templates**: Jinja2
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design patterns
- **Form Handling**: Flask-WTF (server-side validation)

## Features Implemented

### Navigation
- Dynamic active page highlighting
- Responsive navigation menu
- Consistent header across all pages

### Contact Form
- Client-side and server-side validation
- Password confirmation
- Email validation
- Form submission handling with flash messages

### Static File Serving
- CSS stylesheets
- Images (profile photo)
- PDF resume download

### Template System
- Base template with common elements
- Template inheritance
- Dynamic content rendering
- Personal information centralization

## Development

The application runs in debug mode by default. To modify personal information, update the `PERSONAL_INFO` dictionary in `app.py`.

## Deployment

For production deployment:
1. Set `debug=False` in `app.py`
2. Use a production WSGI server like Gunicorn
3. Configure environment variables for sensitive data
4. Set up proper logging and error handling

## License

This project is for personal portfolio purposes.

## Docker (Build & Run)

These instructions show how to build and run the site using Docker on Windows PowerShell.

1. Build the Docker image (from project root):

```powershell
docker build -t personal-website:latest .
```

2. Run the container:

```powershell
docker run --rm -p 5000:5000 --name personal-website personal-website:latest
```

3. Or use docker-compose for easier local development:

```powershell
docker-compose up --build
```

Open http://localhost:5000 in your browser. The app is served by Gunicorn in the container.

Notes:
- The Dockerfile uses a read-only bind (volume) in `docker-compose.yml` to avoid accidental code changes being written into the image. If you want code changes to be reflected immediately, change the volume to a writable mount or remove the `:ro` flag.
- If you want to run the Flask development server (not recommended for production), set the `CMD` in the Dockerfile to `python app.py` and rebuild.