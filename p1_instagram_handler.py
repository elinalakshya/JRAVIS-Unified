# p1_instagram_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/mnt/data/phase1/instagram/"


# Ensure directory exists
def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ---------------------------
# 🔥 Generate 20 viral reel ideas
# ---------------------------
def generate_reel_ideas():
    topics = [
        "AI tips", "Productivity hacks", "Motivation", "Business shortcuts",
        "Passive income insights", "Mindset upgrade", "Tech trends 2025",
        "Scaling online income", "Daily inspiration", "Story + lesson format"
    ]

    templates = [
        "3 Things Nobody Told You About {}",
        "If You're 18–40, Watch This About {}",
        "This 1 Trick Will Change Your {} Forever",
        "Stop Doing This If You Want Better {}",
        "The Fastest Way To Improve Your {}",
        "Most People Fail Because of This — {}",
        "{} — Explained in 10 Seconds",
        "{} — The Secret Nobody Shares",
    ]

    reel_ideas = []

    for i in range(20):
        topic = random.choice(topics)
        template = random.choice(templates)
        reel_ideas.append(template.format(topic))

    return reel_ideas


# ---------------------------
# 🔥 Generate captions
# ---------------------------
def generate_captions(ideas):
    caption_templates = [
        "Here’s the truth ↓\n{}\n\nFollow for daily powerful insights 🔥",
        "{}\n\nIf this helped you, save + share 🔁",
        "{}\n\nYou need to hear this today ⭐",
        "{}\n\nSmall change = Big difference.",
        "{}\n\nFollow us for more daily wisdom.",
    ]

    captions = []
    for idea in ideas:
        template = random.choice(caption_templates)
        captions.append(template.format(idea))

    return captions


# ---------------------------
# 🔥 Generate thumbnail prompts
# ---------------------------
def generate_thumbnail_prompts(ideas):
    prompts = []

    for idea in ideas:
        prompts.append(
            f"Bold motivational typography thumbnail for Instagram reel. Text: '{idea[:20]}...'. Bright neon glow. Black background. High contrast. Viral aesthetic."
        )

    return prompts


# ---------------------------
# 🔥 Save all generated items
# ---------------------------
def save_output(ideas, captions, thumbnails):
    ensure_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    data = {
        "timestamp": timestamp,
        "ideas": ideas,
        "captions": captions,
        "thumbnails": thumbnails
    }

    file_path = BASE_PATH + f"instagram_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return file_path


# ---------------------------
# 🔥 MAIN HANDLER FUNCTION
# Used by JRAVIS Phase-1 Engine
# ---------------------------
def run_instagram_handler():
    ideas = generate_reel_ideas()
    captions = generate_captions(ideas)
    thumbnails = generate_thumbnail_prompts(ideas)

    file_path = save_output(ideas, captions, thumbnails)

    return {
        "status":
        "success",
        "message":
        "Instagram batch generated",
        "file":
        file_path,
        "count":
        len(ideas),
        "upload_instructions":
        """
1. Open the generated JSON file.
2. Each 'idea' is 1 reel.
3. Use the caption text directly for the post.
4. Use the thumbnail prompt to generate the thumbnail in your AI tool.
5. Upload to Instagram manually (platform does not allow automation).
        """
    }


# Debug run
if __name__ == "__main__":
    print(run_instagram_handler())