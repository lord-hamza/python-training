# Day 03 | Conditionals
# Q2 - Shipping Quote Rules
# ------------------------------------------------------------
# You're writing the pricing logic for a vehicle transport company.
# Ask the user for:
#   distance      (miles, int)
#   vehicle type  ("sedan", "suv" or "truck")
#   operable?     ("yes" / "no")   — can the car drive onto the trailer?
#   enclosed?     ("yes" / "no")   — enclosed trailer vs open
#
# Rules (apply in this order):
#   base rate per mile:  sedan 0.60 | suv 0.75 | truck 0.95
#   any other vehicle type   -> print "Unknown vehicle type" and stop
#   not operable             -> add $150 flat
#   enclosed                 -> add 40% to the total so far
#   distance under 100       -> minimum charge $250 applies  (total = max(total, 250))
#   distance over 2000       -> 10% long-haul discount on the total
#
# Print the final quote with 2 decimals, plus a one-line summary:
#   "1300 mi | suv | operable | enclosed | $1365.00"
#
# Requirements:
#   - Handle "Yes", "YES", " yes " the same as "yes"   (.strip().lower())
#   - Use  and / or / not  at least once each
#   - Use a ternary:   label = "enclosed" if enclosed else "open"
#   - Test EVERY branch. Write the inputs you tested and the expected result as comments.
#
# Bonus: what's "truthy" / "falsy"?  Print bool() of:  0, 1, -1, "", "0", " ", [], [0], None
#        and write one sentence about it.


# --- your code below ---

