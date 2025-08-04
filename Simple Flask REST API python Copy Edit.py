from flask import Flask, jsonify, request

app = Flask(__name__)
data = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    data.append(item)
    return jsonify({"status":"added"}), 201

if __name__ == '__main__':
    app.run(debug=True)
