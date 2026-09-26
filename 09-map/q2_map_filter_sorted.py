# Day 09 | Functions Advanced (map, filter, lambda)
# Q2 - map / filter / sorted / higher-order functions
# ------------------------------------------------------------
# shipments = [
#     {"id": 101, "origin": "TX", "dest": "FL", "miles": 1300, "price": 890.0,  "status": "delivered"},
#     {"id": 102, "origin": "CA", "dest": "NY", "miles": 2800, "price": 1650.0, "status": "in_transit"},
#     {"id": 103, "origin": "TX", "dest": "CA", "miles": 1400, "price": 990.0,  "status": "delivered"},
#     {"id": 104, "origin": "FL", "dest": "GA", "miles": 350,  "price": 320.0,  "status": "quoted"},
#     {"id": 105, "origin": "NY", "dest": "TX", "miles": 1600, "price": 1100.0, "status": "in_transit"},
# ]
# 1. filter():  only delivered shipments  ->  list(filter(lambda s: ..., shipments))
# 2. map():     list of just the ids;  list of price-per-mile (2 dp)
# 3. sorted() with key=lambda:  by price descending;  by (status, miles);  by dest alphabetically
#    Does sorted() change `shipments`? Does .sort()?
# 4. max() / min() with key:  most expensive shipment;  shortest shipment
# 5. apply_to_all(func, items) -> list. Use it with a named function AND a lambda.
# 6. repeat(func, times) — takes a function and calls it `times` times.
# 7. Total revenue of delivered shipments with sum() + a generator expression (no list).
# 8. functools.reduce: product of [1, 2, 3, 4, 5];  then the longest word in a list with reduce.
# 9. Sort a list of strings by length, then alphabetically for ties:  key=lambda s: (len(s), s)
# 10. Sort names case-insensitively:  key=str.lower   (no lambda needed — a method is a function)
# 11. Rewrite 1 and 2 as list comprehensions — a preview of tomorrow.
# 12. Write a comment: when would you use map/filter vs a comprehension vs a plain loop?
#
# Bonus: operator.itemgetter("price") instead of lambda s: s["price"]  — and attrgetter for later.


# --- your code below ---

