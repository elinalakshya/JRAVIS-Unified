# p2_affiliate_handler.py

import os, json, random
from datetime import datetime

BASE_PATH = "/mnt/data/phase2/affiliate/"


def ensure_dir():
    os.makedirs(BASE_PATH, exist_ok=True)


def generate_affiliate_assets():
    niches = [
        "AI Tools", "Productivity Apps", "Design Tools", "Writing Tools",
        "Marketing Platforms"
    ]
    data = []
    for _ in range(15):
        n = random.choice(niches)
        data.append({
            "topic":
            f"Top 5 {n} You Must Try",
            "short_video_script":
            f"Here are the best {n} for 2025...",
            "blog_outline":
            ["Intro", "Tool List", "Why it Works", "Final CTA"],
            "cta":
            "Use our affiliate link in bio."
        })
    return data


def save_output(d):
    ensure_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = f"{BASE_PATH}affiliate_{ts}.json"
    json.dump(d, open(fp, "w"), indent=4)
    return fp


def run_affiliate_handler():
    d = generate_affiliate_assets()
    fp = save_output(d)
    return {"status": "success", "file": fp, "count": len(d)}
