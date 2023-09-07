from flask import request, Flask, jsonify
from app.gpt import get_dictionary
from app import app

@app.route("/api/schedule", methods=["POST"])
def get_schedule():
    topic = request.get_json().get("topic")
    level = request.get_json().get("level")
    max_hours = request.get_json().get("max_hours")
    result = get_dictionary(topic, level, max_hours)
    print(result)
    return jsonify(result)
