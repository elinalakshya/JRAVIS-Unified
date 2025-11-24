# ============================================
# JRAVIS INVOICE EMAIL SENDER
# Sends invoices to your Gmail
# ============================================

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from config.settings import EMAIL_USER, EMAIL_PASS


def send_invoice_email(to_email, subject, body, file_path):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body))

    with open(file_path, "rb") as f:
        part = MIMEApplication(f.read(), Name=file_path)
        part['Content-Disposition'] = f'attachment; filename="{file_path}"'
        msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, to_email, msg.as_string())

    return True
