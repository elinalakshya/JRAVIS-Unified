# ============================================
# JRAVIS BACKEND - MAIN APP (FastAPI)
# ============================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .dashboard_api import router as dashboard_router
from .earnings_api import router as earnings_router
from .payout_api import router as payout_router
from .invoice_api import router as invoice_router

app = FastAPI(title="JRAVIS Backend API", version="3.0 Unified")

# Allow dashboard to access backend
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])

# Register routes
app.include_router(dashboard_router)
app.include_router(earnings_router)
app.include_router(payout_router)
app.include_router(invoice_router)


@app.get("/")
def home():
    return {"status": "JRAVIS Backend Running", "version": "3.0 Unified"}
