# ============================================
# JRAVIS INVOICE FETCHER
# Fetches invoices from platforms when supported
# ============================================

import os
from config.settings import INVOICE_DIR


class InvoiceFetcher:

    def __init__(self):
        os.makedirs(INVOICE_DIR, exist_ok=True)

    # ---------------------------------------------------
    # SAMPLE PLATFORM IMPLEMENTATIONS
    # Later we will add Gumroad, Payhip, Printify, etc.
    # ---------------------------------------------------

    def fetch_payhip_invoice(self, order_id):
        # Placeholder: Real API/HTML scraping will go here.
        file_path = f"{INVOICE_DIR}/payhip_order_{order_id}.pdf"
        with open(file_path, "wb") as f:
            f.write(b"%PDF-1.4\n% Fake Payhip Invoice\n")
        return file_path

    def fetch_gumroad_invoice(self, order_id):
        file_path = f"{INVOICE_DIR}/gumroad_order_{order_id}.pdf"
        with open(file_path, "wb") as f:
            f.write(b"%PDF-1.4\n% Fake Gumroad Invoice\n")
        return file_path

    def fetch_platform_invoice(self, platform, order_id):
        """
        Universal entry point
        """
        try:
            if platform == "Payhip":
                return self.fetch_payhip_invoice(order_id)
            if platform == "Gumroad":
                return self.fetch_gumroad_invoice(order_id)

            # Add more platforms here…

            return None

        except Exception as e:
            print(f"[ERROR] Invoice fetch failed for {platform}: {str(e)}")
            return None
