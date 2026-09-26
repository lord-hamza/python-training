# Day 05 | Lists, Tuples & Sets
# Q2 - Tuples & Sets
# ------------------------------------------------------------
# TUPLES — immutable records
#  1. point = (3, 4). Unpack into x, y. Distance from origin: (x**2 + y**2) ** 0.5
#  2. Try  point[0] = 10  — read the error, comment it out. Comment: WHY are tuples immutable,
#     WHEN would you pick one over a list?
#  3. employee = ("Hamza", "Dispatcher", 55000) -> unpack -> "Hamza works as Dispatcher earning $55,000"  (:, in f-string)
#  4. shipments = [("TX", "FL", 1300), ("CA", "NY", 2800), ("TX", "CA", 1400), ("FL", "GA", 350)]
#     for origin, dest, miles in shipments:  print each; total miles; longest shipment
#     (loop + "best so far"); how many start in TX
#  5. .count() and .index().  (5) is an int but (5,) is a tuple — prove it with type().
#  6. t = (1, [2, 3]);  t[1].append(4)  — allowed? Why?
#  7. Extended unpacking:  first, *rest = [1,2,3,4]     *head, last = ...     a, *_, z = ...
#  8. sorted(shipments) — what does it sort by when you don't tell it? Try it.
#
# SETS — unique, unordered, fast membership
#     monday  = {"ali", "sara", "hamza", "zara", "omar"}
#     tuesday = {"sara", "omar", "bilal", "zara"}
#  9. Worked both days (&);  at least one day (|);  Monday only (-);  exactly one day (^)
# 10. .add("ahmed") to tuesday; .remove("ali") from monday; .remove() a missing name vs .discard()
# 11. emails = ["a@x.com", "B@x.com", "a@x.com", "c@x.com", "b@x.com"] -> unique count, case-insensitive -> 3
# 12. Subset / superset / disjoint:  {"sara","zara"} <= monday     .issubset()   .isdisjoint()
# 13. Common elements of two lists: WITHOUT sets (nested loop) then WITH sets (one line).
# 14. Speed: time  x in big_list  vs  x in big_set  for 1,000,000 numbers, x = 999_999
#     (time.perf_counter). Google "O(1) lookup".
# 15. Why can't a list go inside a set? Try it. Use a tuple instead. Comment: "hashable" in one sentence.
# 16. frozenset — immutable set. When would you need one?
#
# Bonus: LeetCode 217 Contains Duplicate — one line with set() + len(). Then a loop version with a
#        "seen" set that returns early. Which does less work if the duplicate is at the start?


# --- your code below ---

