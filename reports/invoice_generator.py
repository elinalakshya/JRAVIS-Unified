# ============================================
# JRAVIS INVOICE PDF GENERATOR
# ============================================

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from config.settings import LOCK_CODE


def generate_invoice_pdf(title, data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, height - 40, title)

    c.setFont("Helvetica", 11)

    y = height - 80
    for key, value in data.items():
        c.drawString(40, y, f"{key}: {value}")
        y -= 20
        if y < 80:
            c.showPage()
            y = height - 40

    c.save()

    return filename
