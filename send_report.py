<<<<<<< HEAD
#!/usr/bin/env python3
import os
import sys
import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from datetime import datetime

from reports.utils_pdf import make_summary_pdf, make_invoice_pdf, encrypt_pdf

MODE = sys.argv[1] if len(sys.argv) > 1 else "daily"

EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
REPORT_TO_EMAIL = os.getenv("REPORT_TO_EMAIL")
LOCK_CODE = os.getenv("LOCK_CODE", "1234")
APP_BASE = os.getenv("APP_BASE", "")


def collect_data(mode):
    now = datetime.utcnow().isoformat()
    summary = {
        "mode": mode,
        "generated_at_utc": now,
        "yesterday_done": "Auto-inspection cycles: 12",
        "today_plan": "Run Phase-1 tests",
        "tomorrow_plan": "Start Phase-2 rollout",
        "total_earnings_so_far": "₹1,23,456"
    }

    invoices = [{
        "id": "INV-01",
        "amount": "₹12,000"
    }, {
        "id": "INV-02",
        "amount": "₹8,000"
    }]

    return summary, invoices


def send_email(mode, summary_pdf, invoice_pdf):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_HOST_USER
    msg["To"] = REPORT_TO_EMAIL
    msg["Subject"] = f"JRAVIS {mode.capitalize()} Report - {datetime.utcnow().date().isoformat()}"

    approval_link = f"{APP_BASE}/approve?mode={mode}&date={datetime.utcnow().date()}"

    msg.attach(
        MIMEText(
            f"""
        <p>Hello Boss,</p>
        <p>Your {mode} report is attached.</p>
        <p><a href="{approval_link}">Click here to approve</a></p>
        <p>Summary PDF is lock protected.</p>
        <p>— JRAVIS</p>
        """, "html"))

    # Attach encrypted summary PDF
    part_sum = MIMEApplication(summary_pdf, Name="summary.pdf")
    part_sum['Content-Disposition'] = 'attachment; filename="summary.pdf"'
    msg.attach(part_sum)

    # Attach invoice PDF
    part_inv = MIMEApplication(invoice_pdf, Name="invoices.pdf")
    part_inv['Content-Disposition'] = 'attachment; filename="invoices.pdf"'
    msg.attach(part_inv)

    # Send through Gmail
    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
        return True
    except Exception as e:
        print("Email sending FAILED:", e)
        return False


if __name__ == "__main__":
    summary, invoices = collect_data(MODE)

    # Build PDFs
    summary_pdf_raw = make_summary_pdf(summary)
    encrypted_summary = encrypt_pdf(summary_pdf_raw, LOCK_CODE)
    invoice_pdf = make_invoice_pdf(invoices)

    ok = send_email(MODE, encrypted_summary, invoice_pdf)

    if not ok:
        sys.exit(1)

    print("Report done.")
=======
# send_report.py
import smtplib, ssl, os, sqlite3, time
from email.message import EmailMessage
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime, timezone, timedelta
from threading import Timer

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
TO_EMAIL = "nrveeresh327@gamil.com"  # as saved

DB = "approvals.db"
LOCK_CODE = os.getenv("LOCK_CODE", "1234")  # set secure in env


def encrypt_pdf(in_path, out_path, password):
    reader = PdfReader(in_path)
    writer = PdfWriter()
    for p in reader.pages:
        writer.add_page(p)
    writer.encrypt(password)
    with open(out_path, "wb") as f:
        writer.write(f)


def send_email_with_approval(summary_pdf_path, invoices_pdf_path, run_id):
    msg = EmailMessage()
    msg["Subject"] = f"{datetime.now().date().isoformat()} summary report"
    msg["From"] = SMTP_USER
    msg["To"] = TO_EMAIL
    # build body with approval link
    approve_link = f"https://your-domain.example/approve?run_id={run_id}"
    body = f"""
Boss — daily summary attached (code-locked).
Click APPROVE to continue: {approve_link}
If no approval in 10 minutes the system will auto-resume.
"""
    msg.set_content(body)
    # attach files
    with open(summary_pdf_path, "rb") as f:
        msg.add_attachment(f.read(),
                           maintype="application",
                           subtype="pdf",
                           filename=os.path.basename(summary_pdf_path))
    with open(invoices_pdf_path, "rb") as f:
        msg.add_attachment(f.read(),
                           maintype="application",
                           subtype="pdf",
                           filename=os.path.basename(invoices_pdf_path))
    # send
    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)


# Approval DB helpers
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS approvals(run_id TEXT PRIMARY KEY, created_at INTEGER, approved INTEGER DEFAULT 0)"
    )
    conn.commit()
    conn.close()


def create_run(run_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        "INSERT OR REPLACE INTO approvals(run_id, created_at, approved) VALUES (?, ?, 0)",
        (run_id, int(time.time())))
    conn.commit()
    conn.close()


def check_approve_and_proceed(run_id, timeout_seconds=600):
    # Wait loop: check DB every 5s up to timeout; if not approved => return False (auto-resume)
    start = time.time()
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    while time.time() - start < timeout_seconds:
        c.execute("SELECT approved FROM approvals WHERE run_id=?", (run_id, ))
        row = c.fetchone()
        if row and row[0] == 1:
            conn.close()
            return True
        time.sleep(5)
    conn.close()
    return False


if __name__ == "__main__":
    init_db()
    run_id = datetime.utcnow().isoformat()
    # example: encrypt summary
    encrypt_pdf("summary_plain.pdf", "summary_locked.pdf", LOCK_CODE)
    create_run(run_id)
    send_email_with_approval("summary_locked.pdf", "invoices.pdf", run_id)
    approved = check_approve_and_proceed(run_id,
                                         timeout_seconds=600)  # 10 minutes
    if approved:
        print("User approved. Proceeding with daily actions.")
    else:
        print("No approval received — auto-resume triggered.")
>>>>>>> 3ce708d27c5316766c8a0e3476828ac15a402322
