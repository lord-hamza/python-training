# Day 10 | List Comprehension
# Q1 - List / Dict / Set Comprehensions
# ------------------------------------------------------------
# Write each as ONE comprehension (no .append):
#  1. squares of 1..10
#  2. even squares only                                   (trailing  if)
#  3. ["EVEN" if n % 2 == 0 else "ODD" for n in ...]       (if/else goes BEFORE the for)
#  4. all (x, y) pairs where x in 1..3, y in 1..3, x != y  (two fors)
#  5. flatten [[1, 2], [3, 4], [5]] -> [1, 2, 3, 4, 5]
#  6. dict:  {word: len(word)}  for the words in a sentence
#  7. dict:  swap keys/values of {"a": 1, "b": 2}
#  8. dict:  from prices = {"laptop": 999, "mouse": 25, "monitor": 300} keep only items over 100
#  9. dict:  {n: n**2 for n in range(1, 6)}  then  {n: "even"/"odd"}
# 10. set:   unique first letters of a list of names, lowercased
# 11. matrix transpose in one line:  [[row[i] for row in matrix] for i in range(3)]
# 12. from a text: words longer than 3 chars, lowercased, no duplicates, sorted
# 13. Rewrite Day 09 Q2 items 1, 2 and 7 as comprehensions.
# 14. Nested dict comprehension: multiplication table  {i: {j: i*j for j in 1..5} for i in 1..5}
# 15. Write a deliberately unreadable triple-nested comprehension. Then rewrite it as loops.
#     Comment: when is a comprehension WORSE than a loop?  (rule of thumb: > 2 clauses, or side effects)
#
# Bonus: generator expression vs list comprehension:
#        sum(x*x for x in range(1_000_000))   vs   sum([x*x for x in range(1_000_000)])
#        Compare memory with  sys.getsizeof()  on the two objects (not the sums).


# --- your code below ---

