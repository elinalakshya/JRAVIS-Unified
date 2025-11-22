# email_auto_reply.py
from gmail_service import get_gmail_service
from base64 import urlsafe_b64decode, urlsafe_b64encode
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
from langdetect import detect

# ---------------------------
# 1. PRIORITY SENDER RULES
# ---------------------------
priority_senders = {
    "client": "instant",
    "supplier": "instant",
    "partner": "instant",
    "support": "priority",
    "team": "priority",
    "no-reply": "ignore",
    "notification": "ignore",
    "ads": "ignore",
    "promo": "ignore"
}


def sender_priority(sender):
    sender_lower = sender.lower()
    for key in priority_senders:
        if key in sender_lower:
            return priority_senders[key]
    return "normal"


# ---------------------------
# 2. ATTACHMENT DETECTION
# ---------------------------
def detect_attachments(raw_msg):
    attachments = []
    parts = raw_msg["payload"].get("parts", [])
    for part in parts:
        if part.get("filename"):
            attachments.append(part["filename"])
    return attachments


# ---------------------------
# 3. AUTO ATTACHMENT REPLY (optional)
# ---------------------------
def send_attachment(service, to_email, subject, message_text, file_path):
    message = MIMEMultipart()
    message["to"] = to_email
    message["subject"] = subject

    message.attach(MIMEText(message_text))

    with open(file_path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition",
                        f"attachment; filename={file_path}")
        message.attach(part)

    raw = urlsafe_b64encode(message.as_bytes()).decode()

    service.users().messages().send(userId="me", body={"raw": raw}).execute()


# ---------------------------
# 4. LANGUAGE-BASED REPLIES
# ---------------------------
def language_based_reply(message):
    lang = detect(message)

    replies = {
        "en":
        "Thank you for your email. We received your message and will get back to you shortly.",
        "hi": "धन्यवाद, आपका संदेश प्राप्त हो गया। हम जल्द ही उत्तर देंगे।",
        "kn":
        "ಧನ್ಯವಾದಗಳು, ನಿಮ್ಮ ಸಂದೇಶವನ್ನು ಸ್ವೀಕರಿಸಲಾಗಿದೆ. ಶೀಘ್ರದಲ್ಲೇ ಪ್ರತಿಕ್ರಿಯಿಸುತ್ತೇವೆ.",
        "te": "ధన్యవాదాలు, మీ మెయిల్ అందింది. త్వరలోనే ప్రత్యుత్తరం ఇస్తాం.",
        "ta":
        "நன்றி, உங்கள் மின்னஞ்சல் கிடைத்துள்ளது. விரைவில் பதில் அளிக்கப்படும்.",
        "ar": "شكراً لرسالتك. سنرد عليك قريباً."
    }

    return replies.get(lang, replies["en"])


# ---------------------------
# 5. TONE-BASED REPLY
# ---------------------------
def tone_based_reply(message):
    txt = message.lower()

    if "urgent" in txt or "important" in txt or "asap" in txt:
        return "We received your urgent message and are handling it immediately."

    if "thank" in txt:
        return "You're welcome! Let me know if you need anything else."

    if "?" in txt or "question" in txt:
        return "Thank you for your question. We will respond soon."

    return "Thank you for contacting us."


# ---------------------------
# 6. SMART REQUIRED-ONLY REPLY LOGIC
# ---------------------------
def generate_auto_reply(email_text):
    text = email_text.lower()

    # Ignore junk emails
    ignore_keywords = [
        "unsubscribe", "newsletter", "promotion", "offer", "discount", "otp",
        "verification", "receipt", "invoice", "marketing", "news", "social",
        "notification", "update"
    ]

    if any(k in text for k in ignore_keywords):
        return None

    # Emails requiring reply
    if any(q in text
           for q in ["help", "support", "issue", "problem", "?", "question"]):
        reply = language_based_reply(email_text)
        reply = tone_based_reply(email_text)
        return reply

    return None


# ---------------------------
# 7. AUTO FORWARD IMPORTANT EMAILS
# ---------------------------
def forward_email(service, msg_id, forward_to):
    message = service.users().messages().get(userId="me",
                                             id=msg_id,
                                             format="raw").execute()
    raw_msg = message["raw"]

    forward = {
        "raw": raw_msg,
        "payload": {
            "headers": [{
                "name": "To",
                "value": forward_to
            }]
        }
    }

    service.users().messages().send(userId="me", body=forward).execute()


# ---------------------------
# 8. DAILY SUMMARY REPORT
# ---------------------------
def generate_daily_summary():
    service = get_gmail_service()

    important = service.users().messages().list(
        userId="me", q="label:IMPORTANT newer_than:1d").execute()
    ignored = service.users().messages().list(
        userId="me", q="label:IGNORED newer_than:1d").execute()

    summary = f"""
JRAVIS DAILY EMAIL SUMMARY

Important emails handled: {len(important.get("messages", []))}
Ignored emails archived: {len(ignored.get("messages", []))}
System stable and running.

Timestamp: {datetime.datetime.now()}
"""

    return summary


def send_daily_summary():
    service = get_gmail_service()
    summary = generate_daily_summary()

    msg = MIMEText(summary)
    msg["to"] = "nrveeresh327@gmail.com"
    msg["subject"] = "JRAVIS Daily Email Summary"

    raw = urlsafe_b64encode(msg.as_bytes()).decode()
    service.users().messages().send(userId="me", body={"raw": raw}).execute()


# ---------------------------
# 9. MAIN GMAIL ENGINE
# ---------------------------
def process_incoming_emails():
    service = get_gmail_service()

    results = service.users().messages().list(userId="me",
                                              q="is:unread").execute()
    messages = results.get("messages", [])

    if not messages:
        return "No unread emails."

    for msg in messages:
        msg_id = msg["id"]

        raw_msg = service.users().messages().get(userId="me",
                                                 id=msg_id).execute()

        headers = raw_msg["payload"]["headers"]
        sender = "(Unknown Sender)"
        subject = "(No Subject)"

        for h in headers:
            if h["name"] == "From":
                sender = h["value"]
            if h["name"] == "Subject":
                subject = h["value"]

        # Decode email body
        try:
            body_data = raw_msg["payload"]["parts"][0]["body"]["data"]
        except:
            body_data = raw_msg["payload"]["body"]["data"]

        text = urlsafe_b64decode(body_data).decode("utf-8")

        # Detect attachments
        attachments = detect_attachments(raw_msg)

        # Determine priority
        priority = sender_priority(sender)

        # Auto reply logic
        reply_text = generate_auto_reply(text)

        # AUTO ATTACHMENT reply example (optional)
        if "pricing" in text:
            send_attachment(service, sender, "Pricing",
                            "Attached is the pricing", "pricing.pdf")

        # Send reply if required
        if reply_text:
            msg_ready = MIMEText(reply_text)
            msg_ready["to"] = sender
            msg_ready["subject"] = f"Re: {subject}"

            raw = urlsafe_b64encode(msg_ready.as_bytes()).decode()
            service.users().messages().send(userId="me", body={
                "raw": raw
            }).execute()

            service.users().messages().modify(userId="me",
                                              id=msg_id,
                                              body={
                                                  "addLabelIds": ["IMPORTANT"],
                                                  "removeLabelIds": ["UNREAD"]
                                              }).execute()

            # Forward important emails
            forward_email(service, msg_id, "nrveeresh327@gmail.com")

        else:
            # Archive ignored emails
            service.users().messages().modify(userId="me",
                                              id=msg_id,
                                              body={
                                                  "addLabelIds": ["IGNORED"],
                                                  "removeLabelIds":
                                                  ["UNREAD", "INBOX"]
                                              }).execute()

    return "Processed all emails."
