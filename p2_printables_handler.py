# p2_printables_handler.py

import os, json, random
from datetime import datetime

BASE_PATH = "/mnt/data/phase2/printables/"


def ensure_dir():
    os.makedirs(BASE_PATH, exist_ok=True)


def generate_printable_sets():
    types = [
        "Planner", "Checklist", "Budget Sheet", "Habit Tracker",
        "Kids Worksheet", "Meal Plan"
    ]
    res = []

    for _ in range(20):
        t = random.choice(types)
        res.append({
            "name": f"{t} Printable Pack",
            "description": f"Unique {t} set for Etsy/Creative Market",
            "pages": random.randint(6, 20)
        })
    return res


def save_output(r):
    ensure_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = f"{BASE_PATH}printables_{ts}.json"
    json.dump(r, open(fp, "w"), indent=4)
    return fp


def run_printables_handler():
    r = generate_printable_sets()
    fp = save_output(r)
    return {"status": "success", "file": fp, "count": len(r)}
