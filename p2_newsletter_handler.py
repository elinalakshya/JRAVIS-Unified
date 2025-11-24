# p2_newsletter_handler.py

import os,json,random
from datetime import datetime

BASE_PATH="/mnt/data/phase2/newsletter/"

def ensure_dir(): os.makedirs(BASE_PATH,exist_ok=True)

def generate_newsletters():
    topics=["AI","Money","Mindset","Business","Productivity"]
    res=[]
    for _ in range(10):
        t=random.choice(topics)
        res.append({
            "title":f"{t} Daily Growth Insights",
            "sections":["Big Idea","Case Study","1-Minute Tip"],
            "ad_slots":random.randint(1,3)
        })
    return res

def save_output(r):
    ensure_dir()
    ts=datetime.now().strftime("%Y%m%d_%H%M%S")
    fp=f\"{BASE_PATH}newsletters_{ts}.json\"
    json.dump(r,open(fp,\"w\"),indent=4)
    return fp

def run_newsletter_handler():
    r=generate_newsletters()
    fp=save_output(r)
    return {\"status\":\"success\",\"file\":fp,\"count\":len(r)}
