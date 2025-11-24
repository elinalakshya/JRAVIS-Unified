# JRAVIS HANDLERS REGISTRY

from .p1_printables_handler import run_printables_handler

# Stream registry:
# ID: ("name", function)
ALL_HANDLERS = {
    1: ("run_printables_handler", run_printables_handler),
    # More handlers will be added here…
}
