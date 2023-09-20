from flask import request, Flask, jsonify
from app.gpt import get_dictionary, add_days, make_schedule
from app import app

learn_list = [
    [
        2,
        "Introduction to Hang Gliding",
        "The Hang Glider's Bible by George L. Worthington, Chapter 1",
        "Read and understand the basic concepts and principles of hang gliding.",
    ],
    [
        1,
        "Safety Procedures",
        "The Hang Glider's Bible by George L. Worthington, Chapter 4",
        "Study the safety procedures and precautions to ensure a safe hang gliding experience.",
    ],
    [
        1,
        "Understanding Equipment",
        "The Hang Glider's Bible by George L. Worthington, Chapter 2",
        "Familiarize yourself with the different components of a hang glider and their functions.",
    ],
    [
        2,
        "Ground Handling Practice",
        "https://www.youtube.com/watch?v=9TnmvGpFTgs",
        "Watch and follow along with instructional videos on ground handling techniques.",
    ],
    [
        1,
        "Flight Simulator Practice",
        "http://www.aerosafety.ca/para/paraflightsim.php",
        "Use the flight simulator to practice controlling a virtual hang glider.",
    ],
    [
        2,
        "Tandem Flight Experience",
        "Book a tandem hang gliding lesson with a certified instructor.",
        "Experience a real hang gliding flight under the guidance of an expert.",
    ],
    [
        1,
        "Understanding Weather Conditions",
        "The Hang Glider's Bible by George L. Worthington, Chapter 3",
        "Learn about how weather conditions impact hang gliding and how to make informed decisions based on them.",
    ],
    [
        1,
        "Understanding Weather Conditions",
        "The Hang Glider's Bible by George L. Worthington, Chapter 3",
        "Learn about how weather conditions impact hang gliding and how to make informed decisions based on them.",
    ],
    [
        1,
        "Understanding Weather Conditions",
        "The Hang Glider's Bible by George L. Worthington, Chapter 3",
        "Learn about how weather conditions impact hang gliding and how to make informed decisions based on them.",
    ],
    [
        1,
        "Understanding Weather Conditions",
        "The Hang Glider's Bible by George L. Worthington, Chapter 3",
        "Learn about how weather conditions impact hang gliding and how to make informed decisions based on them.",
    ],
]


@app.route("/api/schedule", methods=["POST"])
def get_schedule():
    topic = request.get_json().get("topic")
    level = request.get_json().get("level")
    """ max_hours = request.get_json().get("max_hours") """
    result = make_schedule()
    return jsonify(result)
