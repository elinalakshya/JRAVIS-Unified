# p1_queue_engine.py

import json
import time
from datetime import datetime

# Importing all 10 handlers
from p1_instagram_handler import run_instagram_handler
from p1_printify_handler import run_printify_handler
from p1_meshy_handler import run_meshy_handler
from p1_cadcrowd_handler import run_cadcrowd_handler
from p1_contentmarket_handler import run_contentmarket_handler
from p1_youtube_handler import run_youtube_handler
from p1_stock_handler import run_stock_handler
from p1_kdp_handler import run_kdp_handler
from p1_shopify_handler import run_shopify_handler
from p1_stationery_handler import run_stationery_handler

# ============================================================
#            PHASE-1 QUEUE ENGINE (FULL POWER MODE)
# ============================================================

CONTENT_QUEUE = []
UPLOAD_QUEUE = []
METADATA_QUEUE = []
EXPORT_QUEUE = []
ERROR_QUEUE = []


# -----------------------------
# Helper to log errors
# -----------------------------
def log_error(stream, error):
    ERROR_QUEUE.append({
        "stream": stream,
        "error": str(error),
        "time": datetime.now().isoformat()
    })


# -----------------------------
# Process a handler safely
# -----------------------------
def safe_run(handler, stream_name):
    try:
        result = handler()
        CONTENT_QUEUE.append({
            "stream": stream_name,
            "file": result["file"],
            "count": result["count"],
            "timestamp": datetime.now().isoformat()
        })
        return result
    except Exception as e:
        log_error(stream_name, e)
        return None


# ============================================================
#             MAIN PHASE-1 FULL-POWER CYCLE
# ============================================================


def run_phase1_cycle():

    print("\n🔥 Running Phase-1 FULL POWER Cycle...\n")

    # ---------------- RUN ALL 10 STREAM HANDLERS ----------------
    streams = {
        "instagram": run_instagram_handler,
        "printify": run_printify_handler,
        "meshy": run_meshy_handler,
        "cadcrowd": run_cadcrowd_handler,
        "content_market": run_contentmarket_handler,
        "youtube": run_youtube_handler,
        "stock": run_stock_handler,
        "kdp": run_kdp_handler,
        "shopify": run_shopify_handler,
        "stationery": run_stationery_handler
    }

    results = {}

    for name, handler in streams.items():
        print(f"▶ Generating: {name}...")
        result = safe_run(handler, name)
        results[name] = result
        print(f"✔ Completed: {name}")

    # ============================================================
    #               BUILD UPLOAD QUEUE
    # ============================================================
    for stream, data in results.items():
        if data:
            UPLOAD_QUEUE.append({
                "stream": stream,
                "file": data["file"],
                "instructions": data["upload_instructions"],
                "count": data["count"]
            })

    # ============================================================
    #               BUILD METADATA QUEUE
    # ============================================================
    for stream, data in results.items():
        if data:
            METADATA_QUEUE.append({
                "stream": stream,
                "timestamp": datetime.now().isoformat(),
                "file": data["file"],
            })

    # ============================================================
    #              BUILD EXPORT QUEUE (KDP + Stationery + Printify)
    # ============================================================
    for key in ["kdp", "stationery", "printify"]:
        if results.get(key):
            EXPORT_QUEUE.append({"stream": key, "file": results[key]["file"]})

    # ============================================================
    #              CREATE DAILY UPLOAD PACK JSON
    # ============================================================
    daily_pack = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "upload_queue": UPLOAD_QUEUE,
        "metadata_queue": METADATA_QUEUE,
        "export_queue": EXPORT_QUEUE,
        "errors": ERROR_QUEUE
    }

    pack_path = f"/opt/render/project/src/data/phase1/daypack_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(pack_path, "w") as f:
        json.dump(daily_pack, f, indent=4)

    print("\n🔥 DAILY UPLOAD PACK CREATED at:")
    print(pack_path)

    return {
        "status": "success",
        "pack_file": pack_path,
        "upload_items": len(UPLOAD_QUEUE),
        "errors": len(ERROR_QUEUE)
    }


# ============================================================
#         PHASE-1 ACTIVATOR (CALLED FROM main.py)
# ============================================================


def activate_phase1_fullpower_cycle():
    print("\n🚀 JRAVIS Phase-1 Full-Power Execution Started...\n")

    result = run_phase1_cycle()

    print("\n🚀 Phase-1 Cycle Completed.")
    print(f"Total Upload Items: {result['upload_items']}")
    print(f"Errors Logged: {result['errors']}")

    return result


# Standalone debugging
if __name__ == "__main__":
    activate_phase1_fullpower_cycle()
