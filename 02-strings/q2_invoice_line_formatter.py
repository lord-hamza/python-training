# Day 02 | Strings
# Q2 - Invoice Line Formatter
# ------------------------------------------------------------
# item       = "Car transport - Dallas to Miami"
# qty        = 2
# unit_price = 849.5
#
# Part A — fixed-width table row using f-string alignment:
#   item left-aligned & padded to 35 chars   -> f"{item:<35}"
#   qty right-aligned to 5                   -> f"{qty:>5}"
#   unit price right-aligned to 10, 2 dp     -> f"{unit_price:>10.2f}"
#   line total right-aligned to 12, 2 dp
#   Print a header row, a separator line ("-" * width), then the row:
#
#   Item                                 Qty  Unit Price   Line Total
#   ------------------------------------------------------------------
#   Car transport - Dallas to Miami        2      849.50      1699.00
#
#   Add 2 more rows with different items so the columns line up.
#
# Part B — build a URL slug from the item name:
#   "Car transport - Dallas to Miami"  ->  "car-transport-dallas-to-miami"
#   (lowercase, " - " becomes " ", spaces become "-")   .lower() .replace()
#
# Part C — split & join:
#   sentence = "the quick brown fox"
#   Capitalise every word WITHOUT .title():  .split() -> .capitalize() each -> " ".join()
#   (you don't have loops yet — do it for the 4 words by hand, e.g. words[0].capitalize())
#   Print the number of words. Join them with "_" instead.
#
# Part D — multi-line strings & escapes:
#   Print a 3-line address using one triple-quoted string. Print a path with a backslash
#   ("C:\new\folder") — why does it break? Fix with a raw string r"..." or "\\".
#   Print a tab-separated line using \t.
#
# Bonus: format a number with thousands separators:  f"{1234567.891:,.2f}"  ->  1,234,567.89
#        and a percentage:  f"{0.0825:.1%}"  ->  8.2%


# --- your code below ---

