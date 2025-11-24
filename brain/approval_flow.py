# ==========================================
# JRAVIS APPROVAL ENGINE
# Handles the lock code system for approvals
# ==========================================

from config.settings import LOCK_CODE


class ApprovalFlow:

    def generate_request(self, message):
        return {
            "request": message,
            "instruction": "Enter Lock Code to Approve",
            "lock_code_required": True
        }

    def check(self, code_entered):
        return code_entered == LOCK_CODE
