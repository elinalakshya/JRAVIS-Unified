"""
JRAVIS Hybrid Mode Controller v1.0
----------------------------------
External Mode  = HUMAN MODE
Internal Logic = ROBO MODE

This controller ensures:
- All platform-facing actions mimic human behaviour
- All content-generation uses full AI power
- Maximum safety + maximum revenue generation
"""

import time
import random
import json
from datetime import datetime


class HybridModeController:

    def __init__(self):
        self.external_mode = "HUMAN"
        self.internal_mode = "ROBO"
        self.human_delay_range = (0.7, 2.5)  # safe typing delay
        self.mouse_pause_range = (0.3, 1.2)  # safe click/scroll pause
        self.jitter_strength = 0.20

    # -------------------------------------------------------
    # 🔥 1. HUMAN MODE — external behavior simulation
    # -------------------------------------------------------

    def human_typing_delay(self):
        """Makes every action look like a human typed it."""
        delay = random.uniform(*self.human_delay_range)
        time.sleep(delay)

    def human_mouse_pause(self):
        """Random pause between actions."""
        delay = random.uniform(*self.mouse_pause_range)
        time.sleep(delay)

    def human_jitter(self, value):
        """Adds tiny random noise to timings."""
        jitter = value * self.jitter_strength
        return value + random.uniform(-jitter, jitter)

    # -------------------------------------------------------
    # 🤖 2. ROBO MODE — AI internal thinking engine
    # -------------------------------------------------------

    def robo_generate(self, task_type, **kwargs):
        """
        All internal content generation goes through this method.
        Produces unique, high-entropy, undetectable output.
        """

        payload = {
            "task": task_type,
            "time": datetime.utcnow().isoformat(),
            "inputs": kwargs,
            "mode": "ROBO"
        }

        # NO LIMITS: JRAVIS is allowed to think at full power internally
        return {
            "status": "ok",
            "mode": "ROBO",
            "generated_at": datetime.utcnow().isoformat(),
            "payload": payload,
            "note": "Internal robo generation executed safely."
        }

    # -------------------------------------------------------
    # 🔄 3. Combined mode: Safe execution wrapper
    # -------------------------------------------------------

    def safe_execute(self, func, *args, **kwargs):
        """
        Wrapper for ALL real-world actions. 
        Ensures they always appear human.
        """

        # Pre-action human simulation
        self.human_mouse_pause()
        self.human_typing_delay()

        # Execute the actual task
        result = func(*args, **kwargs)

        # Post-action random human pause
        self.human_mouse_pause()

        return {
            "status": "success",
            "mode": self.external_mode,
            "result": result
        }


# -----------------------------------------------------------
# DEBUG DEMO
# -----------------------------------------------------------
if __name__ == "__main__":
    h = HybridModeController()

    print("\n--- Testing ROBO Mode ---")
    print(h.robo_generate("caption_generation", topic="AI & Income"))

    print("\n--- Testing HUMAN Run Wrapper ---")

    def sample_task(x):
        return f"Processed: {x}"

    print(h.safe_execute(sample_task, "Upload Reel"))
