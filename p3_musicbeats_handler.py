# p3_musicbeats_handler.py

import os, json, random
from datetime import datetime

BASE_PATH = "/mnt/data/phase3/musicbeats/"


def ensure_dir():
    os.makedirs(BASE_PATH, exist_ok=True)


def generate_music_ideas():
    genres = ["LoFi", "Ambient", "Cinematic", "Corporate", "Trap", "Synthwave"]
    out = []

    for _ in range(25):
        g = random.choice(genres)
        out.append({
            "beat_name":
            f"{g} Beat Pack",
            "mood":
            random.choice(["Calm", "Energetic", "Dark", "Happy"]),
            "length":
            random.randint(20, 60)
        })
    return out


def save_output(o):
    ensure_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = f"{BASE_PATH}musicbeats_{ts}.json"
    json.dump(o, open(fp, "w"), indent=4)
    return fp


def run_musicbeats_handler():
    o = generate_music_ideas()
    fp = save_output(o)
    return {"status": "success", "file": fp, "count": len(o)}
