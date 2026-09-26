# Day 11 | Error Handling
# Q2 - Custom Exceptions & raise
# ------------------------------------------------------------
# Define (yes, this is a class — that's all you need to know today):
#   class InsufficientFundsError(Exception): pass
#   class InvalidAmountError(Exception): pass
#
# deposit(balance, amount) -> new balance     raises InvalidAmountError if amount <= 0
# withdraw(balance, amount) -> new balance    raises InvalidAmountError if amount <= 0,
#                                             raises InsufficientFundsError if amount > balance
# Give InsufficientFundsError a useful message that includes balance AND requested amount:
#   raise InsufficientFundsError(f"Balance ${balance:.2f}, tried to withdraw ${amount:.2f}")
#
# Rewrite your Day 04-era banking menu (07-functions/banking.py) to use these. The loop must:
#   - catch BOTH custom errors and print friendly messages
#   - catch ValueError for non-numeric input
#   - NEVER crash, whatever the user types
#
# Then:
#   validate_shipment(shipment: dict) -> None
#     raises ValueError with a SPECIFIC message for each missing key ("origin", "dest", "miles"),
#     if miles is not a number, or if miles <= 0. Test with 5 bad dicts and 1 good one.
#
#   parse_age(text) -> int   raises ValueError("age must be a whole number") / ("age out of range")
#
# Custom exception with extra data:
#   class ShipmentError(Exception):
#       def __init__(self, shipment_id, message): ... store shipment_id, call super().__init__(message)
#   Raise it, catch it, print e.shipment_id.
#
# Exception chaining:  raise ValueError("bad config") from e  — read the traceback ("The above
# exception was the direct cause...").
#
# Bonus: `assert amount > 0, "amount must be positive"` — when are asserts OK and when are they
#        NOT a substitute for raising? (hint: python -O strips them)


# --- your code below ---

