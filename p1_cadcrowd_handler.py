# p1_cadcrowd_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/mnt/data/phase1/cadcrowd/"


def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ---------------------------
# 🔥 CAD Work Categories
# ---------------------------
def generate_cad_jobs():
    categories = [
        "Product design", "Mechanical part modeling", "3D printable design",
        "Reverse engineering", "Prototype development", "Industrial design",
        "House floor plan", "AutoCAD drafting", "SolidWorks assembly",
        "Fusion360 organic modeling", "Electronics enclosure design",
        "Furniture modeling"
    ]

    job_types = [
        "Full 3D model", "2D technical drawing", "Dimension corrections",
        "3D to 2D conversion", "3D rendering set", "Exploded view model",
        "Parametric model"
    ]

    difficulties = ["Basic", "Intermediate", "Advanced"]

    jobs = []

    for _ in range(10):
        cat = random.choice(categories)
        typ = random.choice(job_types)
        diff = random.choice(difficulties)

        jobs.append({
            "title":
            f"{cat} — {typ}",
            "difficulty":
            diff,
            "details": (f"Create a {typ.lower()} for a {cat.lower()}. "
                        f"Complexity level: {diff}. "
                        "Final files required: STL, STEP, IGES, PNG renders.")
        })

    return jobs


# ---------------------------
# 🔥 Save output JSON
# ---------------------------
def save_output(jobs):
    ensure_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = BASE_PATH + f"cadcrowd_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump({"timestamp": timestamp, "jobs": jobs}, f, indent=4)

    return file_path


# ---------------------------
# 🔥 MAIN HANDLER FUNCTION
# ---------------------------
def run_cadcrowd_handler():
    jobs = generate_cad_jobs()
    file_path = save_output(jobs)

    return {
        "status":
        "success",
        "message":
        "CADCrowd job batch generated",
        "file":
        file_path,
        "count":
        len(jobs),
        "upload_instructions":
        """
1. Open the generated JSON file.
2. Each item is a CAD job brief.
3. Post these as job listings and apply to similar jobs manually.
4. JRAVIS will later auto-write proposals (email side).
        """
    }


if __name__ == "__main__":
    print(run_cadcrowd_handler())
