# ========================================
# JRAVIS CONFIG SETTINGS
# Unified Configuration (Option A)
# All sensitive values are stored in secrets.env
# ========================================

import os

# ---- PAYPAL ----
PAYPAL_EMAIL = os.getenv("PAYPAL_EMAIL", "")
PAYPAL_CURRENCY = "USD"

# ---- JRAVIS MASTER SETTINGS ----
JRAVIS_MODE = os.getenv("JRAVIS_MODE", "production")  # production / dev
LOCK_CODE = os.getenv("LOCK_CODE", "0000")  # email locking

# ---- EMAIL ----
EMAIL_USER = os.getenv("EMAIL_USER", "")
EMAIL_PASS = os.getenv("EMAIL_PASS", "")
DAILY_REPORT_TIME = "10:00"
WEEKLY_REPORT_TIME = "00:00"

# ---- STORAGE ----
OUTPUT_DIR = "./data/outputs/"
INVOICE_DIR = "./data/invoices/"
REPORT_DIR = "./data/reports/"

# ---- GENERAL ----
HUMAN_MODE = True
DEBUG_LOGS = False

# ---- JRAVIS VERSION ----
JRAVIS_VERSION = "3.0 Unified Repo"
