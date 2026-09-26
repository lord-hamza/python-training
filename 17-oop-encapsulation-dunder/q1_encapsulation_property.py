# Day 17 | OOP 3 - Encapsulation, @property, Dunder Methods
# Q1 - Encapsulation & @property
# ------------------------------------------------------------
# 1. Rewrite BankAccount:
#      balance stored as  self._balance  ("private" by convention)
#      read-only  @property balance
#      deposit/withdraw RAISE (Day 11 exceptions) — no printing inside the class
#    Try  account.balance = 100  from outside — read the AttributeError. Comment: why is that good?
# 2. Name mangling:  self.__secret = "x"  ->  print(account.__secret)  fails,
#    print(account._BankAccount__secret)  works. Comment: single underscore (convention) vs
#    double underscore (mangling) — when to use which. (Most Python code uses single.)
# 3. class Temperature:  stores celsius.
#      @property fahrenheit  (getter computes it)
#      @fahrenheit.setter    (converts back and stores celsius)
#      celsius setter validates  >= -273.15  else ValueError
#    Use the SETTER inside __init__ (self.celsius = value) so validation runs on construction too.
# 4. class Person:  first, last;  @property full_name;  @full_name.setter splits "First Last".
# 5. Shipment (Day 15): make `status` a @property whose SETTER only allows legal transitions
#    (quoted -> dispatched -> picked_up -> delivered; cancel from quoted/dispatched).
#    Raise ValueError otherwise. Now dispatch()/deliver() just do  self.status = "..."
#    Keep the allowed transitions in a class-level dict — no if-chains.
# 6. Read-only computed property:  Rectangle.area  — accessed WITHOUT parentheses. Try
#    rect.area = 5 — read the error.
# 7. @property with a deleter (@x.deleter) — rarely used; just see it exists.
# 8. Comment: Java-style get_balance()/set_balance() vs Python @property — why does Python
#    prefer starting with a plain attribute and adding a property LATER only if needed?
#
# Bonus: functools.cached_property — a property computed once and cached. When would you want it?


# --- your code below ---

