# p1_youtube_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/mnt/data/phase1/youtube/"


def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ---------------------------------------------
# 🔥 Video Ideas (YouTube Automation Niches)
# ---------------------------------------------
YOUTUBE_TOPICS = [
    "AI tools explained", "Motivation and success", "Financial growth hacks",
    "Business shortcuts", "Passive income strategies",
    "Top 5 apps you should know", "Tech news trends",
    "Daily productivity habits", "Mindset transformation", "Side hustle ideas"
]


# ---------------------------------------------
# 🔥 Generate Title
# ---------------------------------------------
def generate_title(topic):
    templates = [
        "The SECRET Behind {} Nobody Talks About",
        "{} — Explained in 60 Seconds",
        "Stop Ignoring This About {}",
        "{}: The FASTEST Way to Improve Your Life",
        "Why Most People Fail at {}",
        "{} — Do THIS Every Day",
    ]
    return random.choice(templates).format(topic)


# ---------------------------------------------
# 🔥 Generate Script (Short + Powerful)
# ---------------------------------------------
def generate_script(topic):
    return f"""
[HOOK]
Most people completely ignore this about {topic}…

[BODY 1]
But once you understand it, everything changes. 
Here's the truth: most people wait for motivation. Winners create momentum.

[BODY 2]
If you want to grow fast, start applying this today:
1. Keep it simple.
2. Stay consistent.
3. Track your progress.

[BODY 3]
Anyone can improve their {topic} in 30 days with small daily habits.

[ENDING]
Follow for more powerful insights that change your life.
"""


# ---------------------------------------------
# 🔥 Generate Thumbnail Prompt
# ---------------------------------------------
def generate_thumbnail_prompt(title):
    short_title = title[:20]
    return f"Create a high-contrast YouTube thumbnail with bold neon text '{short_title}...'. Dark background, glowing edges, dramatic expression."


# ---------------------------------------------
# 🔥 Generate SEO Description
# ---------------------------------------------
def generate_description(topic):
    return f"""
This video breaks down the most important lessons about {topic}.
If you're trying to improve your life, grow faster, or build success habits,
this 60-second guide will change the way you see things.

Follow for more daily insights.
"""


# ---------------------------------------------
# 🔥 Hashtags
# ---------------------------------------------
def generate_hashtags(topic):
    base = ["#shorts", "#motivation", "#success", "#lifehacks", "#inspiration"]
    topic_tag = "#" + topic.replace(" ", "")
    return base + [topic_tag]


# ---------------------------------------------
# 🔥 Build Batch Output
# ---------------------------------------------
def save_output(batch):
    ensure_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = BASE_PATH + f"youtube_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(batch, f, indent=4)

    return file_path


# ---------------------------------------------
# 🔥 MAIN HANDLER
# ---------------------------------------------
def run_youtube_handler():

    ideas = random.sample(YOUTUBE_TOPICS, 10)
    videos = []

    for topic in ideas:
        title = generate_title(topic)
        videos.append({
            "topic":
            topic,
            "title":
            title,
            "script":
            generate_script(topic),
            "thumbnail_prompt":
            generate_thumbnail_prompt(title),
            "description":
            generate_description(topic),
            "hashtags":
            generate_hashtags(topic),
            "outline": [
                "Hook (0-3 sec)", "Body Part 1 (3-10 sec)",
                "Body Part 2 (10-20 sec)", "Tips (20-40 sec)",
                "End CTA (40-60 sec)"
            ]
        })

    batch = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "video_count": len(videos),
        "videos": videos
    }

    file_path = save_output(batch)

    return {
        "status":
        "success",
        "message":
        "YouTube batch generated.",
        "file":
        file_path,
        "count":
        len(videos),
        "upload_instructions":
        """
YOUTUBE UPLOAD:
1. Record/Generate video using script + outline.
2. Use thumbnail_prompt to generate thumbnail.
3. Paste title, description, hashtags.
4. Upload manually (YouTube does not allow automation).
"""
    }


# Debug
if __name__ == "__main__":
    print(run_youtube_handler())
