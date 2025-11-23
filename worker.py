#!/usr/bin/env python3
"""
JRAVIS — Background Worker (Unified Micro-Engine Mode)
-----------------------------------------------------

This worker:
 - Loads all 30 micro-handlers (Phase-1, Phase-2, Phase-3)
 - Runs in HUMAN MODE pacing
 - Generates content in ROBO MODE
 - Runs Gmail Auto-Reply engine
 - Supports daily/instant cycle triggers
"""

import time
import random
import logging
from datetime import datetime

# =============================
# Import Gmail Engine
# =============================
from email_auto_reply import process_incoming_emails

# =============================
# Import Micro-Engine Orchestrator
# =============================
from unified_engine import run_all_streams_micro_engine

# =============================
# STARTUP LOG
# =============================
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")

logging.info("💚 JRAVIS Background Worker Started")


# =============================
# HUMAN-MODE DELAYS
# =============================
def human_delay(min_s=1.5, max_s=3.5):
    time.sleep(random.uniform(min_s, max_s))


def long_human_delay(min_s=8, max_s=18):
    time.sleep(random.uniform(min_s, max_s))


# =============================
# MAIN WORKER LOOP
# (Human-like 3-stage cycle)
# =============================
def main_worker_loop():
    while True:
        try:
            logging.info("📧 Checking Gmail (human mode)…")
            process_incoming_emails()
            human_delay()

            logging.info("🌀 Running 30-Stream Micro Engine…")
            run_all_streams_micro_engine()

            logging.info("😴 Human-like long pause before next full cycle")
            long_human_delay()

        except Exception as e:
            logging.error(f"🔥 Worker error: {e}")
            time.sleep(5)


# =============================
# ENTRY POINT
# =============================
if __name__ == "__main__":
    logging.info("🚀 Worker Loop Starting…")
    main_worker_loop()
