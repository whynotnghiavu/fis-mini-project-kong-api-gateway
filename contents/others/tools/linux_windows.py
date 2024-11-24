import os
import subprocess
# prettier --write  file_path
# pip install pyautogui


def format(directory):
    exclude_dirs = [".git", "node_modules", "__pycache__", "venv", "dist", "build", "versions"]
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            file_path = os.path.join(root, file)
            print(f"Processing file: {file_path}")
            if os.name == 'nt':
                subprocess.run(
                    ["sed", "-i", r"s/\r$//", file_path],
                    check=True,
                    shell=False
                )


if __name__ == "__main__":
    paths = [
        r"C:\Users\vvn20206205\Downloads\Nghia\Git\whynotnghiavu\fis-mini-project-kong-api-gateway",
    ]
    for path in paths:
        format(path)
