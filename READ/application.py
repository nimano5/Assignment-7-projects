###############################################################################
#                         IMPORT REQUIRED LIBRARIES/MODULES
###############################################################################
# 1. The FLASK framework (the webserver)
from flask import Flask

# 2. For opening and read the HTML file and showing them as the webpage
from flask import render_template

# 4. From the objects.py containing our classes for this application, only import the Movie class
from DAL import getAllMovies

# 5. Import the sqlite library
# SQLITE is NOT imported here. I do not have any SQL in this file
# import sqlite3

# 6. Instantiate the Flask() class and called it app
app=Flask(__name__)

###############################################################################
#                         CREATE YOUR WEBPAGE ROUTES
###############################################################################

# -----------------------------------------------------------------------------
# A) Create your home page.  Let's call the page "index"
# -----------------------------------------------------------------------------

#   Start with a decorator with no name. That way when they only type in your server's name
#   It will got to this page
@app.route("/")

#   Let's also add the name "index" since that is a common name for a website home page
@app.route("/index")    # Decorator - Now
@app.route("/home")     # Decorator - Now

#   Define what should happen when visiting this page by using a function called index()
def index():
    # Run a CLASS method called getAllMovies().  
    # NOTE: Instaniation is not needed.
    # CLASSNAME.METHODNAME()
    mList=getAllMovies()

    # Use render_template() to return the template index.html 
    # but pass it the list of movies stored in the variable mList
    # NOTE: The variable mList is a list of dictionaries.
    return render_template('index.html',message=mList )


app.run(debug=True)