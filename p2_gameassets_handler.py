# p2_gameassets_handler.py

import os,json,random
from datetime import datetime

BASE_PATH="/mnt/data/phase2/gameassets/"

def ensure_dir(): os.makedirs(BASE_PATH,exist_ok=True)

def generate_assets():
    styles=["Pixel","3D","Minimal","Cartoon"]
    res=[]
    for _ in range(20):
        s=random.choice(styles)
        res.append({
            "asset_name":f"{s} Character Pack",
            "format":["PNG","SVG","PSD"],
            "compatible_with":["Unity","Unreal","Godot"]
        })
    return res

def save_output(r):
    ensure_dir()
    ts=datetime.now().strftime("%Y%m%d_%H%M%S")
    fp=f\"{BASE_PATH}gameassets_{ts}.json\"
    json.dump(r,open(fp,\"w\"),indent=4)
    return fp

def run_gameassets_handler():
    r=generate_assets()
    fp=save_output(r)
    return{\"status\":\"success\",\"file\":fp,\"count\":len(r)}
