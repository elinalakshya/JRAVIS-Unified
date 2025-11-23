import os
import smtplib
import ssl
import threading
import time
import pandas as pd
from datetime import datetime
from flask import Flask
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pytz

# Import all connectors
from vabot.phase1_connectors import CONNECTORS

# -----------------------------
# Flask app
# -----------------------------
app = Flask(__name__)

<<<<<<< HEAD

=======
>>>>>>> 3ce708d27c5316766c8a0e3476828ac15a402322
@app.route("/")
def index():
    return "✅ VA Bot is running 24/7 on Render!", 200

<<<<<<< HEAD

=======
>>>>>>> 3ce708d27c5316766c8a0e3476828ac15a402322
@app.route("/health")
def health():
    return "OK", 200

<<<<<<< HEAD

=======
>>>>>>> 3ce708d27c5316766c8a0e3476828ac15a402322
@app.route("/send-report")
def send_report():
    send_daily_report()
    return "Manual report sent ✅", 200

<<<<<<< HEAD

=======
>>>>>>> 3ce708d27c5316766c8a0e3476828ac15a402322
# -----------------------------
# Email Sending Logic
# -----------------------------
def send_daily_report():
    EMAIL = os.getenv("VA_EMAIL")
    APP_PASS = os.getenv("VA_PASSWORD")
    TO_EMAIL = "nrveeresh327@gmail.com"

    if not EMAIL or not APP_PASS:
        print("❌ Missing VA_EMAIL or VA_PASSWORD in environment variables!")
        return

    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    now_str = now.strftime("%d-%m-%Y %I:%M %p IST")

    # Load last log
    log_file = "logs/phase1_log.csv"
    if os.path.exists(log_file):
        log_data = pd.read_csv(log_file).tail(10).to_html(index=False)
    else:
        log_data = "<p>No logs yet.</p>"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"✅ VA Bot Daily Report – {now_str}"
    msg["From"] = EMAIL
    msg["To"] = TO_EMAIL

    text = f"Boss, here’s your daily report at {now_str}."
    html = f"""
    <html>
      <body>
        <h2>✅ VA Bot Daily Report</h2>
        <p>Boss, VA Bot is running 24/7 and executed the workflow.</p>
        <p><b>Latest Logs:</b></p>
        {log_data}
        <p>🚀 Mission 2040 on track.</p>
        <p>- Dhruvayu</p>
      </body>
    </html>
    """

    msg.attach(MIMEText(text, "plain"))
    msg.attach(MIMEText(html, "html"))
<<<<<<< HEAD
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465,
                              context=context) as server:
            server.login(EMAIL, APP_PASS)
            from email.mime.base import MIMEBase
            from email import encoders

            # ✅ Paths to generated reports (update if different)
            summary_path = "reports/daily/summary_report.pdf"
            invoice_path = "reports/daily/invoices.pdf"

            for file_path in [summary_path, invoice_path]:
                if os.path.exists(file_path):
                    with open(file_path, "rb") as f:
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename={os.path.basename(file_path)}")
                    msg.attach(part)
                else:
                    print(f"⚠️ Missing file: {file_path}")
=======

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(EMAIL, APP_PASS)
>>>>>>> 3ce708d27c5316766c8a0e3476828ac15a402322
            server.sendmail(EMAIL, TO_EMAIL, msg.as_string())
        print(f"✅ Daily report email sent successfully at {now_str}")
    except Exception as e:
        print("❌ Error sending daily report:", e)

<<<<<<< HEAD

=======
>>>>>>> 3ce708d27c5316766c8a0e3476828ac15a402322
# -----------------------------
# First Log Confirmation Email
# -----------------------------
def send_first_log_confirmation(timestamp):
    EMAIL = os.getenv("VA_EMAIL")
    APP_PASS = os.getenv("VA_PASSWORD")
    TO_EMAIL = "nrveeresh327@gmail.com"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "✅ VA Bot First Log Confirmation"
    msg["From"] = EMAIL
    msg["To"] = TO_EMAIL

    text = f"Boss, VA Bot has completed its first log cycle at {timestamp}."
    html = f"""
    <html>
      <body>
        <h2>✅ VA Bot First Log Confirmation</h2>
        <p>Boss, the first log cycle is complete at <b>{timestamp}</b>.</p>
        <p>From now on, logs will continue every hour.</p>
        <p>🚀 Mission 2040 on track.</p>
        <p>- Dhruvayu</p>
      </body>
    </html>
    """

    msg.attach(MIMEText(text, "plain"))
    msg.attach(MIMEText(html, "html"))

    try:
        ctx = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as server:
            server.login(EMAIL, APP_PASS)
            server.sendmail(EMAIL, TO_EMAIL, msg.as_string())
        print(f"📧 First log confirmation email sent at {timestamp}")
    except Exception as e:
        print("❌ Error sending first log confirmation:", e)

<<<<<<< HEAD

=======
>>>>>>> 3ce708d27c5316766c8a0e3476828ac15a402322
# -----------------------------
# Real Workflow Runner (Phase 1)
# -----------------------------
def run_phase1_cycle():
    log_file = "logs/phase1_log.csv"
    os.makedirs("logs", exist_ok=True)

    first_run = True  # ✅ Track first log cycle

    while True:
        now = datetime.now(pytz.timezone("Asia/Kolkata"))
        now_str = now.strftime("%d-%m-%Y %I:%M %p IST")

        print(f"🚀 Running Phase 1 API checks at {now_str}...")

        results = []
        for conn in CONNECTORS:
            try:
                raw = conn()
                # Flatten results for cleaner logs
                results.append({
<<<<<<< HEAD
                    "Platform":
                    raw.get("platform", conn.__name__),
                    "Orders":
                    raw.get("orders_yesterday") or raw.get("orders")
                    or raw.get("projects_done") or "-",
                    "Revenue":
                    raw.get("revenue_yesterday")
                    or raw.get("royalties_yesterday")
                    or raw.get("earnings_yesterday") or raw.get("balance")
                    or "-",
                    "Followers":
                    raw.get("followers") or "-",
                    "Subscribers":
                    raw.get("subscribers") if "subscribers" in raw else "-",
                    "Status":
                    raw.get("status") or raw.get("note") or "✅ OK",
                    "Timestamp":
                    now_str
=======
                    "Platform": raw.get("platform", conn.__name__),
                    "Orders": raw.get("orders_yesterday") or raw.get("orders") or raw.get("projects_done") or "-",
                    "Revenue": raw.get("revenue_yesterday") or raw.get("royalties_yesterday") or raw.get("earnings_yesterday") or raw.get("balance") or "-",
                    "Followers": raw.get("followers") or "-",
                    "Subscribers": raw.get("subscribers") if "subscribers" in raw else "-",
                    "Status": raw.get("status") or raw.get("note") or "✅ OK",
                    "Timestamp": now_str
>>>>>>> 3ce708d27c5316766c8a0e3476828ac15a402322
                })
            except Exception as e:
                results.append({
                    "Platform": conn.__name__,
                    "Orders": "-",
                    "Revenue": "-",
                    "Followers": "-",
                    "Subscribers": "-",
                    "Status": f"❌ Error: {e}",
                    "Timestamp": now_str
                })

        df = pd.DataFrame(results)

        if os.path.exists(log_file):
            df.to_csv(log_file, mode="a", header=False, index=False)
        else:
            df.to_csv(log_file, index=False)

        # ✅ Send first log confirmation email only once
        if first_run:
            send_first_log_confirmation(now_str)
            first_run = False

        print(f"✅ Logged results to {log_file}")
        print("⏳ Sleeping for 1 hour...")
        time.sleep(3600)  # 1 hour

<<<<<<< HEAD

=======
>>>>>>> 3ce708d27c5316766c8a0e3476828ac15a402322
# -----------------------------
# App Runner
# -----------------------------
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "flask":
        # Start background workflow thread
        threading.Thread(target=run_phase1_cycle, daemon=True).start()

        port = int(os.environ.get("PORT", 10000))
        print(f"🚀 Starting Flask on port {port}")
        app.run(host="0.0.0.0", port=port)

    else:
        print("🚀 Sending daily report without starting Flask...")
        try:
            send_report()
            print("✅ Daily report sent successfully.")
        except Exception as e:
            print(f"❌ Error while sending report: {e}")
