# First: pip install flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, World!</h1><p>This is my first Flask app.</p>"

@app.route('/user/<name>')
def user(name):
    return f"<h1>Hello, {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)

# Run this, then visit http://127.0.0.1:5000/ and http://127.0.0.1:5000/user/Alice
