# p1_shopify_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/opt/render/project/src/data/phase1/shopify/"


def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ---------------------------
# 🛍️ DIGITAL PRODUCT NICHES
# ---------------------------
def generate_product_niches():
    niches = [
        "Canva Templates",
        "Instagram Post Packs",
        "Ebook Templates",
        "Resume / CV Templates",
        "Business Planner",
        "Financial Budget Sheets",
        "Social Media Growth Guides",
        "AI Prompt Packs",
        "Digital Stickers",
        "Printable Journals",
        "Fitness Trackers",
        "SEO Workbook",
    ]
    return random.sample(niches, 10)


# ---------------------------
# 🛍️ PRODUCT TITLE GENERATOR
# ---------------------------
def generate_product_titles(niches):
    templates = [
        "{} Mega Pack (Editable)",
        "{} Bundle — Viral + Trending",
        "{} (PRO Edition)",
        "{} Toolkit for Entrepreneurs",
        "{} System — 2025 Edition",
        "{} Digital Pack (Instant Download)",
    ]

    titles = []

    for n in niches:
        template = random.choice(templates)
        titles.append(template.format(n))

    return titles


# ---------------------------
# 🛍️ PRODUCT DESCRIPTION GENERATOR
# ---------------------------
def generate_descriptions(titles):
    descriptions = []
    for t in titles:
        desc = f"""
Introducing the **{t}** — a powerful digital bundle designed for creators,
entrepreneurs, and business owners.

✔ Fully editable  
✔ Instant download  
✔ Designed for Shopify / Etsy / Creative Market  
✔ High-demand niche product  
✔ Scalable for passive income  

Perfect for selling across 20+ global digital platforms.

"""
        descriptions.append(desc.strip())

    return descriptions


# ---------------------------
# 🛍️ THUMBNAIL PROMPTS
# ---------------------------
def generate_thumbnail_prompts(titles):
    prompts = []

    for t in titles:
        prompts.append(
            f"High-quality digital product thumbnail, modern flat lay, clean white background, bold pastel accents. Include text: '{t}'."
        )

    return prompts


# ---------------------------
# 🛍️ SAVE OUTPUT JSON
# ---------------------------
def save_output(niches, titles, descriptions, thumbnails):
    ensure_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    data = {
        "timestamp": timestamp,
        "niches": niches,
        "titles": titles,
        "descriptions": descriptions,
        "thumbnails": thumbnails,
    }

    file_path = BASE_PATH + f"shopify_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return file_path


# ---------------------------
# 🛍️ MAIN HANDLER (called by JRAVIS)
# ---------------------------
def run_shopify_handler():
    niches = generate_product_niches()
    titles = generate_product_titles(niches)
    descriptions = generate_descriptions(titles)
    thumbnails = generate_thumbnail_prompts(titles)

    file_path = save_output(niches, titles, descriptions, thumbnails)

    return {
        "status":
        "success",
        "message":
        "Shopify Digital Product batch generated",
        "file":
        file_path,
        "count":
        len(titles),
        "instructions":
        """
1. Open the JSON file.
2. Select 1–3 products to publish on Shopify.
3. Use the thumbnail prompt to generate thumbnail images.
4. Upload title + description manually to Shopify.
5. Attach your digital file (PDF, PNG, templates).
        """
    }


if __name__ == "__main__":
    print(run_shopify_handler())
