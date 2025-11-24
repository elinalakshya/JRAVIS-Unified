import os
import re

ENGINE_FILE = "unified_engine.py"


def extract_handler_functions():
    handlers = {}
    for fname in os.listdir("."):
        if fname.endswith("_handler.py"):
            with open(fname, "r") as f:
                content = f.read()

            # find functions starting with run_
            match = re.findall(r"def\s+(run_[a-zA-Z0-9_]+)\s*\(", content)
            if match:
                handlers[fname] = match[0]  # take first run_* function
    return handlers


def fix_unified_engine(handlers):
    with open(ENGINE_FILE, "r") as f:
        content = f.read()

    new_lines = []
    for line in content.split("\n"):
        if "import run_" in line and "handler" in line:
            # extract module name
            m = re.search(r"from\s+(\S+)\s+import\s+(run_[a-zA-Z0-9_]+)", line)
            if m:
                module = m.group(1)
                expected_func = m.group(2)

                handler_file = f"{module}.py"
                if handler_file in handlers:
                    actual_func = handlers[handler_file]

                    # If names differ → auto alias
                    if actual_func != expected_func:
                        print(
                            f"Fixing import for {module}: {expected_func} → {actual_func}"
                        )
                        line = f"from {module} import {actual_func} as {expected_func}"

        new_lines.append(line)

    with open(ENGINE_FILE, "w") as f:
        f.write("\n".join(new_lines))


def main():
    print("🔍 Scanning handler files...")
    handlers = extract_handler_functions()

    print("🔧 Fixing unified_engine imports...")
    fix_unified_engine(handlers)

    print("✔️ All handler import mismatches fixed successfully.")


if __name__ == "__main__":
    main()
