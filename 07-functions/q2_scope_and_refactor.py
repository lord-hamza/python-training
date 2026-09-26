# Day 07 | Functions
# Q2 - Scope & Refactor
# ------------------------------------------------------------
# Part A — Scope
#   counter = 0
#   def increment():
#       counter += 1
#   increment()          <- run it, read the UnboundLocalError. Fix it with `global counter`.
#   Then comment why `global` is usually a bad idea, and rewrite it so  increment(counter)
#   RETURNS the new value instead.
#   Show a local variable shadowing a global one (same name inside and outside) and print both.
#   Can a function READ a global without `global`? Can it MODIFY a global list with .append()
#   without `global`? Test both. Comment: rebinding vs mutating.
#
# Part B — Refactor your earlier work into functions
#   1. Take 03-conditional-statements/q2_shipping_quote.py and turn the rules into
#          calculate_quote(distance, vehicle_type, is_operable, enclosed) -> float
#      No input() inside the function. Call it 5 times with different arguments.
#      A separate  ask_user_for_quote()  collects input and calls calculate_quote().
#      This split (logic vs I/O) is what makes code testable — the testing day will prove it.
#   2. Take 06-dictionary/q1_phone_book.py and split the menu into functions:
#          add_contact(book, name, phone), lookup(book, name), delete(book, name), list_all(book)
#      main() owns the loop and calls them. Notice how much easier the loop is to read.
#   3. Take 04-loops/q2_guess_the_number.py: play_round(secret, max_attempts) -> bool, and main().
#
# Part C — small things you'll use daily
#   - A function with NO return statement — what does it return? Print it.
#   - What does a bare  return  do?  Early return to avoid nested ifs ("guard clauses") — rewrite
#     one of your grade-calculator branches with guard clauses.
#   - Docstrings:  help(calculate_quote)  — write one for every function above.
#
# Bonus: write a function that takes a function as an argument (pass calculate_quote to a
#        run_and_print(func, *args) helper). That's tomorrow's topic peeking in.


# --- your code below ---

