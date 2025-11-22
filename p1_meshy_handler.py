# p1_meshy_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/mnt/data/phase1/meshy/"


# Ensure directory exists
def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# -----------------------------------------
# 🔥 Generate 3D asset themes for Meshy AI
# -----------------------------------------
def generate_asset_themes():
    themes = [
        "Futuristic sci-fi weapon", "Cute low-poly animal",
        "Cyberpunk street prop", "Fantasy magic artifact",
        "Medieval house furniture", "Stylized RPG treasure chest",
        "Realistic kitchen utensil", "Gaming chair low-poly",
        "Robot companion unit", "Alien planet rock formation",
        "Stylized potion bottle", "Modern desk accessory"
    ]
    return random.sample(themes, 10)


# -----------------------------------------
# 🔥 3D Model Prompts
# -----------------------------------------
def generate_model_prompt(theme):
    return f"""
Generate a high-quality 3D model of: {theme}.
Style: Clean topology, optimized mesh, professional asset store quality.
Detail: Proper edge flow, accurate silhouette, balanced polycount.
Format: OBJ / FBX
"""


# -----------------------------------------
# 🔥 Texture Prompts
# -----------------------------------------
def generate_texture_prompt(theme):
    return f"""
Create PBR textures for: {theme}.
Include:
- Base color
- Roughness
- Metallic
- Normal map
- Ambient occlusion
Style: Clean, realistic or stylized as per theme.
Resolution: 2K or 4K
"""


# -----------------------------------------
# 🔥 Titles / Descriptions / Tags
# -----------------------------------------
def generate_title(theme):
    return f"{theme.title()} 3D Model (OBJ/FBX)"


def generate_description(theme):
    return f"""
High-quality 3D asset: {theme}.
Perfect for:
• Game development
• Animation
• CGI projects
• VR/AR environments
Includes clean mesh, PBR textures, and optimized topology.
"""


def generate_tags(theme):
    words = theme.lower().split()
    base_tags = [
        "3D model", "PBR", "game asset", "low-poly", "fbx", "obj", "meshy"
    ]
    return list(set(base_tags + words))


# -----------------------------------------
# 🔥 Save output
# -----------------------------------------
def save_output(batch):
    ensure_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = BASE_PATH + f"meshy_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(batch, f, indent=4)

    return file_path


# -----------------------------------------
# 🔥 MAIN HANDLER FUNCTION
# -----------------------------------------
def run_meshy_handler():

    themes = generate_asset_themes()
    assets = []

    for theme in themes:
        assets.append({
            "theme": theme,
            "title": generate_title(theme),
            "description": generate_description(theme),
            "tags": generate_tags(theme),
            "model_prompt": generate_model_prompt(theme),
            "texture_prompt": generate_texture_prompt(theme),
        })

    batch = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "asset_count": len(assets),
        "assets": assets
    }

    file_path = save_output(batch)

    return {
        "status":
        "success",
        "message":
        "Meshy AI asset batch generated.",
        "file":
        file_path,
        "count":
        len(assets),
        "upload_instructions":
        """
1. Paste model_prompt into Meshy.ai → generate 3D model.
2. Paste texture_prompt into Meshy → generate textures.
3. Export in OBJ/FBX.
4. Upload to your Meshy Store manually (platform does not allow automation).
"""
    }


# Debug
if __name__ == "__main__":
    print(run_meshy_handler())
