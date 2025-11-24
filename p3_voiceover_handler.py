# p3_voiceover_handler.py

import os, json, random
from datetime import datetime

BASE_PATH = "/mnt/data/phase3/voiceover/"


def ensure_dir():
    os.makedirs(BASE_PATH, exist_ok=True)


def generate_voice_scripts():
    niches = [
        "Motivation", "Business Advice", "Storytelling", "Calm Voice",
        "Short Ads"
    ]
    out = []

    for _ in range(20):
        n = random.choice(niches)
        out.append({
            "script_title": f"{n} Voice Pack",
            "script":
            f"A powerful {n} style narration script for dubbing videos…",
            "duration": random.randint(10, 40)
        })
    return out


def save_output(x):
    ensure_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = f"{BASE_PATH}voiceover_{ts}.json"
    json.dump(x, open(fp, "w"), indent=4)
    return fp


def run_voiceover_handler():
    x = generate_voice_scripts()
    fp = save_output(x)
    return {"status": "success", "file": fp, "count": len(x)}
