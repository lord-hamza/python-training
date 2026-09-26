# Day 03 | Conditionals
# Q1 - Grade Calculator
# ------------------------------------------------------------
# Ask for a score from 0 to 100 (input -> int).
#
# 1. Print the letter grade:
#      90-100 -> A,  80-89 -> B,  70-79 -> C,  60-69 -> D,  below 60 -> F
#    If the score is outside 0-100 print "Invalid score" and nothing else.
# 2. Print "Pass" if the grade is A, B or C, otherwise "Fail".
# 3. Add a "+" to the grade if the last digit of the score is 7 or higher
#    (87 -> B+). Use  score % 10.  No "+" for A when score is 100, and never for F.
# 4. Print "Perfect!" only when the score is exactly 100.
#
# Test with: 100, 97, 87, 73, 60, 59, -5, 101  — write the expected output for
# each as a comment at the bottom, then run and compare.
#
# Bonus: Rewrite the grade lookup using a chain of ternary expressions on one line
#        grade = "A" if score >= 90 else "B" if score >= 80 else ...
#        Then write a comment: which version would you want to read in 6 months?


# --- your code below ---

