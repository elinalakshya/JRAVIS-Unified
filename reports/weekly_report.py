# ============================================
# JRAVIS WEEKLY REPORT GENERATOR (Real Data)
# Runs Every Sunday 12:00 AM IST
# ============================================

import os
import json
from datetime import datetime, timedelta
from config.settings import REPORT_DIR, PAYPAL_EMAIL
from brain.brain import JRAVISBrain
from .invoice_generator import generate_invoice_pdf


def generate_weekly_report():
    brain = JRAVISBrain()
    summary = brain.get_summary()

    # Last 7 days earnings
    earnings = summary.get("earnings", [])
    week_earnings = earnings[-50:]  # safe slice

    # Create report file
    os.makedirs(REPORT_DIR, exist_ok=True)
    filename = f"{REPORT_DIR}/weekly_{datetime.now().strftime('%Y%m%d')}.json"

    report = {
        "week_start":
        (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"),
        "week_end": datetime.now().strftime("%Y-%m-%d"),
        "paypal": PAYPAL_EMAIL,
        "earnings": week_earnings,
        "total_week_earnings": len(week_earnings),
    }

    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    pdf_file = generate_invoice_pdf(
        title="JRAVIS Weekly Report",
        data=report,
        filename=f"{REPORT_DIR}/weekly_{datetime.now().strftime('%Y%m%d')}.pdf"
    )

    return {
        "json_report": filename,
        "pdf_report": pdf_file,
        "status": "completed"
    }


if __name__ == "__main__":
    print(generate_weekly_report())
