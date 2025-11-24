# p3_worksheets_handler.py

import os, json, random
from datetime import datetime

BASE_PATH = "/opt/render/project/src/data/phase3/worksheets/"


def ensure_dir():
    os.makedirs(BASE_PATH, exist_ok=True)


def generate_worksheet_packs():
    topics = ["Math", "Logic", "English", "Science", "Memory Training"]
    sets = []

    for _ in range(20):
        t = random.choice(topics)
        sets.append({
            "worksheet_name": f"{t} Worksheet Pack",
            "age_group": random.choice(["5-7", "8-10", "10-12"]),
            "pages": random.randint(5, 15)
        })

    return sets


def save_output(x):
    ensure_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = f"{BASE_PATH}worksheets_{ts}.json"
    json.dump(x, open(fp, "w"), indent=4)
    return fp


def run_worksheets_handler():
    x = generate_worksheet_packs()
    fp = save_output(x)
    return {"status": "success", "file": fp, "count": len(x)}
