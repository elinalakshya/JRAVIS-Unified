#!/usr/bin/env python3
"""
JRAVIS BACKGROUND WORKER — Phase-1 Engine
-----------------------------------------
Runs 24/7 on Render.

This worker does:
 - Phase 1 automated batch generation
 - Gmail auto-reply (optional)
 - Safe scheduling
"""

import time
import logging
from datetime import datetime

# ----------------------------------------
#  PHASE-1 HANDLER IMPORTS (Corrected)
# ----------------------------------------
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

# Gmail Auto Reply
from email_auto_reply import process_incoming_emails


# ----------------------------------------
#  MASTER PHASE-1 EXECUTION FUNCTION
# ----------------------------------------
def run_phase1_cycle():
    logging.info("🚀 Phase-1 Cycle Started")

    results = {}

    try:
        results["instagram"] = run_instagram_handler()
        logging.info("Instagram handler finished.")
    except Exception as e:
        results["instagram"] = f"Error: {e}"

    try:
        results["printify"] = run_printify_handler()
        logging.info("Printify handler finished.")
    except Exception as e:
        results["printify"] = f"Error: {e}"

    try:
        results["meshy"] = run_meshy_handler()
        logging.info("Meshy handler finished.")
    except Exception as e:
        results["meshy"] = f"Error: {e}"

    try:
        results["cadcrowd"] = run_cadcrowd_handler()
        logging.info("CadCrowd handler finished.")
    except Exception as e:
        results["cadcrowd"] = f"Error: {e}"

    try:
        results["contentmarket"] = run_contentmarket_handler()
        logging.info("ContentMarket handler finished.")
    except Exception as e:
        results["contentmarket"] = f"Error: {e}"

    try:
        results["youtube"] = run_youtube_handler()
        logging.info("YouTube handler finished.")
    except Exception as e:
        results["youtube"] = f"Error: {e}"

    try:
        results["stock"] = run_stock_handler()
        logging.info("Stock handler finished.")
    except Exception as e:
        results["stock"] = f"Error: {e}"

    try:
        results["kdp"] = run_kdp_handler()
        logging.info("KDP handler finished.")
    except Exception as e:
        results["kdp"] = f"Error: {e}"

    try:
        results["shopify"] = run_shopify_handler()
        logging.info("Shopify handler finished.")
    except Exception as e:
        results["shopify"] = f"Error: {e}"

    try:
        results["stationery"] = run_stationery_handler()
        logging.info("Stationery Export handler finished.")
    except Exception as e:
        results["stationery"] = f"Error: {e}"

    logging.info("🔥 Phase-1 FULL cycle completed.")

    return results


# ----------------------------------------
#  MAIN WORKER LOOP (Runs 24/7)
# ----------------------------------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    logging.info("💚 JRAVIS Background Worker Started")

    while True:
        try:
            # Gmail Auto Reply Engine
            process_incoming_emails()

            # Phase-1 Auto Execution
            run_phase1_cycle()

        except Exception as e:
            logging.error(f"🔥 Worker error: {e}")

        # Wait before the next cycle (20 minutes)
        time.sleep(1200)
