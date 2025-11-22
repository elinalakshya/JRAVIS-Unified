from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import io


def make_summary_pdf(data: dict) -> bytes:
    """Create a simple summary PDF and return bytes."""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, 800, f"JRAVIS Summary Report")
    c.setFont("Helvetica", 11)
    y = 760
    for k, v in data.items():
        c.drawString(40, y, f"{k}: {v}")
        y -= 18
        if y < 100:
            c.showPage()
            y = 800
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.read()


def make_invoice_pdf(invoices: list) -> bytes:
    """Create a simple invoices PDF and return bytes."""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, 800, "JRAVIS Invoices")
    c.setFont("Helvetica", 11)
    y = 760
    for inv in invoices:
        c.drawString(40, y,
                     f"Invoice: {inv.get('id')} Amount: {inv.get('amount')}")
        y -= 18
        if y < 100:
            c.showPage()
            y = 800
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.read()


def encrypt_pdf(pdf_bytes: bytes, password: str) -> bytes:
    """Encrypt pdf bytes with a password and return new bytes."""
    reader = PdfReader(io.BytesIO(pdf_bytes))
    writer = PdfWriter()
    for p in reader.pages:
        writer.add_page(p)
    writer.encrypt(password)
    out = io.BytesIO()
    writer.write(out)
    out.seek(0)
    return out.read()
