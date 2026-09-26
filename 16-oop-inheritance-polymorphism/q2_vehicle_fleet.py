# Day 16 | OOP 2 - Inheritance & Polymorphism
# Q2 - Vehicle Fleet: Polymorphism in Practice
# ------------------------------------------------------------
# Base class Vehicle:  make, model, year, vin
#   transport_rate() -> 0.60 (per mile)
#   quote(miles)     -> miles * self.transport_rate()
#   describe()       -> "2020 Toyota Camry (VIN123)"
#   __init__ validates:  year between 1900 and next year, vin exactly 17 chars -> raise ValueError
#
# Subclasses that each override transport_rate() (and add attributes where it makes sense):
#   Sedan        -> 0.60
#   SUV          -> 0.75
#   PickupTruck  -> 0.95, extra attribute bed_length
#   Motorcycle   -> 0.45, and quote() adds a $100 crate fee — override quote() and call super()
#
# Inoperable vehicles cost +$150. Is "InoperableVehicle" a SUBCLASS, or an `operable` FLAG on
# Vehicle that quote() checks? Decide, implement it, and justify in a comment.
# (Hint: an inoperable SUV is still an SUV. Inheritance models "is-a".)
#
# fleet = [ ...6 mixed vehicles... ]
# 1. Print a 1000-mile quote for every vehicle in ONE loop — no isinstance, no if on type.
# 2. Now write the same thing the BAD way: one function with if/elif on type(v). Then write a
#    comment about what happens to that function when you add 5 more vehicle types.
# 3. total_quote(vehicles, miles) -> works for any mix.
# 4. Duck typing: an unrelated class Trailer with its own quote(miles) — put one in the fleet.
#    Does your loop still work? Why doesn't Python care that it's not a Vehicle?
# 5. cheapest_vehicle(fleet, miles) using min() with a key.
# 6. Group the fleet by class name into a dict:  {"SUV": [...], "Sedan": [...]}
#
# Bonus: @classmethod  from_string(cls, "Toyota,Camry,2020,VIN...")  on Vehicle — and notice it
#        returns the right subclass when called as SUV.from_string(...). (Day 18 goes deeper.)


# --- your code below ---

