# p1_stock_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/mnt/data/phase1/stock/"


def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ---------------------------
# 🔥 Generate 25 Stock Image/Video Ideas
# ---------------------------
def generate_stock_ideas():
    categories = [
        "Business people working on laptops", "AI futuristic backgrounds",
        "Minimalist workspace", "City skyline timelapse",
        "Coffee cup aesthetic", "Motivation quotes background",
        "Healthy food flatlay", "Neon cyberpunk streets",
        "Nature forest drone shots", "Water splash slow-motion",
        "Tech code screens aesthetic", "Fitness gym shots",
        "Luxury interior shots", "Digital marketing graphics"
    ]

    styles = [
        "ultra-clean", "professional lighting", "high dynamic range",
        "aesthetic minimal", "cinematic lighting", "flatlay top-view",
        "macro detailed"
    ]

    ideas = []

    for _ in range(25):
        cat = random.choice(categories)
        sty = random.choice(styles)
        ideas.append(f"{cat} — {sty}")

    return ideas


# ---------------------------
# 🔥 Generate Titles + Keywords
# ---------------------------
def generate_titles_keywords(ideas):
    titles = []
    keywords = []

    for idea in ideas:
        titles.append(f"{idea} (Royalty-Free Stock)")

        keyword_list = idea.replace("—", ",").lower().split()
        keywords.append(keyword_list[:12])  # top 12 keywords

    return titles, keywords


# ---------------------------
# 🔥 Save output JSON
# ---------------------------
def save_output(ideas, titles, keywords):
    ensure_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = BASE_PATH + f"stock_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(
            {
                "timestamp": timestamp,
                "ideas": ideas,
                "titles": titles,
                "keywords": keywords
            },
            f,
            indent=4)

    return file_path


# ---------------------------
# 🔥 MAIN HANDLER FUNCTION
# ---------------------------
def run_stock_handler():
    ideas = generate_stock_ideas()
    titles, keywords = generate_titles_keywords(ideas)

    file_path = save_output(ideas, titles, keywords)

    return {
        "status":
        "success",
        "message":
        "Stock content batch generated",
        "file":
        file_path,
        "count":
        len(ideas),
        "upload_instructions":
        """
1. Open the generated JSON file.
2. Each idea is a stock image or video request.
3. Use title + keywords for upload metadata.
4. Create the visuals in your AI tool.
5. Upload manually to Shutterstock / AdobeStock / Pond5.
        """
    }


if __name__ == "__main__":
    print(run_stock_handler())
