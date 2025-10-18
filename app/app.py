# app/app.py
"""
Flask app module for CynthiaFlask project.
Contains routes and view functions.
"""

from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

# Default route
@app.route('/')
def home():
    """
       Render the about page.
       """
    return "Hello CPS3500!"

# New page route
@app.route('/new_page')
def new_page():
    """
       Render the about page.
       """
    return "This is a New Page!"

# Route with a variable and template rendering
@app.route('/user/<username>')
def user_page(username):
    """
       Render the about page.
       """
    # Render the template file and pass the username variable to it
    return render_template('user.html', username=username)


# Only runs when we execute this file directly (not when imported)
if __name__ == '__main__':
    app.run(debug=True)
