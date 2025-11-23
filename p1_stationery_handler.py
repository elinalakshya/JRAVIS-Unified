# p1_stationery_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/mnt/data/phase1/stationery/"


def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# -----------------------------------------
# 📦 GLOBAL STATIONERY EXPORT PRODUCT TYPES
# -----------------------------------------
def generate_product_types():
    products = [
        "Premium A5 Notebooks", "Hardcover Journals", "Sketch Books",
        "Daily Planners", "Budget Planners", "School Geometry Kits",
        "Pen Packs (Black/Blue/Red)", "Highlighter Sets", "Sticky Notes",
        "Art & Craft Packs", "Rulers & Measuring Tools",
        "Office Stationery Combo Kit", "Math Workbook Sets",
        "Handwriting Practice Books", "Kids Colouring Books"
    ]

    return random.sample(products, 10)


# -----------------------------------------
# 📦 EXPORT TITLES
# -----------------------------------------
def generate_export_titles(product_types):
    titles = []
    for p in product_types:
        formatted = f"Wholesale {p} — Export Ready Pack (MOQ 100 Units)"
        titles.append(formatted)
    return titles


# -----------------------------------------
# 📦 EXPORT DESCRIPTION GENERATOR
# -----------------------------------------
def generate_descriptions(titles):
    descriptions = []

    for t in titles:
        desc = f"""
**{t}**

✔ Export quality  
✔ Made in India  
✔ MOQ 100 – 5000 units  
✔ Global compliant packaging  
✔ Fast processing time  
✔ Best for USA, UK, UAE, Europe, Australia  

📦 *Lakshya Stationery Export Line*  
Trusted by international buyers and B2B clients.
"""
        descriptions.append(desc.strip())

    return descriptions


# -----------------------------------------
# 📦 EXPORT PACKAGING & SHIPPING DETAILS
# -----------------------------------------
def generate_packaging_details():
    packaging = [
        "5-layer corrugated box — waterproof packing",
        "Shrink-wrap individual items", "Bubble wrap for fragile sets",
        "Custom logo print available", "Standard export box of 20–100 units",
        "Gross weight per carton: 6–18 kg", "Dispatch within 3–7 business days"
    ]
    return packaging


# -----------------------------------------
# 📦 EXPORT THUMBNAIL AI PROMPTS
# -----------------------------------------
def generate_thumbnail_prompts(titles):
    prompts = []
    for t in titles:
        prompts.append(
            f"High-quality export product photo, white background, modern lighting. Include text overlay: '{t}'. Minimal clean design."
        )
    return prompts


# -----------------------------------------
# 📦 SAVE FINAL OUTPUT
# -----------------------------------------
def save_output(product_types, titles, descriptions, packaging, thumbnails):
    ensure_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    data = {
        "timestamp": timestamp,
        "product_types": product_types,
        "titles": titles,
        "descriptions": descriptions,
        "packaging_details": packaging,
        "thumbnail_prompts": thumbnails
    }

    file_path = BASE_PATH + f"stationery_export_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return file_path


# -----------------------------------------
# 📦 MAIN HANDLER (called by JRAVIS)
# -----------------------------------------
def run_stationery_handler():
    product_types = generate_product_types()
    titles = generate_export_titles(product_types)
    descriptions = generate_descriptions(titles)
    packaging = generate_packaging_details()
    thumbnails = generate_thumbnail_prompts(titles)

    file_path = save_output(product_types, titles, descriptions, packaging,
                            thumbnails)

    return {
        "status":
        "success",
        "message":
        "Stationery Export Pack Generated",
        "file":
        file_path,
        "count":
        len(titles),
        "instructions":
        """
1. Open the JSON file.
2. Each 'title' is 1 export-ready B2B listing.
3. Use the description directly for Alibaba, IndiaMART, Etsy Wholesale, Shopify B2B.
4. Use the thumbnail prompt to generate product photos.
5. Packaging details go into "Export Details" section of your listing.
"""
    }


if __name__ == "__main__":
    print(run_stationery_handler())
