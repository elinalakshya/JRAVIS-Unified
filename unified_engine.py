import time
import random
import logging

# =============================
# IMPORT ALL 30 MICRO-HANDLERS
# (MATCHES EXACTLY YOUR REPLIT FILENAMES)
# =============================

# --- Phase 1 ---
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

# --- Phase 2 (your exact filenames) ---
from p2_templates_handler import run_template_handler  # FIXED
from p2_courses_handler import run_resellcourses_handler  # FIXED
from p2_printables_handler import run_printables_handler
from p2_affiliate_handler import run_affiliate_handler
from p2_aisaas_handler import run_aisaas_handler
from p2_newsletter_handler import run_newsletter_handler
from p2_subscriptionbox_handler import run_subbox_handler  # FIXED
from p2_gameassets_handler import run_gamingassets_handler  # FIXED
from p2_webflow_handler import run_webflow_handler
from p2_skillshare_handler import run_skillshare_handler

# --- Phase 3 (your exact filenames) ---
from p3_saas_reseller_handler import run_saasreseller_handler
from p3_voiceover_handler import run_voiceover_handler
from p3_musicbeats_handler import run_musicbeats_handler
from p3_plugins_handler import run_plugins_handler
from p3_worksheets_handler import run_worksheets_handler
from p3_virtualevents_handler import run_events_handler  # FIXED
from p3_resume_handler import run_resume_handler
from p3_crypto_microtasks_handler import run_cryptomicro_handler  # FIXED
from p3_api_marketplace_handler import run_apimarket_handler  # FIXED
from p3_webautomation_handler import run_scripts_handler  # FIXED

# =============================
# STREAM MAP (30 STREAMS)
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
    11: run_template_handler,
    12: run_resellcourses_handler,
    13: run_printables_handler,
    14: run_affiliate_handler,
    15: run_aisaas_handler,
    16: run_newsletter_handler,
    17: run_subbox_handler,
    18: run_gamingassets_handler,
    19: run_webflow_handler,
    20: run_skillshare_handler,
    21: run_saasreseller_handler,
    22: run_voiceover_handler,
    23: run_musicbeats_handler,
    24: run_scripts_handler,
    25: run_plugins_handler,
    26: run_worksheets_handler,
    27: run_events_handler,
    28: run_resume_handler,
    29: run_cryptomicro_handler,
    30: run_apimarket_handler,
}


# =============================
# HUMAN MODE DELAYS
# =============================
def human_delay():
    time.sleep(random.uniform(1.5, 4.0))


def human_block_delay():
    time.sleep(random.uniform(10, 20))


# =============================
# RUN SINGLE STREAM
# =============================
def run_stream(stream_id):
    try:
        handler = STREAM_MAP[stream_id]
        logging.info(f"⚡ Running Stream {stream_id}: {handler.__name__}")
        result = handler()
        logging.info(f"✅ Stream {stream_id} completed: {result.get('status')}")
        return result
    except Exception as e:
        logging.error(f"❌ Error in stream {stream_id}: {e}")
        return {"status": "error", "stream": stream_id, "error": str(e)}


# =============================
# RUN ALL STREAMS
# =============================
def run_all_streams_micro_engine():
    logging.info("🚀 Starting MICRO-ENGINE mode for all 30 streams")

    batch_size = 5
    for i in range(0, 30, batch_size):
        batch = list(range(i + 1, i + batch_size + 1))
        logging.info(f"👤 HUMAN MODE BATCH → {batch}")

        for stream_id in batch:
            run_stream(stream_id)
            human_delay()

        logging.info("⏸ Human-like break before next batch")
        human_block_delay()

    logging.info("🎉 All 30 micro-engines completed.")
    return {"status": "completed", "mode": "micro_engine", "streams": 30}


if __name__ == "__main__":
    run_all_streams_micro_engine()
