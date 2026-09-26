# Day 09 | Functions Advanced (map, filter, lambda)
# Q1 - *args, **kwargs, lambda, defaults
# ------------------------------------------------------------
# 1. total(*numbers) -> sum of any number of arguments.   total(1, 2, 3) -> 6    total() -> 0
# 2. average(*numbers) -> return 0 if called with nothing.
# 3. build_profile(first, last, **extra) -> dict
#    build_profile("lord", "hamza", role="dev", city="Dallas")
#    -> {"first": "lord", "last": "hamza", "role": "dev", "city": "Dallas"}
# 4. log(message, *tags, level="INFO", **meta) prints one line like:
#    [INFO] Order shipped #shipping #urgent {'order_id': 42}
#    Call it 3 ways: message only; with tags; with level="ERROR" and keyword meta.
# 5. Unpack INTO a call:  nums = [3, 5]; power(*nums)     opts = {"a": 1, "b": 2}; f(**opts)
# 6. Rewrite as lambdas assigned to variables:  square, is_even, full_name(first, last)
# 7. make_multiplier(n) RETURNS a lambda.   double = make_multiplier(2);  double(5) -> 10
# 8. The mutable-default bug:   def add_item(item, items=[]): items.append(item); return items
#    Call add_item("a") then add_item("b") — print both results. Surprised? Fix it with None.
# 9. Keyword-only args:   def connect(host, *, port=5432, timeout=30)
#    Try connect("db", 5432) — read the error. Why would you force keyword-only?
# 10. Positional-only (Python 3.8+):  def f(a, b, /):  — try f(a=1, b=2).
# 11. Print a function's __name__ and __doc__. Assign a function to another variable and call it.
#     Put 3 functions in a list and call each in a loop. Put them in a dict {"add": add, ...} and
#     dispatch by user input — that's how the menu in your Day 06 phone book SHOULD work.
#
# Bonus: what's the difference between  *args  as a tuple and  **kwargs  as a dict — and why
#        does order matter:  def f(a, b=2, *args, c, **kwargs)  — draw it as a comment.


# --- your code below ---

