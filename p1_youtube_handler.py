# p1_youtube_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/opt/render/project/src/data/phase1/youtube/"


def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ---------------------------
# 🔥 Generate 15 Video Ideas
# ---------------------------
def generate_video_ideas():
    niches = [
        "AI Tools 2025", "Make Money Online", "Productivity",
        "Business Mindset", "Technology Trends", "Motivation", "Career Growth",
        "Side Hustles", "Entrepreneurship", "Finance Tips"
    ]

    templates = [
        "5 Things Nobody Told You About {}", "The Truth About {} in 2025",
        "Stop Doing This If You Want Better {}",
        "How I Use {} to Save 10 Hours/Week",
        "This {} Trick Will Change Your Life", "Why Most People Fail at {}",
        "{} — Explained in 60 Seconds"
    ]

    ideas = []

    for _ in range(15):
        topic = random.choice(niches)
        template = random.choice(templates)
        ideas.append(template.format(topic))

    return ideas


# ---------------------------
# 🔥 Generate YouTube Titles
# ---------------------------
def generate_titles(ideas):
    titles = []
    for idea in ideas:
        titles.append(f"{idea} (Must Watch 2025)")
    return titles


# ---------------------------
# 🔥 Generate Short Scripts (50–80 words)
# ---------------------------
def generate_scripts(ideas):
    scripts = []

    for idea in ideas:
        scripts.append(f"{idea}.\n"
                       "Here's what you need to know:\n"
                       "1. This applies to everyone.\n"
                       "2. Most people ignore it.\n"
                       "3. But the ones who don’t… grow fast.\n\n"
                       "Save this video and take action today.")

    return scripts


# ---------------------------
# 🔥 Thumbnail Prompts
# ---------------------------
def generate_thumbnails(ideas):
    thumbs = []
    for idea in ideas:
        thumbs.append(
            f"Ultra-bold YouTube thumbnail. Big text: '{idea[:15]}...'. "
            "High contrast yellow/black. Shocked face, dramatic lighting, viral style."
        )
    return thumbs


# ---------------------------
# 🔥 Save JSON Output
# ---------------------------
def save_output(ideas, titles, scripts, thumbnails):
    ensure_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = BASE_PATH + f"youtube_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(
            {
                "timestamp": timestamp,
                "ideas": ideas,
                "titles": titles,
                "scripts": scripts,
                "thumbnails": thumbnails
            },
            f,
            indent=4)

    return file_path


# ---------------------------
# 🔥 MAIN HANDLER FUNCTION
# ---------------------------
def run_youtube_handler():
    ideas = generate_video_ideas()
    titles = generate_titles(ideas)
    scripts = generate_scripts(ideas)
    thumbnails = generate_thumbnails(ideas)

    file_path = save_output(ideas, titles, scripts, thumbnails)

    return {
        "status":
        "success",
        "message":
        "YouTube batch generated",
        "file":
        file_path,
        "count":
        len(ideas),
        "upload_instructions":
        """
1. Open the generated JSON file.
2. Each idea = one video.
3. Use script for YouTube shorts.
4. Use title + thumbnail prompt to create thumbnails.
5. Upload manually (platform automation restricted).
        """
    }


if __name__ == "__main__":
    print(run_youtube_handler())
