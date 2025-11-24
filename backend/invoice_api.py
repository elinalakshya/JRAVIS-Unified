# ============================================
# JRAVIS INVOICE API
# Returns daily/weekly/generated invoices
# ============================================

from fastapi import APIRouter
import os
from config.settings import INVOICE_DIR

router = APIRouter(prefix="/invoice", tags=["Invoices"])


@router.get("/list")
def list_invoices():
    if not os.path.exists(INVOICE_DIR):
        return []

    files = os.listdir(INVOICE_DIR)
    return {"invoices": files}


@router.get("/status")
def invoice_status():
    invoice_count = len(
        os.listdir(INVOICE_DIR)) if os.path.exists(INVOICE_DIR) else 0
    return {"invoice_count": invoice_count}
