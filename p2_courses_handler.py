# p2_courses_handler.py

import os, json, random
from datetime import datetime

BASE_PATH = "/mnt/data/phase2/courses/"


def ensure_dir():
    os.makedirs(BASE_PATH, exist_ok=True)


def generate_course_resell_packs():
    niches = [
        "AI Basics", "Productivity", "Time Management", "Freelancing",
        "Design Theory"
    ]
    packs = []

    for _ in range(10):
        n = random.choice(niches)
        packs.append({
            "course_title":
            f"{n} Mastery Guide",
            "sales_copy":
            f"High-value {n} resell course. Clean script + slides + workbook.",
            "bundle": ["Video Scripts", "Slides", "Workbook", "Promo Ads"]
        })

    return packs


def save_output(x):
    ensure_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = f"{BASE_PATH}courses_{ts}.json"
    json.dump(x, open(fp, "w"), indent=4)
    return fp


def run_courses_handler():
    x = generate_course_resell_packs()
    fp = save_output(x)
    return {"status": "success", "file": fp, "count": len(x)}
