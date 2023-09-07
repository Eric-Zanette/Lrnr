import requests
import json

url = "http://localhost:5000/api/schedule"

payload = {
    "topic": "hang gliding",
    "level": "beginner",
    "max_hours" : "10"
}

payload_json = json.dumps(payload)

response = requests.post(url, json=payload)

print(response.json())
