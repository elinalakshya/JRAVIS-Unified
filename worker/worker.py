# ============================================
# JRAVIS WORKER (Unified Repo - Option A)
# Handles 30-stream automation + payout engine
# ============================================
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import time
import random
import logging
from unified_engine import run_all_streams
from payout_engine import run_payout_checks
from config.settings import HUMAN_MODE

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [INFO] %(message)s")


def worker_loop():
    logging.info("💚 JRAVIS Unified Worker Started")

    while True:
        # -------------------------------
        # 1. Run the 30-stream engine
        # -------------------------------
        logging.info("🌀 Running 30-Stream Engine…")
        run_all_streams()

        # -------------------------------
        # 2. Run payout checks
        # -------------------------------
        logging.info("💰 Checking payout status…")
        run_payout_checks()

        # -------------------------------
        # 3. Human-like delay
        # -------------------------------
        if HUMAN_MODE:
            sleep_time = random.uniform(60, 120)
        else:
            sleep_time = 10

        logging.info(f"😴 Pausing {sleep_time:.1f} sec (human mode)")
        time.sleep(sleep_time)


if __name__ == "__main__":
    worker_loop()
