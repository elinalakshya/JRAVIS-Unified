# p1_contentmarket_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/mnt/data/phase1/content_market/"


def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ----------------------------------------
# 🔥 Product Themes
# ----------------------------------------
def generate_product_themes():
    themes = [
        "Minimalist Instagram Templates", "Modern YouTube Thumbnail Pack",
        "Business Presentation Slides", "Poster & Flyer Bundle",
        "Logo & Branding Kit", "Editable Resume Templates",
        "E-Commerce Product Mockups", "Social Media Icon Set",
        "T-Shirt Vector Pack", "Aesthetic Digital Wallpapers",
        "Business Card Templates", "AI Prompt Template Bundle"
    ]
    return random.sample(themes, 10)


# ----------------------------------------
# 🔥 Title Generator
# ----------------------------------------
def generate_title(theme):
    return f"{theme} — Professional Editable Bundle"


# ----------------------------------------
# 🔥 Description Generator
# ----------------------------------------
def generate_description(theme):
    return f"""
Premium {theme} designed for creators, businesses, designers, and influencers.
Fully editable using Canva, Photoshop, Figma, or Illustrator (depending on bundle type).

Includes:
• Ready-to-use templates
• High-quality layout
• Clean design system
• Fully customizable assets

Perfect for entrepreneurs, marketers, and content creators.
"""


# ----------------------------------------
# 🔥 Tag Generator
# ----------------------------------------
def generate_tags(theme):
    base_tags = [
        "digital_download", "editable", "template", "bundle", "creative_market"
    ]
    theme_tags = [t for t in theme.lower().split() if len(t) > 2]
    return list(set(base_tags + theme_tags))


# ----------------------------------------
# 🔥 Thumbnail Prompt
# ----------------------------------------
def generate_thumbnail_prompt(theme):
    return f"Create a clean, modern thumbnail for a digital product titled '{theme}'. High contrast, minimal design, professional layout."


# ----------------------------------------
# 🔥 Product File Prompt
# ----------------------------------------
def generate_product_prompt(theme):
    return f"""
Generate a complete digital product bundle for: {theme}.
Include:
• Editable source files (PSD / AI / FIG / CANVA)
• JPG/PNG previews
• Organized layers
• 10–50 variations
• High resolution (300 DPI)
"""


# ----------------------------------------
# 🔥 Save Batch Output
# ----------------------------------------
def save_output(batch):
    ensure_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = BASE_PATH + f"content_market_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(batch, f, indent=4)

    return file_path


# ----------------------------------------
# 🔥 MAIN HANDLER
# ----------------------------------------
def run_contentmarket_handler():

    themes = generate_product_themes()
    products = []

    for theme in themes:
        products.append({
            "theme":
            theme,
            "title":
            generate_title(theme),
            "description":
            generate_description(theme),
            "tags":
            generate_tags(theme),
            "thumbnail_prompt":
            generate_thumbnail_prompt(theme),
            "product_prompt":
            generate_product_prompt(theme),
            "category":
            random.choice([
                "Business", "Creative", "Marketing", "Branding", "E-commerce"
            ])
        })

    batch = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "product_count": len(products),
        "products": products
    }

    file_path = save_output(batch)

    return {
        "status":
        "success",
        "message":
        "Content Market batch generated.",
        "file":
        file_path,
        "count":
        len(products),
        "upload_instructions":
        """
CONTENT MARKET UPLOAD:
1. Use product_prompt to generate the full bundle.
2. Use thumbnail_prompt to make 3–5 preview images.
3. Save variations in ZIP.
4. Upload manually to platforms (Creative Market, Gumroad, Etsy Digital), because automation is not allowed.
"""
    }


# Debug
if __name__ == "__main__":
    print(run_contentmarket_handler())
