from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
import threading
from datetime import datetime
import os
<<<<<<< HEAD
from send_report import orchestrate_daily, orchestrate_weekly  # you already created this
=======
from send_report import orchestrate_daily, orchestrate_weekly
>>>>>>> 3ce708d27c5316766c8a0e3476828ac15a402322

app = FastAPI(title="JRAVIS Backend API")

ADMIN_CODE = os.getenv("REPORT_API_CODE", "2040")

@app.get("/")
def home():
    return {"status": "JRAVIS Backend running", "version": "1.0"}

@app.get("/api/send_daily_report")
def send_daily_report(code: str):
    if code != ADMIN_CODE:
        raise HTTPException(status_code=401, detail="Invalid code")

    date_str = datetime.now().strftime("%d-%m-%Y")
<<<<<<< HEAD
    threading.Thread(target=orchestrate_daily, args=(date_str,), daemon=True).start()

    return {"detail": "Daily report sent"}
=======
    threading.Thread(
        target=orchestrate_daily,
        args=(date_str,),
        daemon=True
    ).start()

    return {"detail": "Daily report email sent", "date": date_str}
>>>>>>> 3ce708d27c5316766c8a0e3476828ac15a402322

@app.get("/api/send_weekly_report")
def send_weekly_report(code: str):
    if code != ADMIN_CODE:
        raise HTTPException(status_code=401, detail="Invalid code")

<<<<<<< HEAD
    threading.Thread(target=orchestrate_weekly, daemon=True).start()

    return {"detail": "Weekly report sent"}

# Start server
=======
    threading.Thread(
        target=orchestrate_weekly,
        daemon=True
    ).start()

    return {"detail": "Weekly report email sent"}

>>>>>>> 3ce708d27c5316766c8a0e3476828ac15a402322
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
