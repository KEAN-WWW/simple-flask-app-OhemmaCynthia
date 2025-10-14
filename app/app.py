from flask import Flask, render_template

# Create Flask instance
app = Flask(__name__)

# Default route
@app.route('/')
def home():
    return "Hello CPS3500!"

# New route
@app.route('/new_page')
def new_page():
    return "This is a New Page!"

# Template route
@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
