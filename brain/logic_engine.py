# ==========================================
# JRAVIS LOGIC ENGINE
# Makes decisions based on worker activity
# ==========================================


class JRAVISLogic:

    def analyze(self, worker_status):
        """
        Basic analysis of system health.
        This is simple now but will expand later.
        """

        summary = {
            "streams_completed": worker_status.get("streams_ok", 0),
            "streams_failed": worker_status.get("streams_failed", 0),
            "payouts_completed": worker_status.get("payout_ok", 0),
            "issues": worker_status.get("issues", [])
        }

        # Basic logic rules:
        if summary["streams_failed"] == 0:
            summary["system_health"] = "GOOD"
        elif summary["streams_failed"] <= 3:
            summary["system_health"] = "WARN"
        else:
            summary["system_health"] = "CRITICAL"

        return summary
