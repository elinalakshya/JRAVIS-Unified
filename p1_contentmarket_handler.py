# p1_contentmarket_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/mnt/data/phase1/contentmarket/"


def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ---------------------------
# 🔥 Generate 20 Digital Product Ideas
# ---------------------------
def generate_content_packs():
    product_types = [
        "Canva Template Pack", "Instagram Carousel Pack", "Business Planner",
        "AI Prompt Pack", "Digital Stickers", "Resume Template Set",
        "Brand Identity Kit", "YouTube Thumbnail Pack", "Ebook Template",
        "Notion Dashboard"
    ]

    target_audiences = [
        "Entrepreneurs", "Students", "Content Creators", "Small Businesses",
        "Designers", "Influencers", "Coaches", "Marketing Agencies"
    ]

    packs = []

    for _ in range(20):
        pt = random.choice(product_types)
        ta = random.choice(target_audiences)

        packs.append(f"{pt} for {ta}")

    return packs


# ---------------------------
# 🔥 Generate Description Content
# ---------------------------
def generate_descriptions(packs):
    descs = []
    for p in packs:
        descs.append(f"{p}.\n\nIncludes fully editable templates. "
                     "Optimized for engagement, conversions, and branding.\n"
                     "Ready for upload to CreativeMarket / Envato / Etsy.")
    return descs


# ---------------------------
# 🔥 Save Output JSON
# ---------------------------
def save_output(packs, descriptions):
    ensure_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = BASE_PATH + f"contentmarket_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(
            {
                "timestamp": timestamp,
                "packs": packs,
                "descriptions": descriptions
            },
            f,
            indent=4)

    return file_path


# ---------------------------
# 🔥 MAIN HANDLER FUNCTION
# ---------------------------
def run_contentmarket_handler():
    packs = generate_content_packs()
    descriptions = generate_descriptions(packs)

    file_path = save_output(packs, descriptions)

    return {
        "status":
        "success",
        "message":
        "ContentMarket product batch generated",
        "file":
        file_path,
        "count":
        len(packs),
        "upload_instructions":
        """
1. Open the generated JSON file.
2. Each item is a complete digital product idea.
3. Use description + template prompt to design the actual files.
4. Upload manually to CreativeMarket, Envato, or Etsy.
        """
    }


if __name__ == "__main__":
    print(run_contentmarket_handler())
