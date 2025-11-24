# ============================================
# JRAVIS EARNINGS API
# Fetches all earnings across 30 streams
# ============================================

from fastapi import APIRouter
from brain.brain import JRAVISBrain

router = APIRouter(prefix="/earnings", tags=["Earnings"])
brain = JRAVISBrain()


@router.get("/all")
def all_earnings():
    summary = brain.get_summary()
    return {"earnings": summary.get("earnings", [])}


@router.get("/wallets")
def wallet_balances():
    # placeholder, real values come from payout handlers
    wallets = {
        "Printables": 0,
        "Templates": 0,
        "Course Sales": 0,
        "Affiliate Sales": 0
    }
    return wallets
