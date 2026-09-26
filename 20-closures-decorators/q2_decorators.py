# Day 20 | Closures & Decorators
# Q2 - Decorators
# ------------------------------------------------------------
# A decorator is a function that takes a function and returns a new function.  @name  is just
# sugar for  func = name(func).  Prove that first with a trivial decorator applied both ways.
#
# 1. @timer  -> prints how long the call took (time.perf_counter). Use  @functools.wraps(func)
#    inside and show what  func.__name__ / __doc__  look like WITHOUT it.
# 2. @log_calls  -> prints the function name, args, kwargs, and the return value.
#    Must work for ANY signature:  def wrapper(*args, **kwargs)
# 3. @retry(times=3, delay=0.5)  -> a decorator WITH ARGUMENTS (a function that returns a
#    decorator). Test on a function that raises randomly. Re-raise after the last attempt.
# 4. @require_positive  -> raises ValueError if any positional arg is <= 0. Apply to withdraw().
# 5. @memoize (your Q1) vs  @functools.lru_cache(maxsize=None)  on fib(35). Then  fib.cache_info().
# 6. Stacking:   @timer  @log_calls  def f(): ...   — which wrapper runs first? Which is
#    applied first? Comment with the equivalent  timer(log_calls(f)).
# 7. Class-based decorator:  class CountCalls  with __init__(func) and __call__(*a, **kw)  that
#    counts calls;  f.calls  is readable from outside.
# 8. Decorating METHODS: write  @validate_status(*allowed)  for Shipment methods — checks
#    self.status is in allowed before running, else raises. (args[0] is self.)
#    @property, @staticmethod, @classmethod are decorators too — now you know what they do.
# 9. Decorator that registers functions in a dict — a tiny command dispatcher:
#      commands = {}
#      @command("deposit")  def deposit(...)
#      commands["deposit"](...)      <- your menu apps should have worked like this since Day 09
#
# Bonus: contextlib.contextmanager — a decorator that turns a generator into a `with` context
#        manager (Day 17 bonus, in 4 lines). Write  @contextmanager def timer():


# --- your code below ---

