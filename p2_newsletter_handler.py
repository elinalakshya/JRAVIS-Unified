# p2_newsletter_handler.py

import os, json, random
from datetime import datetime

BASE_PATH = "/mnt/data/phase2/newsletters/"


def ensure_dir():
    os.makedirs(BASE_PATH, exist_ok=True)


def generate_newsletters():
    topics = [
        "AI Trends 2025",
        "Passive Income Systems",
        "Motivation & Mindset",
        "Digital Products Tips",
        "Scaling Online Income",
        "Automation Tools",
        "Business Strategy",
    ]

    output = []
    for _ in range(10):
        t = random.choice(topics)
        output.append({
            "title": f"{t} — Weekly Deep Insight",
            "body": f"A premium deep-dive newsletter on: {t}. Fully original.",
            "tags": ["newsletter", "automation", "2025",
                     t.lower()]
        })

    return output


def save_output(data):
    ensure_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = f"{BASE_PATH}newsletters_{ts}.json"
    json.dump(data, open(fp, "w"), indent=4)
    return fp


def run_newsletter_handler():
    r = generate_newsletters()
    fp = save_output(r)
    return {"status": "success", "file": fp, "count": len(r)}
