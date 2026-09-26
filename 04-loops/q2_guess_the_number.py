# Day 04 | Loops
# Q2 - Guess the Number
# ------------------------------------------------------------
# import random
# secret = random.randint(1, 100)
#
# Use a while loop to keep asking for a guess until the user gets it.
#   - After each wrong guess print "Too high" or "Too low" and the number of guesses so far.
#   - Max 7 attempts. If they run out, print the secret and end.
#   - If the user types "q", quit immediately (break).
#   - If the user types something that isn't a number, print "Numbers only" and DON'T count
#     it as an attempt (continue + str.isdigit()).
#   - On a win, print "You got it in N tries!"
#
# Then wrap the whole game in an outer loop:  "Play again? (y/n)"
#
# Bonus: track the best score (fewest tries) across games in the same session.
# Bonus 2: binary-search yourself — what's the minimum number of guesses that GUARANTEES
#          a win for 1..100? Write it in a comment and explain why.


# --- your code below ---

