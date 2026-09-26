# Day 21 | Standard Library
# Q1 - datetime, random, math, decimal
# ------------------------------------------------------------
# datetime
#  1. now, today's date, current year. Format:  "Wednesday, 16 September 2026 14:05"  (strftime)
#  2. Parse "2026-09-16" and "16/09/2026" with strptime. Print the weekday name for each.
#  3. delivery_eta(pickup_date, miles) -> pickup + 1 day per 500 miles, counting BUSINESS days
#     only (skip Saturday/Sunday). Use timedelta and .weekday().
#  4. Days until your next birthday. Your age in days. Which of two datetimes is later?
#  5. Naive vs aware:  datetime.now()  vs  datetime.now(timezone.utc). Convert UTC to your zone
#     with zoneinfo.ZoneInfo("America/Chicago"). Comment: why store UTC in a database?
#  6. .isoformat() and datetime.fromisoformat() — the format you'll use in JSON/SQLite.
#  7. Group a list of (date, amount) shipments by month -> {"2026-09": total, ...}
#
# random
#  8. random.choice, random.sample (no repeats), random.shuffle (in place!), random.randint,
#     random.uniform, random.choices(weights=...).  random.seed(42) — what does seeding do and
#     why does it matter for tests?
#  9. Generate 20 fake shipments: random origin/dest from a list of states (origin != dest),
#     random miles 100-3000, random vehicle type, random pickup date in the next 30 days.
# 10. Simulate 10,000 dice rolls; count each face in a dict. Roughly 1/6 each?
#
# math / decimal
# 11. math.ceil/floor/sqrt/pi/log/hypot.  Why is 0.1 + 0.2 != 0.3?  math.isclose().
# 12. Money must NOT be float. Use  decimal.Decimal("0.1") + Decimal("0.2")  and
#     .quantize(Decimal("0.01"), rounding=ROUND_HALF_UP). Rewrite Day 03's quote with Decimal.
#
# Bonus: secrets.token_hex(16) for API keys / passwords — why not random?  uuid.uuid4() for ids.


# --- your code below ---

