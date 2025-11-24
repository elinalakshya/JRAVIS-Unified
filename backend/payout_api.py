# ============================================
# JRAVIS PAYOUT API
# Interfaces with payout engine + PayPal link
# ============================================

from fastapi import APIRouter
from config.settings import PAYPAL_EMAIL

router = APIRouter(prefix="/payout", tags=["Payout"])


@router.get("/paypal")
def paypal_info():
    return {"paypal_email": PAYPAL_EMAIL}


@router.get("/status")
def payout_status():
    return {
        "supported_streams": 17,
        "wallet_only_streams": 13,
        "paypal_linked": True
    }
