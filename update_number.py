#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime

def read_number():
    with open("number.txt", "r") as f:
        return int(f.read().strip())

def write_number(num):
    with open("number.txt", "w") as f:
        f.write(str(num))

def update_readme(number):
    with open("README.md", "r") as f:
        lines = f.readlines()

    with open("README.md", "w") as f:
        for line in lines:
            if line.startswith("Daily Number:"):
                f.write(f"Daily Number: {number}\n")
            else:
                f.write(line)

def git_commit_and_push():
    subprocess.run(["git", "add", "number.txt", "README.md"])
    date = datetime.now().strftime("%Y-%m-%d")
    commit_message = f"Update number: {date}"
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push"])

def main():
    number = read_number() + 1
    write_number(number)
    update_readme(number)
    git_commit_and_push()

if __name__ == "__main__":
    main()
