#!/usr/bin/env python3
"""
JRAVIS Automation Engine (worker.py)
------------------------------------
Runs all background tasks:
✓ Gmail auto-reply (AUTO MODE)
✓ Daily Phase-1 content cycle
✓ Daily report email
✓ Weekly report email
✓ Heartbeat logging
✓ Non-blocking infinite scheduler loop
"""

import os
import time
import logging
import schedule
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

# PHASE-1 Queue Engine
from p1_queue_engine import activate_phase1_fullpower_cycle

# Gmail Auto-Reply
from email_auto_reply import process_incoming_emails

# Daily Report System (already built)
from main import orchestrate_and_wait_for_approval

# =====================================================================
# 1️⃣ CONFIG
# =====================================================================
VA_EMAIL = os.getenv("VA_EMAIL", "")
VA_EMAIL_PASS = os.getenv("VA_EMAIL_PASS", "")
REPORT_CODE = os.getenv("REPORT_API_CODE", "2040")
LOCK_CODE = os.getenv("LOCK_CODE", "2040")

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")


# =====================================================================
# 2️⃣ HEARTBEAT
# =====================================================================
def heartbeat():
    logging.info(f"💓 JRAVIS Worker alive at {datetime.now().isoformat()}")


# =====================================================================
# 3️⃣ GMAIL AUTO-REPLY ENGINE (every 10 minutes)
# =====================================================================
def gmail_cycle():
    try:
        result = process_incoming_emails()
        logging.info(f"📧 Gmail cycle: {result}")
    except Exception as e:
        logging.error(f"Gmail error: {e}")


# =====================================================================
# 4️⃣ DAILY PHASE-1 AUTO CYCLE (Your Request: YES)
# =====================================================================
def auto_phase1_cycle():
    logging.info("🚀 Running automatic Phase-1 Full Power Cycle...")
    result = activate_phase1_fullpower_cycle()
    logging.info(f"Phase-1 Auto Cycle Completed: {result}")


# =====================================================================
# 5️⃣ DAILY REPORT (uses your approval system)
# =====================================================================
def daily_report_task():
    logging.info("📄 Creating daily report...")
    today = datetime.now().strftime("%d-%m-%Y")
    orchestrate_and_wait_for_approval(today, LOCK_CODE)
    logging.info("📨 Daily report email sent.")


# =====================================================================
# 6️⃣ WEEKLY REPORT (Sunday auto)
# =====================================================================
def weekly_report_task():
    logging.info("📊 Weekly report triggered...")
    today = datetime.now().strftime("%d-%m-%Y")
    orchestrate_and_wait_for_approval(today, LOCK_CODE)
    logging.info("📬 Weekly report email sent.")


# =====================================================================
# 7️⃣ SCHEDULER SETUP
# =====================================================================

# Heartbeat every 30 minutes
schedule.every(30).minutes.do(heartbeat)

# Gmail every 10 minutes (AUTO mode — as Boss requested)
schedule.every(10).minutes.do(gmail_cycle)

# Phase-1 daily at 10:00 IST (04:30 UTC approx)
schedule.every().day.at("04:30").do(auto_phase1_cycle)

# Daily report at 04:35 UTC (10:05 IST)
schedule.every().day.at("04:35").do(daily_report_task)

# Weekly report (Sunday 00:00 IST)
schedule.every().sunday.at("18:30").do(weekly_report_task)

# =====================================================================
# 8️⃣ MAIN WORKER LOOP (runs forever)
# =====================================================================
if __name__ == "__main__":
    logging.info("🚀 JRAVIS Worker started. Automation online.")

    while True:
        try:
            schedule.run_pending()
        except Exception as e:
            logging.error(f"Scheduler error: {e}")

        time.sleep(5)
