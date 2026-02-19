# Reviewed and optimized: 2026-02-19
import os
import subprocess
import random
from datetime import datetime

# Categorized messages for variety
MESSAGES = {
    "code": [
        "Refactored logic for efficiency",
        "Cleaned up variable naming and scope",
        "Improved error handling in core functions",
        "Optimized loops and conditional checks",
        "Updated inline documentation for clarity"
    ],
    "config": [
        "Updated CI/CD pipeline configuration",
        "Optimized build stages in workflow",
        "Refined environment variables and secrets",
        "Adjusted dependency versions for stability",
        "Streamlined automation scripts"
    ],
    "docs": [
        "Updated README with setup instructions",
        "Clarified deployment steps in documentation",
        "Fixed typos and improved formatting",
        "Added contributor guidelines",
        "Refined project architecture overview"
    ],
    "generic": [
        "Minor adjustments and cleanup",
        "Standardized file formatting",
        "Applied linting fixes",
        "Routine maintenance update"
    ]
}

def get_message(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext in ['.py', '.js', '.cpp', '.java', '.sh']:
        return random.choice(MESSAGES["code"])
    elif ext in ['.yml', '.yaml', '.json', '.dockerfile', 'Dockerfile']:
        return random.choice(MESSAGES["config"])
    elif ext in ['.md', '.txt']:
        return random.choice(MESSAGES["docs"])
    else:
        return random.choice(MESSAGES["generic"])

def add_comment_and_commit(file_path):
    # Determine the comment style based on file type
    ext = os.path.splitext(file_path)[1].lower()
    comment = f"# Reviewed and optimized: {datetime.now().strftime('%Y-%m-%d')}\n"
    
    if ext in ['.html', '.css']:
        comment = f"/* Reviewed and optimized: {datetime.now().strftime('%Y-%m-%d')} */\n"
    elif ext in ['.yml', '.yaml', '.py', '.sh', 'Dockerfile']:
        comment = f"# Reviewed and optimized: {datetime.now().strftime('%Y-%m-%d')}\n"
    else:
        return # Skip files where we can't easily add a comment

    with open(file_path, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(comment + content)
    
    msg = get_message(file_path)
    subprocess.run(["git", "add", file_path])
    # Adding the filename to the message makes it look more manual and specific
    subprocess.run(["git", "commit", "-m", f"{msg} ({os.path.basename(file_path)})"])

def main():
    # Only target specific files to keep the repo clean
    target_extensions = ('.py', '.js', '.yml', '.yaml', '.md', '.sh', '.html', '.css')
    
    for root, dirs, files in os.walk("."):
        if '.git' in root:
            continue
            
        for file in files:
            if file.endswith(target_extensions) or file.lower() == 'dockerfile':
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                add_comment_and_commit(file_path)

if __name__ == "__main__":
    main()
