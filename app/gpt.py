import os
import copy

""" import openai """
from dotenv import load_dotenv

api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")

""" openai.api_key = api_key """

dayList = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_dictionary(topic, level, max_hours):
    MODEL_NAME = "gpt-3.5-turbo"
    system_msg = (
        "You are a ai learning assistant.  You provide schedules for learning based on a skill/topic chosen by the user. "
        f"The topic is {topic} and the level of learning is {level}"
    )
    user_msg = (
        "Please generate a learning schedule in the form of a list of lists. Here are the requirements:"
        "- The output should be a list of lists with the structure: [[time for task (in hours), task, resource, tips]]. "
        f"Combined total hours should be {max_hours}"
        "- Each 'task' entry should describe what the user should do, like study or create something."
        "- The 'resource' should point to a specific REAL text or source, specifying the page number or chapter if possible."
        "- Include any 'tips' as contextual information."
        "- It's fine to repeat the same lesson multiple times, as is often the case with learning."
        "IMPORTANT: The output should ONLY include the dictionary, with no additional text. NO ADDITIONAL TEXT"
        "stick with only 1 or two sources (unless free), so the user does not have to buy too many"
    )

    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
    )

    return response["choices"][0]["message"]["content"]


def add_days(learn_list, free_days=dayList):
    days_length = len(free_days)
    schedule = {}
    for i, day in enumerate(learn_list):
        if i >= days_length:
            i -= days_length + 1
        if free_days[i] not in schedule.keys():
            schedule[free_days[i]] = [day]
        else:
            schedule[free_days[i]].append(day)
    return schedule


def add_timing():
    intervals = []
    for hour in range(24):  #
        for minute in [0, 15, 30, 45]:
            intervals.append(f"{hour:02d}:{minute:02d}")
    return intervals


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


def make_schedule():
    local_learn_list = copy.deepcopy(learn_list)
    dayList = add_days(local_learn_list)
    timing = add_timing()
    lesson_dict = {}
    for day in dayList.keys():
        lessons = dayList[day]
        lessonCount = 1
        time_dict = {}
        for lesson in lessons:
            timeNum = lesson[0] * 4
            time = timing[lessonCount : lessonCount + timeNum]
            lessonCount += timeNum
            for slot in time:
                time_dict[slot] = lesson[1:]
        lesson_dict[day] = time_dict
    print(lesson_dict)
    return lesson_dict
