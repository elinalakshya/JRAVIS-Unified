# p1_stock_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/mnt/data/phase1/stock/"


def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ---------------------------------------------
# 🔥 Stock Image Prompts
# ---------------------------------------------
def generate_image_prompts():
    themes = [
        "business meeting", "minimal office desk", "financial graph rising",
        "luxury home interior", "fitness workout pose", "healthy food bowl",
        "technology AI chip", "robotic hand touching hologram",
        "sunset time-lapse skyline", "coding laptop setup",
        "travel nature mountains", "abstract neon shapes",
        "cybersecurity lock icon", "creative workspace flatlay",
        "global network connection", "startup brainstorming team",
        "money wealth financial freedom", "digital marketing concept",
        "corporate handshake", "modern home office"
    ]

    prompts = []
    for theme in themes:
        prompts.append(
            f"Ultra-realistic stock photo of {theme}, 8K resolution, cinematic lighting, professional studio look."
        )
    return prompts


# ---------------------------------------------
# 🔥 Stock Video Prompts
# ---------------------------------------------
def generate_video_prompts():
    themes = [
        "looping city skyline", "typing on keyboard",
        "abstract moving background", "financial graph animated",
        "coffee steam slow motion", "neon lines animation",
        "quick time-lapse clouds", "business handshake slow motion",
        "AI futuristic animation", "coding speed visualization"
    ]

    prompts = []
    for theme in themes:
        prompts.append(
            f"4K stock video clip of {theme}, 60fps, smooth motion, cinematic color grading, depth of field."
        )
    return prompts


# ---------------------------------------------
# 🔥 Titles
# ---------------------------------------------
def generate_title(prompt):
    return prompt.split(" of ")[-1].split(",")[0].title()


# ---------------------------------------------
# 🔥 Description
# ---------------------------------------------
def generate_description(prompt):
    return f"""
High-quality stock content: {prompt}.
Perfect for commercial use, YouTube, branding, websites, presentations, and advertising.
"""


# ---------------------------------------------
# 🔥 Tags
# ---------------------------------------------
def generate_tags(prompt):
    words = prompt.lower().split()
    base = ["stock", "photo", "video", "royaltyfree", "professional"]
    return list(set(base + [w for w in words if len(w) > 3]))


# ---------------------------------------------
# 🔥 Save Batch
# ---------------------------------------------
def save_output(batch):
    ensure_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = BASE_PATH + f"stock_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(batch, f, indent=4)

    return file_path


# ---------------------------------------------
# 🔥 MAIN HANDLER
# ---------------------------------------------
def run_stock_handler():

    image_prompts = generate_image_prompts()
    video_prompts = generate_video_prompts()

    items = []

    # Images
    for prompt in image_prompts:
        items.append({
            "type":
            "image",
            "prompt":
            prompt,
            "title":
            generate_title(prompt),
            "description":
            generate_description(prompt),
            "tags":
            generate_tags(prompt),
            "category":
            random.choice(
                ["Business", "Technology", "Nature", "Lifestyle", "Abstract"])
        })

    # Videos
    for prompt in video_prompts:
        items.append({
            "type":
            "video",
            "prompt":
            prompt,
            "title":
            generate_title(prompt),
            "description":
            generate_description(prompt),
            "tags":
            generate_tags(prompt),
            "category":
            random.choice(
                ["Business", "Tech Motion", "Background", "Cinematic"])
        })

    batch = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "image_count": len(image_prompts),
        "video_count": len(video_prompts),
        "total_items": len(items),
        "items": items
    }

    file_path = save_output(batch)

    return {
        "status":
        "success",
        "message":
        "Stock image/video batch generated.",
        "file":
        file_path,
        "count":
        len(items),
        "upload_instructions":
        """
STOCK UPLOAD:
1. Use prompts to generate images/videos using your AI tools.
2. Export images (JPG, PNG) at 4K–8K.
3. Export videos (MP4/Mov) at 4K 60fps.
4. Upload to Shutterstock, Adobe Stock, Pond5, Pixabay, etc.
5. Manual upload required (platform restrictions).
"""
    }


# Debug
if __name__ == "__main__":
    print(run_stock_handler())
