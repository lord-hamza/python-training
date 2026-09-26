# Day 06 | Dictionaries
# Q2 - Counting, Grouping, Transforming
# ------------------------------------------------------------
# text = "the quick brown fox jumps over the lazy dog the fox"
#
# 1. Count how many times each word appears  ->  {"the": 3, "fox": 2, "quick": 1, ...}
#    First with the   if word in counts: ... else: ...   pattern,
#    then again in one line inside the loop with   counts[word] = counts.get(word, 0) + 1
# 2. Print the 3 most common words. (sorted with key is Day 09 — for now build a list of
#    (count, word) tuples, sort it, take the last 3.)
# 3. Group by state:
#    shipments = [("TX", 1300), ("FL", 900), ("TX", 1400), ("CA", 2800), ("FL", 400)]
#    ->  {"TX": [1300, 1400], "FL": [900, 400], "CA": [2800]}
#    then totals per state  ->  {"TX": 2700, "FL": 1300, "CA": 2800}
#    then the state with the most miles
# 4. Invert a dict:  {"a": 1, "b": 2}  ->  {1: "a", 2: "b"}
# 5. Merge two dicts where the second wins on conflicts. Try  {**a, **b}  and  a | b.
# 6. Nested data — walk this and print each order line:
#    orders = {
#        "ORD-1": {"customer": "Ali",  "items": [{"name": "laptop", "qty": 1, "price": 999}],
#                  "status": "shipped"},
#        "ORD-2": {"customer": "Sara", "items": [{"name": "mouse", "qty": 2, "price": 25},
#                                                 {"name": "hub", "qty": 1, "price": 45}],
#                  "status": "pending"},
#    }
#    Print the total per order and the grand total. List customers with pending orders.
# 7. Delete every key whose value is 0 from a dict — WHILE iterating over it. Read the error.
#    Then do it correctly (iterate over a copy / build a new dict).
# 8. setdefault():  group words by their first letter using .setdefault(letter, []).append(word)
#
# Bonus: count characters in a string (ignore spaces) and print a vertical bar chart, sorted:
#        e | #####
#        o | ####


# --- your code below ---

