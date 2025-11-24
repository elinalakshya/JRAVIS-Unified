# p3_resume_handler.py

import os, json, random
from datetime import datetime

BASE_PATH = "/mnt/data/phase3/resume/"


def ensure_dir():
    os.makedirs(BASE_PATH, exist_ok=True)


def generate_resume_packs():
    styles = ["Modern", "Minimal", "Corporate", "Creative"]
    res = []

    for _ in range(20):
        s = random.choice(styles)
        res.append({
            "template":
            f"{s} Resume Template",
            "sections":
            ["Summary", "Skills", "Experience", "Projects", "Links"],
            "bonus":
            "Cover Letter Included"
        })
    return res


def save_output(x):
    ensure_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = f"{BASE_PATH}resume_{ts}.json"
    json.dump(x, open(fp, "w"), indent=4)
    return fp


def run_resume_handler():
    x = generate_resume_packs()
    fp = save_output(x)
    return {"status": "success", "file": fp, "count": len(x)}
