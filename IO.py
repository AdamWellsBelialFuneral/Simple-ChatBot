import json
from termcolor import colored
import sys
import os

# Input / Output
def get_input(settings, prompt, icon="\U0001F464"):
    print(f"{icon}{prompt}{settings['chat_separator']} ", end='', flush=True)
    user_input = input()
    sys.stdout.write("\033[F\033[K")  # Move cursor up one line and clear the line
    sys.stdout.flush()
    print(colored(f"{icon}{prompt}{settings['chat_separator']}", "blue"), colored(user_input, "dark_grey"))
    return user_input

def bot_print(settings, msg, icon="bot"):
    COLORED_CHATBOT_NAME = colored(settings['chatbot_name'], 'cyan', attrs=["bold"])
    if icon == "bot":
        print(f"\U0001F916{COLORED_CHATBOT_NAME}{settings['chat_separator']}", colored(msg, settings['theme']["casual"], attrs=["underline", "bold"]))
    elif icon == "PC":
        print(f"\U0001F4BB{COLORED_CHATBOT_NAME}{settings['chat_separator']}", colored(msg, settings['theme']["casual"], attrs=["underline", "bold"]))
