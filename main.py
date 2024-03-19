import os
import sys
import subprocess

from nltk.chat.util import Chat, reflections
from difflib import get_close_matches

from termcolor import colored

import json

theme = {
        "casual": "light_grey",
        "dangerous": "light_red",
        "secure": "cyan",
        "positive": "green",
        "warning": "yellow",
    }

# Config to hide running command
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE

chatbot_name = "Jorge"

colored_chatbot_name = colored(chatbot_name, "cyan", attrs=["bold"])

print("\n" + f"🖥 [{colored_chatbot_name}]", "chatbot", colored("initialized!\n", theme["positive"]))

def get_input(prompt):
    print(prompt, end='', flush=True)
    user_input = input()
    # Move cursor up one line and clear the line
    sys.stdout.write("\033[F\033[K")
    sys.stdout.flush()
    return user_input

command_patterns = [
    (r'open youtube|open yt', [colored('Opening YouTube...', theme['secure'])]),
    (r'turn off computer|turn off PC|shutdown', [colored('Turning off computer...', theme['dangerous'])]),
    (r"abort shutdown|abort|don't turn off|cancel shutdown", [colored("Aborting shutdown...", theme['positive'])]),
    (r"open URL(.*)", [colored("Opening URL...", theme["warning"])]),

]

commands = {
    colored('Opening YouTube...', theme['secure']): lambda arg: os.startfile("https://www.youtube.com"),
    colored('Turning off computer...', theme['dangerous']): lambda arg: subprocess.run(["shutdown", "-s", "-t", "1800"]),
    colored("Aborting shutdown...", theme['positive']) : lambda arg: subprocess.run(["shutdown", "-a"]),
    colored("Opening URL...", theme["warning"]) : lambda arg: os.startfile(arg),
    
}

with open('patterns.json', 'r') as file:
    patterns = json.load(file)

all_patterns = command_patterns + patterns

for idx, response_pair in enumerate(all_patterns):
    pattern, replies = response_pair
    modified_replies = []
    for reply in replies:
        modified_reply = reply.replace("{chatbot_name}", chatbot_name)
        modified_replies.append(modified_reply)

    all_patterns[idx] = (pattern, modified_replies)

chatbot = Chat(all_patterns, reflections)

while True:
    user_input = get_input(colored("👤You", "blue") + ": ")
    print(colored("👤You", "blue") + ":", colored(user_input, "dark_grey"))

    response = chatbot.respond(user_input)
    
    if response in commands:
        print(f"🖥 {colored_chatbot_name}:", colored(response, attrs=["underline"]))
        commands[response](user_input[9:])
    else:
        print(f"🤖{colored_chatbot_name}:", colored(response, theme["casual"], attrs=["underline"]))

    if any(keyword in user_input.lower() for keyword in ('quit', 'exit', 'bye')):
        break
