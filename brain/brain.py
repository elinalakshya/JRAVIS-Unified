# ==========================================================
# JRAVIS BRAIN
# Central decision engine: memory, logic, approvals
# Unified Repo - Option A
# ==========================================================

import json
import os
from .logic_engine import JRAVISLogic
from .approval_flow import ApprovalFlow
from config.settings import LOCK_CODE

MEMORY_FILE = "./brain/memory.json"


class JRAVISBrain:

    def __init__(self):
        self.logic = JRAVISLogic()
        self.approval_engine = ApprovalFlow()

        # Load JRAVIS memory
        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "w") as f:
                json.dump({"events": [], "earnings": []}, f)

    # ----------------------
    # MEMORY MANAGEMENT
    # ----------------------
    def save_event(self, event):
        with open(MEMORY_FILE, "r") as f:
            mem = json.load(f)

        mem["events"].append(event)

        with open(MEMORY_FILE, "w") as f:
            json.dump(mem, f, indent=4)

    def save_earning(self, earning):
        with open(MEMORY_FILE, "r") as f:
            mem = json.load(f)

        mem["earnings"].append(earning)

        with open(MEMORY_FILE, "w") as f:
            json.dump(mem, f, indent=4)

    # ----------------------
    # APPROVAL FLOW
    # ----------------------
    def request_approval(self, message):
        return self.approval_engine.generate_request(message)

    def verify_approval(self, code_entered):
        return code_entered == LOCK_CODE

    # ----------------------
    # DECISION LOGIC
    # ----------------------
    def evaluate_system_status(self, worker_status):
        return self.logic.analyze(worker_status)

    # ----------------------
    # SUMMARY FOR DAILY REPORT
    # ----------------------
    def get_summary(self):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
