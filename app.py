from flask import Flask, render_template, request, redirect, url_for, flash
import os
from DAL import get_all_projects
from DAL import add_project
from DAL import update_project, get_project_by_id
import os

app = Flask(__name__)
# Load secret key from environment for safer configuration in Docker/production
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your-secret-key-here')  # override via env

# Personal information - can be moved to a config file later
PERSONAL_INFO = {
    'name': 'Nikitha Manoj Thomas',
    'title': 'Graduate Student | Information Systems | Indiana University',
    'email': 'nimano@iu.edu',
    'linkedin': 'https://linkedin.com/in/thomas-nikitha',
    'github': 'https://github.com/nimano5/AiDD-nimano-lab01',
    'location': 'Bloomington, Indiana'
}

@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html', personal_info=PERSONAL_INFO)

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html', personal_info=PERSONAL_INFO)

@app.route('/projects')
def projects():
    """Projects page route"""
    projects_list = get_all_projects()
    return render_template('projects.html', personal_info=PERSONAL_INFO, projects=projects_list)


@app.route('/projects/new', methods=['GET', 'POST'])
def add_project_route():
    """Add new project form and handler"""
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        image = request.form.get('image', '').strip()

        errors = []
        if not title:
            errors.append('Title is required')

        if errors:
            for e in errors:
                flash(e, 'error')
            return render_template('add_project.html', personal_info=PERSONAL_INFO, title=title, description=description, image=image)

        # Insert into DB
        add_project(title, description, image)
        flash('Project added successfully', 'success')
        return redirect(url_for('projects'))

    return render_template('add_project.html', personal_info=PERSONAL_INFO)


@app.route('/projects/<int:project_id>/edit', methods=['GET', 'POST'])
def edit_project(project_id):
    project = get_project_by_id(project_id)
    if not project:
        flash('Project not found', 'error')
        return redirect(url_for('projects'))

    images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images')
    try:
        images = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]
    except Exception:
        images = []

    if request.method == 'POST':
        image = request.form.get('image', '').strip()
        # Update project (preserve title & description)
        update_project(project_id, project['Title'], project['Description'], image, project.get('Url',''))
        flash('Project updated', 'success')
        return redirect(url_for('projects'))

    return render_template('edit_project.html', personal_info=PERSONAL_INFO, project=project, images=images)

@app.route('/resume')
def resume():
    """Resume page route"""
    return render_template('resume.html', personal_info=PERSONAL_INFO)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route with form handling"""
    if request.method == 'POST':
        # Get form data
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')
        message = request.form.get('message')
        
        # Basic validation
        errors = []
        
        if not first_name:
            errors.append('First name is required')
        if not last_name:
            errors.append('Last name is required')
        if not email:
            errors.append('Email address is required')
        elif '@' not in email:
            errors.append('Please enter a valid email address')
        if not password:
            errors.append('Password is required')
        elif len(password) < 8:
            errors.append('Password must be at least 8 characters long')
        if password != confirm_password:
            errors.append('Passwords do not match')
        
        if errors:
            flash('Please correct the following errors: ' + ', '.join(errors), 'error')
            return render_template('contact.html', personal_info=PERSONAL_INFO)
        
        # If validation passes, redirect to thank you page
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('thank_you'))
    
    return render_template('contact.html', personal_info=PERSONAL_INFO)

@app.route('/thank-you')
def thank_you():
    """Thank you page route"""
    return render_template('thankyou.html', personal_info=PERSONAL_INFO)

@app.route('/resume/download')
def download_resume():
    """Route to serve resume PDF"""
    return app.send_static_file('Thomas_Nikitha_Resume_updated.pdf')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
