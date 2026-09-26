# Day 19 | Iterators & Generators
# Q2 - Generators & yield
# ------------------------------------------------------------
# 1. Rewrite Countdown, EvenNumbers, Fibonacci from Q1 as generator FUNCTIONS using yield.
#    Compare line counts. Print type(countdown(5)) — it's a generator object; call next() on it.
# 2. Generate a file with 1,000,000 log lines ("INFO ..." / "ERROR ..." at random). Then
#    read_lines(path)  yields stripped lines one at a time. Count lines containing "ERROR"
#    WITHOUT ever holding the whole file in memory. Compare peak memory to f.readlines()
#    (tracemalloc, or just watch Activity Monitor).
# 3. Generator PIPELINE — each stage consumes the previous one, nothing runs until the sum():
#      lines = read_lines("shipments.csv")
#      rows = parse(lines)                   -> yields dicts
#      delivered = (r for r in rows if r["status"] == "delivered")
#      total = sum(float(r["price"]) for r in delivered)
#    Put a print() inside parse() to SEE the laziness — lines are pulled one by one.
# 4. chunked(iterable, size)  ->  chunked(range(10), 3)  yields [0,1,2], [3,4,5], [6,7,8], [9]
# 5. Infinite generator:  ids(start=100): while True: yield start; start += 1
#    Use with next() and with islice. Why does list(ids()) never return? (Ctrl+C)
# 6. Generator expression vs list comprehension: sys.getsizeof() of both for range(1_000_000);
#    put a print inside a function called in each to see WHEN it runs.
# 7. yield from:  flatten(nested)  recursively —  [1, [2, [3, [4]]], 5]  ->  1 2 3 4 5
# 8. send():  running_average()  — a generator you .send(value) to and it yields the average so far.
#    (advanced — get it working, then move on)
# 9. Generators and files: a generator that opens a file, yields lines, and CLOSES it — where does
#    the `with` go? What happens if the consumer stops early? (try/finally in the generator)
#
# Bonus: a generator that reads shipments.csv and yields Day 18 dataclass Shipment objects.
#        That's the read path of your final project.


# --- your code below ---

