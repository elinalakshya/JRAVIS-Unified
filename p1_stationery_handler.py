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
# 🔥 Stationery Product Types
# -----------------------------------------
PRODUCT_TYPES = [
    "A5 Notebook Cover",
    "A4 Notebook Cover",
    "Hardcover Diary Design",
    "Softcover Journal",
    "Daily Planner Template",
    "Weekly Planner Design",
    "Kids Coloring Book Cover",
    "Minimalist Sketchbook Cover",
    "Cute Sticker Sheet",
    "Aesthetic Bookmark Set",
    "Notepad Design",
    "Greetings Card Template",
    "Invitation Card Set",
    "Reward Sticker Sheet",
    "Classroom Poster"
]


# -----------------------------------------
# 🔥 Design Prompt Generator
# -----------------------------------------
def generate_design_prompt(product):
    return f"""
Create a high-resolution print-ready design for: {product}.
Style: Clean, commercial, export-friendly.
Color mode: CMYK.
Resolution: 300 DPI.
Margins: Safe margins included.
Add modern minimalist aesthetic unless product demands theme.
"""


# -----------------------------------------
# 🔥 Export Listing Description
# -----------------------------------------
def generate_listing_description(product):
    return f"""
Premium {product} designed for international stationery buyers.
This product is perfect for wholesalers, distributors, and retail chains.

✔ High-resolution commercial design  
✔ Export-ready format  
✔ Universal global appeal  
✔ Suitable for bulk production  
"""


# -----------------------------------------
# 🔥 Tags for Stationery Market
# -----------------------------------------
def generate_tags(product):
    base = ["stationery", "export", "notebook", "planner", "diary", "design"]
    words = product.lower().split()
    return list(set(base + words))


# -----------------------------------------
# 🔥 SKU Generator
# -----------------------------------------
def generate_sku(product, index):
    code = ''.join(word[0].upper() for word in product.split()[:3])
    return f"{code}-{index:03d}"


# -----------------------------------------
# 🔥 Printing Instructions (for factories)
# -----------------------------------------
def generate_printing_instructions(product):
    return f"""
PRINTING INSTRUCTIONS FOR {product.upper()}:
• 300 DPI CMYK file
• Include 3mm bleed
• Add cutting guides
• High contrast text
• Export PDF/X-1a format
"""


# -----------------------------------------
# 🔥 Save JSON Output
# -----------------------------------------
def save_output(batch):
    ensure_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = BASE_PATH + f"stationery_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(batch, f, indent=4)

    return file_path


# -----------------------------------------
# 🔥 MAIN HANDLER
# -----------------------------------------
def run_stationery_handler():

    selected = random.sample(PRODUCT_TYPES, 15)
    items = []

    for i, product in enumerate(selected, start=1):
        items.append({
            "product_type": product,
            "design_prompt": generate_design_prompt(product),
            "description": generate_listing_description(product),
            "tags": generate_tags(product),
            "sku": generate_sku(product, i),
            "printing_instructions": generate_printing_instructions(product)
        })

    batch = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "product_count": len(items),
        "products": items
    }

    file_path = save_output(batch)

    return {
        "status": "success",
        "message": "Stationery export batch generated.",
        "file": file_path,
        "count": len(items),
        "upload_instructions": """
STATIONERY EXPORT WORKFLOW:
1. Generate designs using 'design_prompt'.
2. Export print files using 'printing_instructions'.
3. Create a combined ZIP folder.
4. Upload to your stationery distributor / marketplace.
"""
    }


# Debug
if __name__ == "__main__":
    print(run_stationery_handler())
