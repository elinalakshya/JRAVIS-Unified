# p2_skillshare_handler.py

import os,json,random
from datetime import datetime

BASE_PATH="/mnt/data/phase2/skillshare/"

def ensure_dir(): os.makedirs(BASE_PATH,exist_ok=True)

def generate_course_outlines():
    topics=["AI Tools","Instagram Growth","Productivity Hacks","Freelancing","Branding"]
    res=[]
    for _ in range(8):
        t=random.choice(topics)
        res.append({
            "course_title":f"{t} 2025 Masterclass",
            "modules":[
                "Introduction","Core Lessons","Case Studies","Assignments","Takeaways"
            ],
            "project":"Upload a completed assignment"
        })
    return res

def save_output(r):
    ensure_dir()
    ts=datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = f"{BASE_PATH}skillshare_{ts}.json"
    json.dump(r,open(fp,"w"),indent=4)
    return fp

def run_skillshare_handler():
    r=generate_course_outlines()
    fp=save_output(r)
    return{"status":"success","file":fp,"count":len(r)}
