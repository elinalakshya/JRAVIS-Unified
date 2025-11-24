class BasePayoutHandler:
    """
  Base payout handler for every earning platform.
  """

    def login(self):
        return True

    def check_payout_methods(self):
        return {"paypal_supported": False}

    def add_paypal(self, paypal_email):
        return False

    def save_wallet_balance(self):
        # For platforms that do not support PayPal directly
        return True
