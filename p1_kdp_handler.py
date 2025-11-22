# p1_kdp_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/mnt/data/phase1/kdp/"


def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ----------------------------------------------
# 🔥 Book Niches (High Demand 2025)
# ----------------------------------------------
KDP_NICHES = [
    "Daily Productivity Journal", "Motivational Quote Book",
    "Gratitude Journal", "Kids Activity Book", "Adult Coloring Book",
    "Fitness Tracker Planner", "Budget Planner", "Goal Setting Workbook",
    "Mindfulness Journal", "Affirmation Notebook"
]


# ----------------------------------------------
# 🔥 Title Generator
# ----------------------------------------------
def generate_title(niche):
    templates = [
        "{} — Improve Your Daily Life", "{} — 30 Day Guide",
        "{} for Busy People", "{}: A Simple System", "{} Workbook",
        "{} for Beginners"
    ]
    return random.choice(templates).format(niche)


# ----------------------------------------------
# 🔥 Subtitle Generator
# ----------------------------------------------
def generate_subtitle(niche):
    return f"A guided {niche.lower()} designed for clarity, growth, and self-improvement."


# ----------------------------------------------
# 🔥 Description
# ----------------------------------------------
def generate_description(niche):
    return f"""
Unlock the power of {niche.lower()} with this professionally designed book.
Whether you're a beginner or experienced, this guide will help you stay
consistent, motivated, and inspired each day.

Perfect for:
• Personal growth  
• Productivity  
• Stress relief  
• Creativity  

Start your journey today!
"""


# ----------------------------------------------
# 🔥 7 Keyword Slots
# ----------------------------------------------
def generate_keywords(niche):
    base = [
        "journal", "planner", "notebook", "guide", "self improvement",
        "daily growth"
    ]
    niche_words = niche.lower().split()
    return list(set(base + niche_words))[:7]


# ----------------------------------------------
# 🔥 Categories (BISAC / KDP)
# ----------------------------------------------
def generate_categories():
    return [
        random.choice([
            "Self-Help / Personal Growth", "Body, Mind & Spirit / Inspiration",
            "Crafts & Hobbies / General"
        ]),
        random.choice([
            "Juvenile / Activity Books", "Health & Fitness / General",
            "Business & Economics / Productivity"
        ])
    ]


# ----------------------------------------------
# 🔥 Interior Prompt Generator
# ----------------------------------------------
def generate_interiors(niche):
    return f"""
Generate a clean, printable interior for: {niche}.
Page size: 6x9 inch
Style: Minimal layout, high contrast, book-ready lines, black & white.
Include 100–120 pages with consistent formatting.

(Example: journal pages, tracking boxes, doodle sections, activity puzzles based on niche.)
"""


# ----------------------------------------------
# 🔥 Cover Prompt Generator
# ----------------------------------------------
def generate_cover_prompt(niche):
    return f"Create a high-quality KDP cover for a {niche}, 6x9 inch, bold typography, minimal clean design, strong contrast."


# ----------------------------------------------
# 🔥 Page Count
# ----------------------------------------------
def generate_page_count():
    return random.choice([100, 120, 150])


# ----------------------------------------------
# 🔥 Save JSON batch
# ----------------------------------------------
def save_output(batch):
    ensure_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = BASE_PATH + f"kdp_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(batch, f, indent=4)

    return file_path


# ----------------------------------------------
# 🔥 MAIN HANDLER
# ----------------------------------------------
def run_kdp_handler():

    niches = random.sample(KDP_NICHES, 8)
    books = []

    for niche in niches:
        books.append({
            "niche": niche,
            "title": generate_title(niche),
            "subtitle": generate_subtitle(niche),
            "description": generate_description(niche),
            "keywords": generate_keywords(niche),
            "categories": generate_categories(),
            "interior_prompt": generate_interiors(niche),
            "cover_prompt": generate_cover_prompt(niche),
            "page_count": generate_page_count()
        })

    batch = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "book_count": len(books),
        "books": books
    }

    file_path = save_output(batch)

    return {
        "status":
        "success",
        "message":
        "KDP batch generated.",
        "file":
        file_path,
        "count":
        len(books),
        "upload_instructions":
        """
KDP UPLOAD:
1. Use interior_prompt → generate interior PDF (100–120 pages).
2. Use cover_prompt → generate front + back cover.
3. Upload interior + cover on KDP manually.
4. Paste title, subtitle, description, keywords.
5. Choose generated categories.
6. Publish (takes 72 hours for approval).
"""
    }


# Debug
if __name__ == "__main__":
    print(run_kdp_handler())
