# p3_saas_reseller_handler.py

import os, json, random
from datetime import datetime

BASE_PATH = "/opt/render/project/src/data/phase3/saas_reseller/"


def ensure_dir():
    os.makedirs(BASE_PATH, exist_ok=True)


def generate_reseller_packs():
    tools = [
        "AI Resume Tool", "AI Caption Maker", "AI SEO Writer",
        "AI Invoice Generator", "AI Grammar Fixer"
    ]
    packs = []

    for _ in range(12):
        t = random.choice(tools)
        packs.append({
            "tool_name":
            t,
            "reseller_materials": [
                "Landing Page Copy", "Promo Ads Pack", "Email Sequence",
                "Short Video Scripts"
            ],
            "profit_margin":
            "60–80%"
        })

    return packs


def save_output(x):
    ensure_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = f"{BASE_PATH}saas_reseller_{ts}.json"
    json.dump(x, open(fp, "w"), indent=4)
    return fp


def run_saas_reseller_handler():
    x = generate_reseller_packs()
    fp = save_output(x)
    return {"status": "success", "file": fp, "count": len(x)}
