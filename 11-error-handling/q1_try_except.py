# Day 11 | Error Handling
# Q1 - Bulletproof Input
# ------------------------------------------------------------
# 1. safe_int(prompt) -> int       keeps asking until the user enters a valid integer (ValueError)
# 2. safe_float(prompt, min_value=None, max_value=None) -> float   also enforces a range
# 3. safe_divide(a, b)            returns a / b, catches ZeroDivisionError, returns None + message
# 4. get_item(items, index)       catches IndexError -> "No such index"; catches TypeError if
#                                 index isn't an int. SEPARATE except blocks. Print the message (as e).
# 5. try / except / else / finally — write one block that uses all four. In a comment explain
#    exactly when `else` runs and when `finally` runs. Test: does finally run if the try block
#    has a `return`? If the exception isn't caught?
# 6. Open a file that doesn't exist -> catch FileNotFoundError. Then add a generic
#    `except Exception as e` AFTER it as a fallback. Explain in a comment why
#    `except Exception:` everywhere (or a bare `except:`) is bad practice.
# 7. Catch multiple types in one line:  except (ValueError, TypeError) as e:
# 8. Re-raise after logging:  except ValueError: print("logging..."); raise
# 9. int("12abc"), int("3.7"), float("3.7"), int(3.7), int(" 42 "), int("") — predict which
#    raise BEFORE running, then run each in try/except and print the exception type name:
#    type(e).__name__
# 10. Print the exception hierarchy for the ones you used:  ValueError.__mro__
#
# Bonus: `except:` vs `except Exception:` — what does the bare one also catch that you almost
#        never want to catch? (KeyboardInterrupt, SystemExit)


# --- your code below ---

