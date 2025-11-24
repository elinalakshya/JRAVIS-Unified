# p3_virtualevents_handler.py

import os, json, random
from datetime import datetime

BASE_PATH = "/opt/render/project/src/data/phase3/virtualevents/"


def ensure_dir():
    os.makedirs(BASE_PATH, exist_ok=True)


def generate_event_kits():
    niches = [
        "AI Webinar", "Business Bootcamp", "Productivity Class",
        "Motivation Seminar"
    ]
    out = []

    for _ in range(10):
        n = random.choice(niches)
        out.append({
            "event_title":
            f"{n} Kit",
            "assets":
            ["Slides", "Scripts", "Marketing Ads", "Landing Page Copy"],
            "duration":
            "60 minutes"
        })
    return out


def save_output(x):
    ensure_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = f"{BASE_PATH}virtualevents_{ts}.json"
    json.dump(x, open(fp, "w"), indent=4)
    return fp


def run_virtualevents_handler():
    x = generate_event_kits()
    fp = save_output(x)
    return {"status": "success", "file": fp, "count": len(x)}
