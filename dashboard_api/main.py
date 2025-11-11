from fastapi import FastAPI
import httpx, asyncio, os

app = FastAPI()

services = {
    "backend": "https://jravis-backend.onrender.com/healthz",
    "brain": "https://jravis-brain.onrender.com/healthz",
    "intelligence": "https://mission2040-intelligence-worker.onrender.com",
    "memory": "https://mission2040-memory-sync-worker.onrender.com",
    "daily_report": "https://jravis-daily-report.onrender.com",
    "weekly_report": "https://jravis-weekly-report.onrender.com",
    "va_bot": "https://va-bot-connector.onrender.com",
    "income_system": "https://income-system-bundle.onrender.com"
}


@app.get("/api/status")
async def status():
    results = {}
    async with httpx.AsyncClient(timeout=5) as client:
        for name, url in services.items():
            try:
                r = await client.get(url)
                results[
                    name] = "🟢 OK" if r.status_code == 200 else f"⚠️ {r.status_code}"
            except Exception as e:
                results[name] = f"🔴 Error"
    return results


@app.get("/healthz")
def health():
    return {"status": "Dashboard API healthy ✅"}
