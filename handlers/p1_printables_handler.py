from .handler_template import BaseHandler
import random
import json
import os
from config.settings import OUTPUT_DIR


class PrintablesHandler(BaseHandler):

    def run(self):
        # Generate a sample printable product
        data = {
            "title": "Minimal Productivity Printable",
            "format": "PDF",
            "tags": ["productivity", "stationery"],
            "price": 3.99,
            "timestamp": random.random()
        }

        # Ensure output directory exists
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Save output
        filename = f"{OUTPUT_DIR}/printable_{int(data['timestamp'])}.json"
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        print(f"[STREAM] Printable generated → {filename}")


# Function to be used by unified engine
def run_printables_handler():
    PrintablesHandler().run()
    