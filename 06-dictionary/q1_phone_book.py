# Day 06 | Dictionaries
# Q1 - Phone Book (menu app)
# ------------------------------------------------------------
# Build a phone book using a dict and a while-loop menu:
#   1. Add contact    name -> phone. If the name already exists, ask before overwriting.
#   2. Look up        print the phone or "Not found"   (.get() with a default — no crash)
#   3. Delete         .pop(name, None) so it doesn't crash on a missing name
#   4. List all       sorted by name, formatted "Name: phone"
#   5. Search         partial, case-insensitive match on the name
#   6. Count          how many contacts
#   7. Exit
#
# Somewhere in the program also show:  .keys()  .values()  .items()  `in`  len()  .update()
# What happens when you do  book["nobody"]  directly?  (KeyError — catch it properly on Day 11)
#
# Then upgrade: each contact stores more than a phone:
#   book = {"Ali": {"phone": "555-1234", "email": "ali@x.com", "city": "Dallas"}}
# Update Add / Look up / List to handle the nested dict. Add option 8: update ONE field of a contact.
#
# Bonus: dict keys must be hashable — try a list as a key, then a tuple. Which works?
#        Also: dicts remember insertion order (since Python 3.7) — prove it.


# --- your code below ---

