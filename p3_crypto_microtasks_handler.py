# p3_crypto_microtasks_handler.py

import os, json, random
from datetime import datetime

BASE_PATH = "/mnt/data/phase3/crypto_microtasks/"


def ensure_dir():
    os.makedirs(BASE_PATH, exist_ok=True)


def generate_tasks():
    types = ["Survey", "Small Writing", "Design Microtask", "Data Labeling"]
    out = []

    for _ in range(15):
        t = random.choice(types)
        out.append({
            "task_type": t,
            "avg_earning": "₹20–₹200",
            "difficulty": random.choice(["Easy", "Medium"])
        })
    return out


def save_output(o):
    ensure_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = f"{BASE_PATH}microtasks_{ts}.json"
    json.dump(o, open(fp, "w"), indent=4)
    return fp


def run_crypto_microtasks_handler():
    o = generate_tasks()
    fp = save_output(o)
    return {"status": "success", "file": fp, "count": len(o)}
