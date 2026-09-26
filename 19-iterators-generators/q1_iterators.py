# Day 19 | Iterators & Generators
# Q1 - The Iterator Protocol
# ------------------------------------------------------------
# 1. What does a `for` loop actually do? Do it by hand:
#      it = iter([1, 2, 3]);  next(it);  next(it);  next(it);  next(it)  -> StopIteration
#    Then write  my_for(iterable, func)  that uses iter()/next() and catches StopIteration.
# 2. class Countdown(start):  __iter__ returns self;  __next__ yields start..1 then raises
#    StopIteration.   for n in Countdown(5): print(n)
# 3. class EvenNumbers(limit)   and   class Fibonacci(limit)   as iterator classes.
# 4. ITERABLE vs ITERATOR: an iterable has __iter__ (a list); an iterator ALSO has __next__.
#    Make Day 17's Inventory iterable by returning  iter(self._items.items())  from __iter__.
#    Comment: why is it fine (and better) for Inventory NOT to be its own iterator?
# 5. An iterator is exhausted after one pass:  it = iter([1,2]);  list(it);  list(it)  -> []
#    A list can be looped twice. Why? (each iter(list) call makes a NEW iterator)
# 6. enumerate, zip, reversed, map, filter, dict.items() all return lazy iterators/views —
#    prove it: call next() on each, and print one (no data shown — just an object).
# 7. itertools — one example each, with a comment on what it did:
#      count(10, 5)     cycle("AB") (use islice or you'll loop forever)     repeat("x", 3)
#      islice(...)      chain(a, b)      accumulate([1,2,3,4])      product("AB", repeat=2)
#      permutations([1,2,3], 2)      combinations([1,2,3,4], 2)      pairwise([1,2,3,4])
#      groupby(shipments, key=lambda s: s["origin"])  — sort by the key FIRST or it won't group
# 8. class Paginator(items, page_size):  iterating yields one PAGE (a list) at a time. Use islice.
#
# Bonus: sentinel form of iter():  iter(input, "quit")  — reads input until the user types quit.


# --- your code below ---

