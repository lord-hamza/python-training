# Day 22 | Testing with pytest
# Q1 - pytest Basics
# ------------------------------------------------------------
# In your venv:  python -m pip install pytest     (add it to requirements.txt)
# Write the code AND the tests in this file.  Run:   pytest 22-testing-pytest/q1_pytest_basics.py -v
#
# Code under test (copy from earlier days):
#   add(a, b)      divide(a, b) -> raises ZeroDivisionError      is_palindrome(s)      slugify(s)
#   calculate_quote(distance, vehicle_type, is_operable, enclosed)   (Day 07)
#
# Tests — functions whose names start with  test_ :
#  1. Plain asserts:  assert add(2, 3) == 5.  Write 3 tests per function INCLUDING edge cases
#     (empty string, 0, negative numbers, unicode, whitespace).
#  2. Expected errors:
#       with pytest.raises(ZeroDivisionError): divide(1, 0)
#       with pytest.raises(ValueError, match="Unknown vehicle"): calculate_quote(100, "boat", True, False)
#  3. @pytest.mark.parametrize("text, expected", [...])  — test slugify with 6 inputs in ONE test.
#  4. Floats:  assert calculate_quote(1300, "suv", True, True) == pytest.approx(1365.0)
#  5. Write a test that FAILS on purpose. Read the output carefully — pytest shows you the values.
#     Then fix it.
#  6. Run each and note in a comment what it does:
#       pytest -v        pytest -x        pytest -k slug        pytest --lf        pytest -q
#  7. Naming: a test name should say what it checks:  test_withdraw_more_than_balance_raises
#     — rename yours.
#  8. Arrange / Act / Assert — restructure one test with those three comment sections.
#
# Bonus (TDD): write the test for  parse_vin(vin) -> dict  FIRST (it fails: red), then implement
#        the minimum to pass (green), then clean up (refactor). Rules: 17 chars, no I/O/Q,
#        chars 1-3 = manufacturer, char 10 = model year code.


# --- your code below ---

