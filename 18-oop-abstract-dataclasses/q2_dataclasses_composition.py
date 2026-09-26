# Day 18 | OOP 4 - Abstract Classes, classmethod/staticmethod, dataclasses, Composition
# Q2 - dataclasses & Composition over Inheritance
# ------------------------------------------------------------
# from dataclasses import dataclass, field, asdict
#
# 1. @dataclass class Customer:  name, email, phone = ""
#    @dataclass class Vehicle:   make, model, year, vin
#    @dataclass class Shipment:  id, customer: Customer, vehicle: Vehicle, origin, dest, miles,
#                                status = "quoted", notes: list[str] = field(default_factory=list)
#    You get __init__, __repr__, __eq__ for FREE. Print one. Compare two equal ones with ==.
#    Why  field(default_factory=list)  and not  notes = []  ? (the Day 09 mutable-default bug)
# 2. @dataclass(frozen=True) class Point  -> try to mutate -> FrozenInstanceError. Now hashable.
#    @dataclass(order=True)  -> sorted() works (compares fields in order).
# 3. Dataclasses are normal classes: add a  price  @property to Shipment (Day 07 rules) and a
#    __post_init__ that raises ValueError if miles <= 0 or vin isn't 17 chars.
# 4. COMPOSITION ("has-a") instead of inheritance ("is-a"):
#    class Driver:      name, license_no, current_shipment: Shipment | None = None
#    class Dispatcher:  has a list of drivers and a list of shipments;
#                       assign(shipment, driver) — driver must be free; sets both sides
#                       available_drivers() -> list
#    class Invoice:     built FROM a Shipment (takes it in __init__), computes line items
#                       (transport, crate fee, enclosed surcharge...) and total; render() -> str
#                       Invoice does NOT inherit from Shipment. Comment: why not?
# 5. asdict(shipment) -> json.dumps  (nested dataclasses serialise fine). Then rebuild the object
#    from the dict — Customer and Vehicle are nested, handle that (a from_dict classmethod).
# 6. Comment, one line each — when would you pick:  dict  /  tuple  /  NamedTuple  /  dataclass  /  full class?
#
# Bonus: @dataclass(slots=True) — what are __slots__ and why do they save memory?
#        dataclasses.replace(obj, status="delivered") — copy with one field changed.


# --- your code below ---

