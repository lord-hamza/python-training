# Day 18 | OOP 4 - Abstract Classes, classmethod/staticmethod, dataclasses, Composition
# Q1 - ABCs, @classmethod, @staticmethod
# ------------------------------------------------------------
# 1. from abc import ABC, abstractmethod
#    class Shape(ABC):  @abstractmethod area();  @abstractmethod perimeter();
#                       concrete  describe()  that uses both.
#    Circle, Rectangle, Triangle implement them.
#    Try  Shape()  -> read the TypeError.  Write a subclass that forgets perimeter() -> read THAT error.
#    Comment: what does an ABC give you that a plain base class with  raise NotImplementedError  doesn't?
# 2. class PaymentProcessor(ABC):  abstract  pay(amount) -> str
#    CardProcessor, PayPalProcessor, CashProcessor.
#    checkout(processor: PaymentProcessor, amount)  — doesn't know or care which one it gets.
#    Comment: this is "program to an interface, not an implementation".
# 3. @classmethod as alternative constructors:
#    class Date(y, m, d):  @classmethod from_string("2026-09-16");  @classmethod today()
#    class Shipment:       @classmethod from_dict(d);  @classmethod from_csv_row(row)
#    Notice: cls(...) not Date(...) inside — so subclasses get the right type.
# 4. @staticmethod:  Date.is_valid(y, m, d) -> bool;  Money.convert(amount, rate)  — no self, no cls.
#    Comment: staticmethod vs classmethod vs a plain module-level function — when each?
# 5. Class-level registry with __init_subclass__:
#    class Vehicle:  registry = {}
#        def __init_subclass__(cls, **kw):  super().__init_subclass__(**kw); Vehicle.registry[cls.__name__.lower()] = cls
#    Now  Vehicle.create("suv", ...)  builds the right subclass from a string. No if-chain.
# 6. Class constants + classmethod counters:  Shipment.count_created  incremented in __init__;
#    Shipment.reset_count()  as a classmethod.
#
# Bonus: typing.Protocol — "static duck typing". Define  class Quotable(Protocol): def quote(self, miles: int) -> float
#        and see that Trailer (Day 16) satisfies it without inheriting anything. Compare to ABC.


# --- your code below ---

