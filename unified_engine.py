# unified_engine.py
"""
UNIFIED MICRO-ENGINE FOR ALL 30 STREAMS
---------------------------------------
This file matches EXACTLY with your real filenames from Replit.
It loads all handlers (Phase-1, Phase-2, Phase-3)
and runs them in HUMAN MODE batches.
"""

import time
import random
import logging

# =============================
# IMPORT PHASE-1 HANDLERS (10)
# =============================
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

# =============================
# IMPORT PHASE-2 HANDLERS (10)
# Matching EXACT filenames posted by Boss
# =============================
from p2_aisaas_handler import run_aisaas_handler
from p2_courses_handler import run_courses_handler
from p2_webflow_handler import run_webflow_handler
from p2_templates_handler import run_template_handler
from p2_affiliate_handler import run_affiliate_handler
from p2_printables_handler import run_printables_handler
from p2_newsletter_handler import run_newsletter_handler
from p2_gameassets_handler import run_gameassets_handler
from p2_skillshare_handler import run_skillshare_handler
from p2_subscriptionbox_handler import run_subbox_handler

# =============================
# IMPORT PHASE-3 HANDLERS (10)
# Matching EXACT filenames posted by Boss
# =============================
from p3_resume_handler import run_resume_handler
from p3_plugins_handler import run_plugins_handler
from p3_voiceover_handler import run_voiceover_handler
from p3_musicbeats_handler import run_musicbeats_handler
from p3_worksheets_handler import run_worksheets_handler
from p3_saas_reseller_handler import run_saasreseller_handler
from p3_webautomation_handler import run_scripts_handler
from p3_virtualevents_handler import run_events_handler
from p3_api_marketplace_handler import run_apimarket_handler
from p3_crypto_microtasks_handler import run_cryptomicro_handler

# =============================
# STREAM MAP — FINAL MATCHED LIST OF 30 STREAMS
# =============================
STREAM_MAP = {
    1: run_instagram_handler,
    2: run_printify_handler,
    3: run_meshy_handler,
    4: run_cadcrowd_handler,
    5: run_contentmarket_handler,
    6: run_youtube_handler,
    7: run_stock_handler,
    8: run_kdp_handler,
    9: run_shopify_handler,
    10: run_stationery_handler,
    11: run_aisaas_handler,
    12: run_courses_handler,
    13: run_webflow_handler,
    14: run_template_handler,
    15: run_affiliate_handler,
    16: run_printables_handler,
    17: run_newsletter_handler,
    18: run_gameassets_handler,
    19: run_skillshare_handler,
    20: run_subbox_handler,
    21: run_resume_handler,
    22: run_plugins_handler,
    23: run_voiceover_handler,
    24: run_musicbeats_handler,
    25: run_worksheets_handler,
    26: run_saasreseller_handler,
    27: run_scripts_handler,
    28: run_events_handler,
    29: run_apimarket_handler,
    30: run_cryptomicro_handler,
}


# =============================
# HUMAN-MODE TIMING
# =============================
def human_delay():
    time.sleep(random.uniform(1.5, 4.0))


def human_block_delay():
    time.sleep(random.uniform(8, 18))


# =============================
# RUN SINGLE STREAM
# =============================
def run_stream(stream_id):
    try:
        handler = STREAM_MAP[stream_id]
        logging.info(f"⚡ Running Stream {stream_id}: {handler.__name__}")
        result = handler()
        logging.info(f"✅ Completed Stream {stream_id}")
        return result
    except Exception as e:
        logging.error(f"❌ Error in Stream {stream_id}: {e}")
        return {"status": "error", "stream": stream_id, "error": str(e)}


# =============================
# RUN ALL STREAMS (5 per batch)
# =============================
def run_all_streams_micro_engine():
    logging.info("🚀 MICRO-ENGINE starting (30 streams)")

    batch_size = 5
    for i in range(0, 30, batch_size):
        batch = list(range(i + 1, i + batch_size + 1))
        logging.info(f"👤 HUMAN MODE BATCH → {batch}")

        for stream_id in batch:
            run_stream(stream_id)
            human_delay()

        logging.info("⏸ Human-like break before next batch")
        human_block_delay()

    logging.info("🎉 All 30 streams completed")
    return {"status": "completed", "streams": 30}


if __name__ == "__main__":
    run_all_streams_micro_engine()
