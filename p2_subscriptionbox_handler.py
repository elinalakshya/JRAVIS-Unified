# p2_subscriptionbox_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/mnt/data/phase2/subscription/"


def ensure_dir():
    os.makedirs(BASE_PATH, exist_ok=True)


def generate_box_items():
    items = [
        "Pens", "Notebooks", "Stickers", "Templates", "Digital Downloads",
        "PDF Packs"
    ]
    box = []
    for _ in range(8):
        box.append({
            "box_name": "Creative Stationery Box",
            "items": random.sample(items, 3),
            "bonus": "Digital Printable Pack"
        })
    return box


def save_output(box):
    ensure_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = f"{BASE_PATH}subbox_{ts}.json"
    with open(fp, "w") as f:
        json.dump(box, f, indent=4)
    return fp


def run_subbox_handler():  # <-- FIXED NAME
    box = generate_box_items()
    fp = save_output(box)
    return {"status": "success", "file": fp, "count": len(box)}
