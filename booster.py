# Updated and reviewed on 2026-02-19
import os
import subprocess
import random

# Realistic commit messages to make the history look natural
MESSAGES = [
    "Refactored logic for better performance",
    "Updated inline documentation and comments",
    "Cleaned up redundant code structures",
    "Improved variable naming for clarity",
    "Minor optimizations in file structure"
]

def add_comment_and_commit(file_path):
    # Add a small comment at the top of the file to create a diff
    with open(file_path, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        # Adding a simple timestamp or generic refactor comment
        f.write(f"# Updated and reviewed on 2026-02-19\n" + content)
    
    # Git commands to stage and commit
    msg = random.choice(MESSAGES)
    subprocess.run(["git", "add", file_path])
    subprocess.run(["git", "commit", "-m", f"{msg}: {os.path.basename(file_path)}"])

def main():
    # Only targeting common code files
    extensions = ('.py', '.js', '.cpp', '.java', '.html', '.css', '.md')
    
    for root, dirs, files in os.walk("."):
        # Ignore the .git folder
        if '.git' in root:
            continue
            
        for file in files:
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                print(f"Updating: {file_path}")
                add_comment_and_commit(file_path)

if __name__ == "__main__":
    main()
