# operations.py
import json
from nltk.chat.util import Chat, reflections

from env import PATH

def read_patterns():
    try:
        with open(f'{PATH}/patterns.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        return []

def write_patterns(patterns):
    try:
        with open(f'{PATH}/patterns.json', 'w') as file:
            json.dump(patterns, file, indent=4)
            print("New pattern added!")
    except Exception as e:
        # Handle any errors that occur during file writing
        print(f"Error writing patterns: {e}")

def update_chatbot(patterns):
    return Chat(patterns, reflections)

def translate_variables(settings, patterns):
    modified_patterns = []
    for pattern, replies in patterns:
        modified_replies = [reply.replace("{chatbot_name}", settings['chatbot_name']) for reply in replies]
        modified_patterns.append((pattern, modified_replies))
    return modified_patterns
