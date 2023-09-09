import os
import openai
from dotenv import load_dotenv

api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")

openai.api_key = api_key


def get_dictionary(topic, level, max_hours):
    MODEL_NAME = "gpt-3.5-turbo"
    system_msg = (
        "You are a ai learning assistant.  You provide schedules for learning based on a skill/topic chosen by the user. "
        f"The topic is {topic} and the level of learning is {level}"
    )
    user_msg = (
        "Please generate a learning schedule in the form of a dictionary. Here are the requirements:"
        "- The output should be a dictionary with the structure: {time for task : [task, resource, tips]}. "
        f"Combined total hours should be {max_hours}"
        "- Each 'task' entry should describe what the user should do, like study or create something."
        "- The 'resource' should point to a specific REAL text or source, specifying the page number or chapter if possible."
        "- Include any 'tips' as contextual information."
        "- It's fine to repeat the same lesson multiple times, as is often the case with learning."
        "IMPORTANT: The output should ONLY include the dictionary, with no additional text."
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
