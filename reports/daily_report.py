# ============================================
# JRAVIS DAILY REPORT GENERATOR (Real Data)
# Runs at 10 AM IST
# ============================================

import os
import json
from datetime import datetime
from config.settings import REPORT_DIR, PAYPAL_EMAIL
from brain.brain import JRAVISBrain
from .invoice_generator import generate_invoice_pdf


def generate_daily_report():
    brain = JRAVISBrain()
    summary = brain.get_summary()

    # Extract values
    earnings = summary.get("earnings", [])
    events = summary.get("events", [])

    # Create report file
    os.makedirs(REPORT_DIR, exist_ok=True)
    filename = f"{REPORT_DIR}/daily_{datetime.now().strftime('%Y%m%d')}.json"

    report = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "paypal": PAYPAL_EMAIL,
        "earnings_count": len(earnings),
        "earnings": earnings,
        "events": events,
    }

    # Save JSON version
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    # Generate encrypted PDF invoice bundle
    pdf_file = generate_invoice_pdf(
        title="JRAVIS Daily Report",
        data=report,
        filename=f"{REPORT_DIR}/daily_{datetime.now().strftime('%Y%m%d')}.pdf")

    return {
        "json_report": filename,
        "pdf_report": pdf_file,
        "status": "completed"
    }


if __name__ == "__main__":
    print(generate_daily_report())
