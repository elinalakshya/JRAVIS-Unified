# p1_shopify_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/mnt/data/phase1/shopify/"

def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ---------------------------------------------
# 🔥 Shopify Digital Product Themes
# ---------------------------------------------
SHOPIFY_THEMES = [
    "Digital Planner (GoodNotes/Notability)",
    "Printable Wall Art",
    "Business Branding Kit",
    "Social Media Template Pack",
    "Minimalist Icon Set",
    "Podcast Cover Templates",
    "E-book Template Pack",
    "Fitness & Meal Planner",
    "Wedding Invitation Suite",
    "Canva Instagram Post Bundle",
    "Daily Affirmation Cards",
    "Productivity Dashboard Template"
]


# ---------------------------------------------
# 🔥 Title Generator
# ---------------------------------------------
def generate_title(theme):
    return f"{theme} — Editable Digital Download"


# ---------------------------------------------
# 🔥 Description Generator
# ---------------------------------------------
def generate_description(theme):
    return f"""
This premium {theme} includes everything you need to simplify your daily life,
grow your business, or improve your productivity.

✔ Fully editable  
✔ High-resolution  
✔ Instant digital download  
✔ Perfect for personal or commercial use  

Delivered instantly after purchase.
"""


# ---------------------------------------------
# 🔥 Tag Generator
# ---------------------------------------------
def generate_tags(theme):
    base = ["digital", "template", "download", "editable", "shopify", "printable"]
    theme_words = [w.lower() for w in theme.split() if len(w) > 3]
    return list(set(base + theme_words))


# ---------------------------------------------
# 🔥 Thumbnail Prompt
# ---------------------------------------------
def generate_thumbnail_prompt(theme):
    return (
        f"Create a clean aesthetic Shopify thumbnail for a '{theme}' digital product. "
        "Minimal design, pastel tones, high clarity, professional layout."
    )


# ---------------------------------------------
# 🔥 Digital File Creation Prompt
# ---------------------------------------------
def generate_file_prompt(theme):
    return f"""
Generate the complete digital product bundle for: {theme}.
Include:
• Editable source files (Canva/PSD/Figma)
• Printable PDF version
• High-resolution JPG/PNG previews
• Organized folder structure
"""


# ---------------------------------------------
# 🔥 Category Selector
# ---------------------------------------------
def generate_category():
    return random.choice([
        "Business",
        "Productivity",
        "Design Templates",
        "Lifestyle",
        "Aesthetic Printables",
        "Marketing Resources"
    ])


# ---------------------------------------------
# 🔥 Save Batch
# ---------------------------------------------
def save_output(batch):
    ensure_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = BASE_PATH + f"shopify_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(batch, f, indent=4)

    return file_path


# ---------------------------------------------
# 🔥 MAIN HANDLER
# ---------------------------------------------
def run_shopify_handler():

    themes = random.sample(SHOPIFY_THEMES, 10)
    products = []

    for theme in themes:
        products.append({
            "theme": theme,
            "title": generate_title(theme),
            "description": generate_description(theme),
            "tags": generate_tags(theme),
            "thumbnail_prompt": generate_thumbnail_prompt(theme),
            "file_prompt": generate_file_prompt(theme),
            "category": generate_category()
        })

    batch = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "product_count": len(products),
        "products": products
    }

    file_path = save_output(batch)

    return {
        "status": "success",
        "message": "Shopify digital product batch generated.",
        "file": file_path,
        "count": len(products),
        "upload_instructions": """
SHOPIFY UPLOAD STEPS:
1. Use file_prompt to generate digital files (ZIP recommended).
2. Use thumbnail_prompt for preview images.
3. Add title, description, tags.
4. Set price and publish.
5. Upload manually (Shopify apps prohibit automation).
"""
    }


# Debug
if __name__ == "__main__":
    print(run_shopify_handler())
