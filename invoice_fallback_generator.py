# ============================================
# JRAVIS FALLBACK INVOICE GENERATOR
# Used when platforms do not provide invoices
# ============================================

import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from config.settings import INVOICE_DIR


def create_fallback_invoice(platform, product, amount, order_id):
    os.makedirs(INVOICE_DIR, exist_ok=True)

    filename = f"{INVOICE_DIR}/{platform}_fallback_invoice_{order_id}.pdf"

    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, 750, "JRAVIS Auto Invoice")

    c.setFont("Helvetica", 12)
    c.drawString(40, 700, f"Platform: {platform}")
    c.drawString(40, 680, f"Product: {product}")
    c.drawString(40, 660, f"Amount: ${amount}")
    c.drawString(40, 640, f"Order ID: {order_id}")

    c.drawString(40, 600,
                 "This invoice was auto-generated because the platform")
    c.drawString(40, 580, "does not provide direct invoice downloads.")

    c.save()
    return filename
