# Day 22 | Testing with pytest
# Q2 - Testing Classes, Fixtures, Mocking
# ------------------------------------------------------------
# Run:   pytest 22-testing-pytest/q2_fixtures_mocking_classes.py -v
#
#  1. Copy BankAccount (Day 17) here. Tests:
#       deposit increases balance / withdraw decreases / withdraw over balance raises
#       InsufficientFundsError / negative amount raises / balance is read-only (AttributeError)
#  2. @pytest.fixture  def account():  return BankAccount("Hamza", 100)   — inject it into every
#     test instead of rebuilding. Comment: does each test get a FRESH account? Prove it.
#  3. Copy Shipment with the status property (Day 17). Parametrize the LEGAL transitions in one
#     test and the ILLEGAL ones in another (expecting ValueError).
#  4. A function that writes a report file — test it with pytest's built-in  tmp_path  fixture.
#     Assert on the file's content. Nothing touches your real disk.
#  5. Mocking: fetch_fuel_rate() would call an API. In the test, replace it:
#       monkeypatch.setattr(module_or_object, "fetch_fuel_rate", lambda: 0.85)
#     or  unittest.mock.patch. Assert quote() used the fake value. Comment: why mock?
#  6. Test input()-driven code:  monkeypatch.setattr("builtins.input", lambda _: "42")
#  7. Test printed output:  capsys  fixture ->  captured = capsys.readouterr(); assert "..." in captured.out
#  8. Group related tests in a class:  class TestBankAccount:  (methods still start with test_)
#  9. A yield fixture with setup + teardown (print before/after; or create/delete a temp file).
# 10. conftest.py at the repo root with a shared fixture; pytest.ini / pyproject.toml with
#     testpaths. Run ALL tests from the repo root with just:  pytest
#
# Bonus: pip install pytest-cov;  pytest --cov=. --cov-report=term-missing  — what's uncovered?
#        Add tests until this file's code is 100%.  Also: pytest.mark.skip / xfail — when?


# --- your code below ---

