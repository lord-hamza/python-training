# Day 08 | Recursion
# Q1 - Recursion Basics
# ------------------------------------------------------------
# A recursive function calls itself. It MUST have a base case (when to stop) and every call
# must move toward it. Write each of these recursively — no loops:
#
#  1. factorial(n)              5 -> 120.       Base case: n <= 1
#  2. sum_to(n)                 sum of 1..n
#  3. sum_list(numbers)         [1, 2, 3] -> 6    (hint: first element + sum_list(rest))
#  4. sum_digits(n)             1234 -> 10
#  5. power(base, exp)          2, 10 -> 1024
#  6. reverse_string(s)         "hello" -> "olleh"
#  7. is_palindrome(s)          compare first and last, recurse on the middle
#  8. count_down(n)             prints n, n-1, ... 1, "Liftoff!"   — then count_up(n) by moving
#                               the print to AFTER the recursive call. Comment: why does that work?
#  9. fib(n)                    the slow way. Time fib(30) and fib(35). Comment: how many times is
#                               fib(2) computed for fib(35)? (draw the tree for fib(5) as a comment)
# 10. gcd(a, b)                 Euclid: gcd(b, a % b), base case b == 0
# 11. binary(n) -> str          10 -> "1010"
#
# Then:
# 12. Call factorial(1000). Read the RecursionError. Print  sys.getrecursionlimit().
#     Comment: what is the call stack, and why does Python limit it?
# 13. Write factorial and sum_list AGAIN with loops. Comment: when is recursion clearer than a
#     loop, and when is a loop the better choice?
#
# Bonus: trace a call by hand — add a  depth  parameter and print  "  " * depth + f"factorial({n})"
#        so you can SEE the calls go down and the returns come back up.


# --- your code below ---

