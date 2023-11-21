"""
Web server gateway interface
"""

from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    """
    Index function
    """
    return "<p>Index page</p> "


@app.route('/hello')
def hello_world() -> str:
    """
    Hello world function
    """
    return "<p>Hello, world!!!!!!</p>"


@app.route('/user/<username>')
def profile(username: str) -> str:
    """
    Show user profile function
    """
    return f"User {escape(username)}"


with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello_world'))
    print(url_for('profile', username='John Doe'))


@app.route('/login', methods=['GET', 'POST'])
def login() -> str:
    """
    Login function
    """
    if request.method == 'POST':
        # return do_the_login()
    else:
        # return show_the_login_form()
