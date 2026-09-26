# Day 12 | File Handling
# Q2 - JSON & CSV: Shipment Records
# ------------------------------------------------------------
# shipments = [
#     {"id": 101, "origin": "TX", "dest": "FL", "miles": 1300, "price": 890.0,  "status": "delivered"},
#     ... add 4 more (reuse Day 09) ...
# ]
#
# JSON
# 1. json.dump(shipments, f, indent=2) -> shipments.json. Open the file in your editor and look.
# 2. json.load it back, append a new shipment, dump again.
# 3. json.dumps / json.loads work on STRINGS — show the difference from dump/load in a comment.
# 4. Try to json.dump a dict containing a datetime, then a set. Read the TypeError.
#    Fix with  default=str  (and note what you lose).
# 5. Config file: write settings.json {"currency": "USD", "min_charge": 250, "rates": {...}}
#    and load it at the top of a program. Handle: file missing (use defaults) and invalid JSON
#    (json.JSONDecodeError).
#
# CSV
# 6. Write the same shipments to shipments.csv with csv.DictWriter (write the header row).
#    Open it in your editor / Numbers / Excel.
# 7. Read it back with csv.DictReader. Every value comes back as a STRING — convert miles -> int,
#    price -> float.
# 8. Total revenue and average miles from the CSV.
# 9. Filter rows where origin == "TX" -> tx_shipments.csv
# 10. Read a CSV that uses ";" as the delimiter (write one by hand first). newline="" — why is it
#     required when opening CSV files on some platforms?
# 11. A CSV with a broken row (missing column) — what does DictReader give you? Handle it.
#
# Bonus: convert JSON -> CSV -> JSON and assert the round-trip data is == the original.
#        Then look at what happens to the types after CSV (hint: it isn't equal until you convert).


# --- your code below ---

