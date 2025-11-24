# ============================================
# JRAVIS DASHBOARD API
# Provides data to frontend dashboard
# ============================================

from fastapi import APIRouter
from brain.brain import JRAVISBrain

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])
brain = JRAVISBrain()


@router.get("/summary")
def dashboard_summary():
    return brain.get_summary()


@router.get("/status")
def system_status():
    worker_status = {
        "streams_ok": 25,  # to be filled dynamically
        "streams_failed": 5,
        "payout_ok": 10,
        "issues": []
    }
    return brain.evaluate_system_status(worker_status)
