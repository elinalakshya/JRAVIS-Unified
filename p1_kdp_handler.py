# p1_kdp_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/opt/render/project/src/data/phase1/kdp/"


def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ---------------------------
# 🎯 Generate 10 KDP Book Niches (high-demand, low-competition)
# ---------------------------
def generate_kdp_niches():
    niches = [
        "Mindset & Personal Growth",
        "Teen Motivation Workbook",
        "AI for Beginners",
        "Manifestation & Law of Attraction",
        "Small Business Side-Hustle Guide",
        "Anxiety Relief Workbook",
        "Productivity System for Entrepreneurs",
        "Daily Gratitude Journal",
        "Fitness + Habit Tracker",
        "Parenting Hacks for Busy Moms",
    ]
    return random.sample(niches, 10)


# ---------------------------
# 🎯 Title Generator
# ---------------------------
def generate_titles(niches):
    templates = [
        "The Ultimate Guide to {}",
        "{} — A Complete Beginner Handbook",
        "Unlock Your Potential with {}",
        "{}: How to Transform Your Life Fast",
        "{} Workbook: Daily Skill-Building Approach",
        "{} Made Simple (2025 Edition)",
    ]

    titles = []
    for n in niches:
        template = random.choice(templates)
        titles.append(template.format(n))

    return titles


# ---------------------------
# 🎯 Chapter Outline Generator
# ---------------------------
def generate_chapters(title):
    outline = [
        "Introduction — Why This Matters",
        "Core Principles Explained",
        "Step-by-Step Practical Guide",
        "Real Life Examples",
        "Daily / Weekly Action Plan",
        "Common Mistakes to Avoid",
        "Advanced Techniques",
        "Final Summary & Next Steps",
    ]

    return {"title": title, "chapters": outline}


# ---------------------------
# 🎯 Save Output JSON
# ---------------------------
def save_output(niches, titles, outlines):
    ensure_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = BASE_PATH + f"kdp_batch_{timestamp}.json"

    data = {
        "timestamp": timestamp,
        "niches": niches,
        "titles": titles,
        "outlines": outlines
    }

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return file_path


# ---------------------------
# 🎯 MAIN HANDLER FUNCTION
# ---------------------------
def run_kdp_handler():
    niches = generate_kdp_niches()
    titles = generate_titles(niches)

    outlines = []
    for t in titles:
        outlines.append(generate_chapters(t))

    file_path = save_output(niches, titles, outlines)

    return {
        "status":
        "success",
        "message":
        "KDP batch generated successfully",
        "file":
        file_path,
        "count":
        len(titles),
        "instructions":
        """
1. Open the JSON file.
2. Choose 1–3 titles for book publishing.
3. Use the generated outline as your chapter structure.
4. Use any AI writer (ChatGPT / Claude / Gemini) to expand each chapter.
5. Format in Word → Save as PDF → Upload to Amazon KDP manually.
        """
    }


if __name__ == "__main__":
    print(run_kdp_handler())
