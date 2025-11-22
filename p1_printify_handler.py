# p1_printify_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/mnt/data/phase1/printify/"


# Ensure directory exists
def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ---------------------------
# 🔥 Generate POD design themes
# ---------------------------
def generate_design_themes():
    themes = [
        "minimal quote",
        "retro vintage",
        "bold typography",
        "funny sarcasm",
        "motivation",
        "anime style",
        "aesthetic flowers",
        "geometric modern",
        "streetwear bold",
        "abstract shapes",
    ]
    return random.sample(themes, 10)


# ---------------------------
# 🔥 Design Prompts for AI Images
# ---------------------------
def generate_ai_prompt(theme):
    prompts = {
        "minimal quote":
        "Minimalist text-only design, clean font, soft shadows, modern aesthetic",
        "retro vintage":
        "Retro 80s design, grain texture, neon edges, chrome letters",
        "bold typography":
        "Large block letters, extreme bold, high contrast, edgy layout",
        "funny sarcasm":
        "Funny sarcastic quote, expressive font, playful layout",
        "motivation":
        "Motivational phrase, elegant font pairing, clean contrast",
        "anime style":
        "Anime line-art, vibrant colors, expressive character silhouette",
        "aesthetic flowers":
        "Soft pastel flowers, aesthetic collage, dreamy texture",
        "geometric modern":
        "Geometric abstract shapes, trendy palette, modern balance",
        "streetwear bold":
        "Streetwear vibe, graffiti texture, urban typography",
        "abstract shapes":
        "Colorful abstract pattern, flowing shapes, artistic movement"
    }

    return prompts.get(
        theme, "Modern graphic design, balanced layout, clean aesthetic")


# ---------------------------
# 🔥 Titles / Descriptions
# ---------------------------
def generate_title(theme):
    return f"{theme.title()} Design T-Shirt"


def generate_description(theme):
    return f"""High-quality print featuring a {theme} style design.
• Premium fabric
• Vibrant long-lasting print
• Soft and comfortable
Perfect for daily wear and gifting!"""


# ---------------------------
# 🔥 Tags
# ---------------------------
def generate_tags(theme):
    base_tags = ["tshirt", "unisex", "print", "gift", "premium", "trending"]
    theme_parts = theme.split()
    return list(set(base_tags + theme_parts))


# ---------------------------
# 🔥 Mockup Prompts
# ---------------------------
def generate_mockup_prompt(theme):
    return f"High-quality t-shirt mockup featuring: {theme} design. Studio lighting, clean background."


# ---------------------------
# 🔥 Save batch output
# ---------------------------
def save_output(batch):
    ensure_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = BASE_PATH + f"printify_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(batch, f, indent=4)

    return file_path


# ---------------------------
# 🔥 MAIN HANDLER FUNCTION
# ---------------------------
def run_printify_handler():

    themes = generate_design_themes()
    products = []

    for theme in themes:
        products.append({
            "theme": theme,
            "title": generate_title(theme),
            "description": generate_description(theme),
            "tags": generate_tags(theme),
            "ai_prompt": generate_ai_prompt(theme),
            "mockup_prompt": generate_mockup_prompt(theme)
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
        "Printify batch generated.",
        "file":
        file_path,
        "count":
        len(products),
        "upload_instructions":
        """
1. Generate the design using the AI prompt.
2. Upload design to Printify.
3. Choose product (T-shirt, hoodie, mug, etc.).
4. Use mockup prompt to generate images.
5. Publish manually (Printify does not allow automation).
"""
    }


# Debug
if __name__ == "__main__":
    print(run_printify_handler())
