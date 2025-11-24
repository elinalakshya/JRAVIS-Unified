# p2_templates_handler.py

import os, json, random
from datetime import datetime

BASE_PATH = "/mnt/data/phase2/templates/"


def ensure_dir():
    os.makedirs(BASE_PATH, exist_ok=True)


def generate_template_pack():
    categories = [
        "Business Slides", "Resume Layouts", "Canva Templates",
        "Instagram Carousels", "Pitch Decks", "Poster Designs",
        "Ebook Layouts", "Brand Kits", "Minimal UI Kits"
    ]

    outputs = []
    for _ in range(15):
        c = random.choice(categories)
        outputs.append({
            "title":
            f"{c} — Premium Editable Template",
            "description":
            f"A fully editable {c} template pack. Unique, clean, viral-friendly.",
            "tags": [c.lower(), "editable", "modern", "professional"]
        })

    return outputs


def save_output(data):
    ensure_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = f"{BASE_PATH}templates_{ts}.json"
    json.dump(data, open(fp, "w"), indent=4)
    return fp


def run_template_handler():
    data = generate_template_pack()
    fp = save_output(data)
    return {"status": "success", "file": fp, "count": len(data)}
