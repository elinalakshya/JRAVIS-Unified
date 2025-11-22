# p1_cadcrowd_handler.py

import os
import json
import random
from datetime import datetime

BASE_PATH = "/mnt/data/phase1/cadcrowd/"


def ensure_dir():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH, exist_ok=True)


# ----------------------------------------
# 🔥 Generate CAD tasks (2D → 3D conversions)
# ----------------------------------------
def generate_cad_tasks():
    tasks = [
        "Convert 2D mechanical part drawing into parametric 3D model",
        "Create 3D housing for an electronic device based on sketch",
        "Convert floor plan into full 3D architectural model",
        "Reverse engineer a machine bracket into full CAD model",
        "Create technical 3D assembly from reference images",
        "Design a 3D printable prototype from concept sketch",
        "Convert hand-drawn product idea into full 3D model",
        "Generate 3D exploded view from assembly diagram",
        "Transform product blueprint into STL + STEP models",
        "Produce CAD-ready model for vacuum forming mold"
    ]
    return random.sample(tasks, 6)


# ----------------------------------------
# 🔥 Technical description generator
# ----------------------------------------
def generate_technical_description(task):
    return f"""
Technical Work Description:
• Task: {task}
• Workflow:
  1. Review client sketches/blueprints
  2. Extract main dimensions & constraints
  3. Build clean parametric 3D model
  4. Apply material features (fillets, chamfers, ribs)
  5. Export in STEP, STL, OBJ formats
• Delivery:
  - Native CAD + universal formats
  - Fully editable model
  - Clean topology
"""


# ----------------------------------------
# 🔥 Tags & skill keywords
# ----------------------------------------
def generate_tags(task):
    base = [
        "CAD", "3D modeling", "mechanical", "solidworks", "fusion360",
        "engineering"
    ]
    words = task.lower().split()
    return list(set(base + words))


# ----------------------------------------
# 🔥 Submission message for CadCrowd
# ----------------------------------------
def generate_submission_message(task):
    return f"""
Hello! I have completed your task: "{task}".

Deliverables include:
• Fully editable 3D model
• STEP / STL / OBJ formats
• Technical drawing (if requested)
• Clean topology & dimensions matched

Let me know if you need modifications!
"""


# ----------------------------------------
# 🔥 Save JSON batch
# ----------------------------------------
def save_output(batch):
    ensure_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = BASE_PATH + f"cadcrowd_batch_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(batch, f, indent=4)

    return file_path


# ----------------------------------------
# 🔥 MAIN HANDLER
# ----------------------------------------
def run_cadcrowd_handler():

    tasks = generate_cad_tasks()
    items = []

    for t in tasks:
        items.append({
            "task":
            t,
            "technical_description":
            generate_technical_description(t),
            "submission_message":
            generate_submission_message(t),
            "tags":
            generate_tags(t),
            "file_name_instructions":
            f"Name files as: {t[:15].replace(' ', '_')}_v1.step/stl"
        })

    batch = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "task_count": len(items),
        "tasks": items
    }

    file_path = save_output(batch)

    return {
        "status":
        "success",
        "message":
        "CadCrowd task batch generated.",
        "file":
        file_path,
        "count":
        len(items),
        "upload_instructions":
        """
CadCrowd Steps:
1. Choose 1 task from the batch.
2. Create the 3D model in your CAD tool.
3. Export STEP + STL + native file.
4. Paste the submission_message.
5. Upload manually (platform prohibits automation).
"""
    }


# Debug
if __name__ == "__main__":
    print(run_cadcrowd_handler())
