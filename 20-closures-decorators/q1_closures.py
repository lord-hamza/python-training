# Day 20 | Closures & Decorators
# Q1 - Closures
# ------------------------------------------------------------
# 1. make_counter():  count = 0;  inner inc() does  nonlocal count; count += 1; return count;
#    return inc.   c1 = make_counter(); c2 = make_counter()  — call each a few times. Independent. Why?
# 2. Remove `nonlocal` — read the UnboundLocalError. Comment: LEGB — Local, Enclosing, Global,
#    Built-in — the order Python looks up a name.
# 3. make_multiplier(n) from Day 09. Inspect:  double.__closure__[0].cell_contents  -> 2
# 4. make_rate_limiter(max_calls) -> a function that returns True for the first max_calls calls
#    and False after. (A closure holding state.)
# 5. The classic trap:  funcs = [lambda: i for i in range(3)]  — call each. All return 2!
#    Fix with a default arg:  lambda i=i: i.  Comment: "late binding" in one sentence.
# 6. Closure vs class: write the counter as  class Counter  with __call__. Which do you prefer
#    for tiny state? For lots of state?
# 7. make_validator(min_len, pattern) -> a function is_valid(text). Build 3 validators from it.
# 8. memoize(func):  cache = {}  in the closure; inner wrapper looks up args in cache before
#    calling func. Wrap fib. Time fib(35) before and after.
#    ...that IS a decorator. You just wrote one. Q2 formalises it.
# 9. functools.partial:  quote_sedan = partial(calculate_quote, vehicle_type="sedan")
#    — not a closure, but solves the same problem. Compare.
#
# Bonus: a closure that "remembers" a config dict and returns a formatter function:
#        fmt = make_money_formatter(symbol="$", decimals=2);  fmt(1234.5) -> "$1,234.50"


# --- your code below ---

