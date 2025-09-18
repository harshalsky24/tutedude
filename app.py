from flask import Flask, jsonify
import json, os

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    file_path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
