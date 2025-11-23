#!/usr/bin/env python3
"""
JRAVIS Backend (MAIN) — Clean Architecture B
--------------------------------------------
This file is ONLY the API + Dashboard + Command Interface.

All automation (scheduler, gmail, daily reports, phase cycles)
runs inside worker.py or other workers separately.

This file must stay ASGI SAFE for Render (gunicorn + uvicorn worker).
"""

import os
import logging
from datetime import datetime

# ---------------------------
# FLASK APP  (WSGI)
# ---------------------------
from flask import Flask, jsonify, request

# Phase-1 Engine
from p1_queue_engine import activate_phase1_fullpower_cycle

flask_app = Flask(__name__)


@flask_app.route("/", methods=["GET"])
def root():
    return jsonify({
        "status": "ok",
        "system": "JRAVIS Backend",
        "message": "🚀 JRAVIS Backend Active (Main Server)"
    }), 200


@flask_app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "system": "JRAVIS Backend",
        "time": datetime.utcnow().isoformat()
    }), 200


@flask_app.route("/command", methods=["POST"])
def command():
    if cmd in ["activate_phase_1", "begin_phase_1", "phase1_start"]:
        return jsonify({"status": "ok", "phase": "1 activated"}), 200

    if cmd in ["activate_phase_2", "begin_phase_2", "phase2_start"]:
        return jsonify({"status": "ok", "phase": "2 activated"}), 200

    if cmd in ["activate_phase_3", "begin_phase_3", "phase3_start"]:
        return jsonify({"status": "ok", "phase": "3 activated"}), 200



# ---------------------------
# FASTAPI Dashboard (ASGI)
# ---------------------------
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.wsgi import WSGIMiddleware

api = FastAPI(title="JRAVIS Dashboard API")

api.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])


@api.get("/summary")
def get_summary():
    return {
        "system": "JRAVIS Dashboard",
        "status": "running",
        "time": datetime.utcnow().isoformat(),
        "note": "Dashboard API responding normally."
    }


# ---------------------------
# UNIFIED ASGI SERVER
# ---------------------------
asgi_app = FastAPI(title="JRAVIS Unified Server")

# CORS
asgi_app.add_middleware(CORSMiddleware,
                        allow_origins=["*"],
                        allow_methods=["*"],
                        allow_headers=["*"])

# mount Flask WSGI inside ASGI
asgi_app.mount("/", WSGIMiddleware(flask_app))

# mount FastAPI at /api
asgi_app.mount("/api", api)

# Export for Gunicorn/Uvicorn
application = asgi_app
