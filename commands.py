import subprocess
import os
import time
import json

from env import CURRENT_OS, PATH

def open_youtube(arg):
    if CURRENT_OS == "Windows":
        os.startfile("https://www.youtube.com")
    elif CURRENT_OS == "Linux":
        subprocess.Popen(["setsid nohup xdg-open https://www.youtube.com >/dev/null 2>&1 &"], shell=True)

def shutdown_computer(arg):
    if CURRENT_OS == "Windows":
        subprocess.run(["shutdown", "/s", "/t", "1800"])
    elif CURRENT_OS == "Linux":
        subprocess.run(["shutdown", "-h", "+30"])
    print('\nYou can abort entering "abort shutdown"\n')

def abort_shutdown(arg):
    if CURRENT_OS == "Windows":
        subprocess.run(["shutdown", "-a"])
    elif CURRENT_OS == "Linux":
        subprocess.run(["shutdown", "-c"])

def open_url(url):
    if CURRENT_OS == "Windows":
        os.startfile(url)
    elif CURRENT_OS == "Linux":
        subprocess.Popen([f"setsid nohup xdg-open {url} >/dev/null 2>&1 &"], shell=True)

def clear_terminal(arg):
    time.sleep(3)
    subprocess.run(['clear'])

def set_chat_separator(new_separator):
    # Read settings from settings.json
    with open(f'{PATH}/settings.json', 'r') as file:
        settings = json.load(file)

    # Modify chat separator setting
    settings['chat_separator'] = new_separator

    # Write updated settings back to settings.json
    with open(f'{PATH}/settings.json', 'w') as file:
        json.dump(settings, file, indent=4)
