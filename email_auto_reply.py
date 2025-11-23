import base64
import json
import os
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from langdetect import detect

# -----------------------------------------
#  SECRET FILE PATHS FOR RENDER
# -----------------------------------------
CREDENTIALS_FILE = "/etc/secrets/credentials.json"
TOKEN_FILE = "/etc/secrets/token.json"

# Gmail scopes
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]


def get_gmail_service():
    """Load Google OAuth credentials + token.json (auto-refresh)."""

    creds = None

    # Load token.json if exists
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # If no valid token, create a new one using credentials.json
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save updated token.json back into secret directory
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def send_reply(service, sender, subject, body):
    """Send email reply using Gmail API."""

    message = MIMEText(body)
    message["to"] = sender
    message["subject"] = f"Re: {subject}"

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    service.users().messages().send(userId="me", body={"raw": raw}).execute()


def should_reply(subject, body):
    """Only reply to real messages."""

    # Ignore newsletters + promotions
    ignore_words = ["unsubscribe", "no-reply", "newsletter", "promotion"]

    text = (subject + " " + body).lower()
    if any(word in text for word in ignore_words):
        return False

    # Detect language (English only for reply)
    try:
        lang = detect(body)
        if lang != "en":
            return False
    except:
        return False

    return True


def process_incoming_emails():
    """Main Gmail reader + auto-reply module."""
    try:
        service = get_gmail_service()
        results = service.users().messages().list(userId="me",
                                                  labelIds=["INBOX"],
                                                  q="is:unread").execute()

        messages = results.get("messages", [])

        if not messages:
            return

        for msg in messages:
            msg_data = service.users().messages().get(userId="me",
                                                      id=msg["id"]).execute()

            payload = msg_data["payload"]
            headers = payload.get("headers", [])

            sender = subject = body = ""

            for header in headers:
                name = header["name"]
                value = header["value"]

                if name == "From":
                    sender = value
                if name == "Subject":
                    subject = value

            # Extract body
            if "data" in payload["body"]:
                body = base64.urlsafe_b64decode(
                    payload["body"]["data"]).decode("utf-8", errors="ignore")
            else:
                body = "No body"

            # Decide reply
            if should_reply(subject, body):
                reply_text = f"""
Hello,

Thank you for your message.

I have received your email and JRAVIS will respond with the required details shortly.

Best regards,
JRAVIS Auto-Assistant
"""
                send_reply(service, sender, subject, reply_text)

            # Mark message as read
            service.users().messages().modify(userId="me",
                                              id=msg["id"],
                                              body={
                                                  "removeLabelIds": ["UNREAD"]
                                              }).execute()

    except Exception as e:
        print(f"Email engine error: {e}")
