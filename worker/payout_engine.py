# ============================================
# JRAVIS PAYOUT ENGINE
# Links each stream to PayPal or holds wallet
# ============================================

import logging
import time
import random
import os
from config.settings import PAYPAL_EMAIL
from handlers.payout_handlers import PAYOUT_HANDLERS


def run_payout_checks():
    logging.info("💼 Running payout checks for all platforms")

    for platform, handler in PAYOUT_HANDLERS.items():
        try:
            logging.info(f"🔗 Checking payout for: {platform}")

            # Login
            if not handler.login():
                logging.error(f"❌ Login failed: {platform}")
                continue

            # Check payout options
            info = handler.check_payout_methods()

            if info.get("paypal_supported"):
                logging.info(f"💰 Adding PayPal to {platform}")
                handler.add_paypal(PAYPAL_EMAIL)
            else:
                logging.info(
                    f"⚠️ {platform} does not support PayPal — storing wallet balance"
                )
                handler.save_wallet_balance()

            # Human-like delay
            time.sleep(random.uniform(1.5, 3.0))

        except Exception as e:
            logging.error(f"❌ Error checking payouts for {platform}: {str(e)}")

    logging.info("💚 Completed payout run")
