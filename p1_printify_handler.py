# p1_printify_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/opt/render/project/src/data/phase1/printify/"


def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ---------------------------
# 🔥 Generate 15 Printify Product Ideas
# ---------------------------
def generate_printify_ideas():
    niches = [
        "Motivation", "Fitness", "AI Quotes", "Anime", "Luxury Minimal",
        "Business Mindset", "Travel", "Pet Lovers", "Sarcastic Humor",
        "Love / Couples", "Zodiac Signs", "Gaming", "Study Motivation"
    ]

    product_types = [
        "T-shirt", "Hoodie", "Mug", "Poster", "Phone Case", "Tote Bag",
        "Sticker Pack"
    ]

    ideas = []

    for _ in range(15):
        niche = random.choice(niches)
        prod = random.choice(product_types)
        ideas.append(f"{prod} Design: '{niche}' theme")

    return ideas


# ---------------------------
# 🔥 Generate Printify Titles & Descriptions
# ---------------------------
def generate_titles_descriptions(ideas):
    titles = []
    descriptions = []

    for idea in ideas:
        titles.append(f"{idea} — Trending 2025 Edition")

        descriptions.append(
            f"{idea}.\n\nHigh quality, vibrant colors, perfect for daily use or gifting.\n"
            "Created for Printify automated store uploads.")

    return titles, descriptions


# ---------------------------
# 🔥 Save all generated items
# ---------------------------
def save_output(ideas, titles, descriptions):
    ensure_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    data = {
        "timestamp": timestamp,
        "ideas": ideas,
        "titles": titles,
        "descriptions": descriptions
    }

    file_path = BASE_PATH + f"printify_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return file_path


# ---------------------------
# 🔥 MAIN HANDLER FUNCTION
# ---------------------------
def run_printify_handler():
    ideas = generate_printify_ideas()
    titles, descriptions = generate_titles_descriptions(ideas)

    file_path = save_output(ideas, titles, descriptions)

    return {
        "status":
        "success",
        "message":
        "Printify batch generated",
        "file":
        file_path,
        "count":
        len(ideas),
        "upload_instructions":
        """
1. Open the generated JSON file.
2. Each idea is one product listing.
3. Use title + description for Printify listing.
4. Generate product image in your AI tool.
5. Upload manually to Printify dashboard (automation restricted).
        """
    }


if __name__ == "__main__":
    print(run_printify_handler())
