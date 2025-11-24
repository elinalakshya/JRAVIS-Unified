# ============================================
# JRAVIS UNIFIED ENGINE
# Runs all 30 stream handlers
# ============================================

import logging
import random
from handlers import ALL_HANDLERS


def run_all_streams():
    logging.info("🚀 Micro-Engine starting")

    stream_numbers = list(range(1, len(ALL_HANDLERS) + 1))
    batch_size = 5

    # Run streams in human-like chunks
    for i in range(0, len(stream_numbers), batch_size):
        batch = stream_numbers[i:i + batch_size]
        logging.info(f"👤 HUMAN MODE BATCH → {batch}")

        for stream_id in batch:
            handler_name, handler_func = ALL_HANDLERS[stream_id]
            logging.info(f"⚡ Running Stream {stream_id}: {handler_name}")

            try:
                handler_func()
                logging.info(f"✅ Completed Stream {stream_id}")
            except Exception as e:
                logging.error(f"❌ Error in Stream {stream_id}: {str(e)}")

        logging.info("⏸ Human-like break before next batch")
        time_sleep = random.uniform(10, 20)
        logging.info(f"⏸ Sleeping {time_sleep:.1f} sec")
        import time
        time.sleep(time_sleep)
