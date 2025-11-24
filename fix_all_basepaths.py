import os
import re

# Paths
OLD_PATH = "/opt/render/project/src/data/"
NEW_PATH = "/opt/render/project/src/data/"

def fix_file(path):
    with open(path, "r") as f:
        content = f.read()

    if OLD_PATH in content:
        new_content = content.replace(OLD_PATH, NEW_PATH)

        with open(path, "w") as f:
            f.write(new_content)

        print(f"✔️ Fixed base path in: {path}")


def walk_and_fix(root):
    for subdir, dirs, files in os.walk(root):
        for file in files:
            # Only modify python code files
            if file.endswith(".py"):
                fix_file(os.path.join(subdir, file))


def create_directories():
    base_dir = NEW_PATH
    print("📁 Ensuring data directory exists:", base_dir)
    os.makedirs(base_dir, exist_ok=True)


if __name__ == "__main__":
    print("🔍 Searching for /opt/render/project/src/data/ occurrences...")

    walk_and_fix(".")

    create_directories()

    print("\n🎉 All base paths fixed successfully!")
    print("➡️ /opt/render/project/src/data/  →  /opt/render/project/src/data/")
