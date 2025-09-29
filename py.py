import time
from datetime import datetime
import subprocess

file_path = "123/Elysium.txt"

branch = "main"

def update_file():
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(now)
    print(f"Файл обновлён: {now}")
    return now

def git_commit_and_push(commit_message):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", branch], check=True)
      
    except subprocess.CalledProcessError as e:
        print(f"⚠ Ошибка Git: {e}")

while True:
    now = update_file()
    git_commit_and_push(f"Автообновление: {now}")
    time.sleep(300)  
