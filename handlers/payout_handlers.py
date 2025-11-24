from .payout_handler_template import BasePayoutHandler


# Example placeholder payout handler
class PrintablesPayoutHandler(BasePayoutHandler):

    def check_payout_methods(self):
        return {"paypal_supported": True}

    def add_paypal(self, paypal_email):
        print(f"[PAYOUT] PayPal {paypal_email} linked to Printables platform")
        return True


# Registry of payout handlers
PAYOUT_HANDLERS = {
    "Printables": PrintablesPayoutHandler(),
    # Add other platforms here...
}
