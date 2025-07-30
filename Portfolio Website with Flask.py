from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("<h1>My Portfolio</h1><p>Welcome to my page!</p>")

if __name__ == "__main__":
    app.run(debug=True)
