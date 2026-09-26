# Day 17 | OOP 3 - Encapsulation, @property, Dunder Methods
# Q2 - Dunder (Magic) Methods
# ------------------------------------------------------------
# class Money(amount, currency="USD"):
#   __str__     -> "$12.50"                 (print(), f-strings)
#   __repr__    -> "Money(12.5, 'USD')"     (debugger, REPL, inside lists) — print a LIST of Money
#                                            objects to see which one Python picks
#   __add__, __sub__  -> new Money;  raise ValueError if currencies differ
#   __mul__     -> Money(10) * 3   (and __rmul__ so 3 * Money(10) works too)
#   __eq__, __lt__, __le__  -> compare amounts. Now sorted(), max(), min() just work.
#   __bool__    -> False when amount == 0     (so  if money:  works)
#   __hash__    -> so Money can go in a set / be a dict key. Defining __eq__ silently sets
#                  __hash__ = None — try putting Money in a set without __hash__ first.
#
# class Inventory:
#   __len__       -> number of distinct items
#   __getitem__   -> inventory["laptop"] returns qty  (KeyError -> return 0? your call — comment it)
#   __setitem__   -> inventory["laptop"] = 5
#   __delitem__   -> del inventory["laptop"]
#   __contains__  -> "laptop" in inventory
#   __iter__      -> for item in inventory:      (return iter(self._items))
#
# class Vector(x, y):  __add__, __sub__, __mul__ (scalar), __abs__ (length), __eq__, __repr__, __neg__
#
# Test EVERYTHING. Then in a comment:
#   - print(obj) calls ___ ;  obj in the REPL / inside a list calls ___
#   - If you only define ONE of __str__/__repr__, which should it be, and why?
#
# Bonus:
#   __call__            make an object callable:  counter()  (Day 20 uses this)
#   __enter__/__exit__  your own context manager:  with Timer(): ...  prints elapsed time.
#   functools.total_ordering — define __eq__ and __lt__ and get the rest for free.


# --- your code below ---

