from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

# MongoDB configuration (update with your MongoDB URI)
app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_db"
mongo = PyMongo(app)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.get_json()
    item_name = data.get('itemName')
    item_description = data.get('itemDescription')

    if not item_name or not item_description:
        return jsonify({"error": "Both fields are required"}), 400

    mongo.db.todos.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })
    return jsonify({"message": "To-Do item saved successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
