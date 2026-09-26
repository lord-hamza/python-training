# Day 10 | List Comprehension
# Q2 - enumerate / zip / any / all
# ------------------------------------------------------------
# names  = ["Ali", "Sara", "Hamza", "Zara"]
# scores = [88, 95, 60, 70]
# cities = ["Dallas", "Miami", "Austin", "Houston"]
#
# 1. Print "1. Ali" ... using enumerate(names, start=1)          (no manual counter variable)
# 2. Print "Ali scored 88" using zip
# 3. Build {name: score} in one line with dict(zip(...))
# 4. Zip all three lists and print a formatted row per person (f-string alignment from Day 02)
# 5. Unzip:  names2, scores2 = zip(*pairs)   — what type do you get back?
# 6. Find the INDEX of the highest score using enumerate (no .index())
# 7. any():  does anyone score under 65?      all():  did everyone pass (>= 60)?
#    Use them with a generator expression inside.
# 8. Compare two lists element-wise with zip: print the positions where they differ.
# 9. enumerate over a dict's .items() to print "1) key = value"
# 10. Pair each item with the NEXT one:  for a, b in zip(items, items[1:])  — print the jumps
#     in a list of shipment miles.
# 11. zip stops at the shortest list — show it. Then itertools.zip_longest(fillvalue="-").
#     Python 3.10+:  zip(a, b, strict=True)  raises if lengths differ — try it.
# 12. Build a dict {name: (score, city)} in one comprehension using zip.
# 13. reversed(), sorted() with enumerate — print a ranking (1st, 2nd, 3rd ... by score).
#
# Bonus: write your own  my_enumerate(iterable, start=0)  and  my_zip(a, b)  using plain loops
#        (Day 19 will show you how to make them lazy with yield).


# --- your code below ---

