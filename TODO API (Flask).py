from flask import Flask, request, jsonify

app = Flask(__name__)
todos = []

@app.route("/todos", methods=["GET", "POST"])
def manage_todos():
    if request.method == "POST":
        todos.append(request.json["task"])
    return jsonify(todos)

if __name__ == "__main__":
    app.run(debug=True)
