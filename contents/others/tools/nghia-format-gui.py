import os
import subprocess
from time import sleep
# prettier --write  file_path
# pip install pyautogui
import pyautogui


def format(directory):
    exclude_dirs = [".git", "node_modules", "__pycache__", "venv", "dist", "build", "versions"]
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            if file.endswith(".py") or file.endswith(".js"):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                subprocess.run(["code", file_path], check=True, shell=True)
                sleep(1)

                if os.name == 'nt':
                    pyautogui.hotkey('alt', 'shift', 'f')
                    pyautogui.hotkey('alt', 'shift', 'o')
                elif os.name == 'posix':
                    pyautogui.hotkey('alt', 'shift', 'o')
                    pyautogui.hotkey('ctrl', 'shift', 'i')
                sleep(1)


if __name__ == "__main__":
    paths = [
        r"C:\Users\vvn20206205\Downloads\Nghia\Git\whynotnghiavu\fis-mini-project-kong-api-gateway",
    ]
    for path in paths:
        format(path)
