import os
import re

TARGET_EXTENSIONS = [".py"]


def fix_file(path):
    with open(path, "r") as f:
        content = f.read()

    # Remove escaped quotes " → "
    new_content = content.replace(r'"', '"')

    # Fix escaped curly braces { → {
    new_content = new_content.replace(r"{", "{").replace(r"}", "}")

    # Fix escaped single quotes ' → '
    new_content = new_content.replace(r"'", "'")

    # Optional: clean fp= f"" spacing
    new_content = re.sub(r"fp\s*=\s*f"(.+?)"", r'fp = f"\1"', new_content)

    if new_content != content:
        with open(path, "w") as f:
            f.write(new_content)
        print(f"Fixed: {path}")


def walk_and_fix(root):
    for subdir, dirs, files in os.walk(root):
        for file in files:
            if any(file.endswith(ext) for ext in TARGET_EXTENSIONS):
                fix_file(os.path.join(subdir, file))


if __name__ == "__main__":
    print("🚀 Running global Python cleaner...")
    walk_and_fix(".")
    print("✔️ Cleaning complete.")
