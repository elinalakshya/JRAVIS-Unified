#!/usr/bin/env python3
"""
JRAVIS Backend (MAIN)
Clean ASGI + WSGI Hybrid
"""

import os
import logging
from datetime import datetime

from flask import Flask, jsonify, request
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.wsgi import WSGIMiddleware

# ---------------------
# Flask App (WSGI)
# ---------------------
flask_app = Flask(__name__)


@flask_app.route("/", methods=["GET"])
def root():
    return jsonify({
        "status": "ok",
        "system": "JRAVIS Backend",
        "message": "🚀 JRAVIS Backend Active"
    })


@flask_app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "time": datetime.utcnow().isoformat()})


@flask_app.route("/command", methods=["POST"])
def command():
    data = request.get_json(force=True)
    cmd = data.get("cmd", "").lower().strip()

    if cmd in ["activate_phase_1", "begin_phase_1", "phase1_start"]:
        return jsonify({"status": "ok", "phase": "1 activated"}), 200

    if cmd in ["activate_phase_2", "begin_phase_2", "phase2_start"]:
        return jsonify({"status": "ok", "phase": "2 activated"}), 200

    if cmd in ["activate_phase_3", "begin_phase_3", "phase3_start"]:
        return jsonify({"status": "ok", "phase": "3 activated"}), 200

    return jsonify({"error": "unknown command"}), 400


# ---------------------
# FastAPI (ASGI)
# ---------------------
api = FastAPI(title="JRAVIS Dashboard API")

api.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])


@api.get("/summary")
def summary():
    return {
        "system": "JRAVIS Dashboard",
        "status": "running",
        "time": datetime.utcnow().isoformat()
    }


# ---------------------
# Unified ASGI App
# ---------------------
asgi_app = FastAPI(title="JRAVIS Unified ASGI Server")

asgi_app.add_middleware(CORSMiddleware,
                        allow_origins=["*"],
                        allow_methods=["*"],
                        allow_headers=["*"])

asgi_app.mount("/", WSGIMiddleware(flask_app))
asgi_app.mount("/api", api)

# Gunicorn entrypoint
application = asgi_app
