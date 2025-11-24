# p1_meshy_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/opt/render/project/src/data/phase1/meshy/"


def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ---------------------------
# 🔥 Generate 3D Model Ideas for Meshy
# ---------------------------
def generate_meshy_ideas():
    categories = [
        "Mascot character", "Cute animal 3D model", "Futuristic gadget",
        "Robot companion", "Fantasy weapon", "Low-poly game asset",
        "Stylized environment prop", "Sci-fi accessory", "Magic object",
        "Toy model"
    ]

    styles = [
        "Pixar-style", "Low-poly", "Realistic", "Cyberpunk", "Minimal smooth",
        "Clay render", "3D printable style"
    ]

    ideas = []

    for _ in range(12):
        cat = random.choice(categories)
        sty = random.choice(styles)
        ideas.append(f"{cat} — {sty} design")

    return ideas


# ---------------------------
# 🔥 Generate Meshy prompt variations
# ---------------------------
def generate_prompts(ideas):
    prompts = []

    for idea in ideas:
        prompts.append(
            f"Create a high-quality 3D model of: {idea}. "
            "Clean geometry, perfect proportions, high-resolution textures, "
            "smooth lighting, suitable for games and animations.")

    return prompts


# ---------------------------
# 🔥 Save output JSON
# ---------------------------
def save_output(ideas, prompts):
    ensure_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    data = {
        "timestamp": timestamp,
        "ideas": ideas,
        "prompts": prompts,
    }

    file_path = BASE_PATH + f"meshy_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return file_path


# ---------------------------
# 🔥 MAIN HANDLER FUNCTION
# ---------------------------
def run_meshy_handler():
    ideas = generate_meshy_ideas()
    prompts = generate_prompts(ideas)

    file_path = save_output(ideas, prompts)

    return {
        "status":
        "success",
        "message":
        "Meshy 3D asset batch generated",
        "file":
        file_path,
        "count":
        len(ideas),
        "upload_instructions":
        """
1. Open the generated JSON file.
2. Each idea is a 3D asset request.
3. Use each 'prompt' directly inside Meshy AI.
4. Export STL/OBJ and upload to asset marketplaces manually.
        """
    }


if __name__ == "__main__":
    print(run_meshy_handler())
