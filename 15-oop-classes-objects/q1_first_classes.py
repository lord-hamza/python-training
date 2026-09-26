# Day 15 | OOP 1 - Classes & Objects
# Q1 - Your First Classes
# ------------------------------------------------------------
# 1. class Dog:  __init__(self, name, age);  bark() -> "Rex says woof";  birthday() -> age += 1
#    Create 2 dogs, call the methods, print their attributes. Print the dog object itself —
#    ugly? That's fixed on Day 17 (__str__).
# 2. class BankAccount:  owner, balance (default 0);  deposit(amount), withdraw(amount) with
#    validation (raise your Day 11 exceptions);  show_balance().
#    Move your Day 11 banking functions INTO this class — notice `balance` is no longer passed
#    around, it lives on `self`.
# 3. class Rectangle:  width, height;  area(), perimeter(), is_square();  scale(factor) modifies
#    the object in place. Then make  scaled(factor)  that RETURNS a new Rectangle instead.
#    Comment: mutating vs returning new — which is safer?
# 4. class Counter:  starts at 0;  increment(), reset(), get().  Create two Counters — prove they
#    don't share state.
# 5. Class attribute vs instance attribute:
#       class Car:  wheels = 4  (class attr);  __init__ sets self.make (instance attr)
#    Change Car.wheels, then change wheels on ONE instance. Print wheels for both instances.
#    Explain in a comment what happened.
# 6. What is `self`? Call a method the long way:  Dog.bark(rex)  — it's the same thing.
#    Add a method with no self — call it on an instance — read the error.
# 7. Give Dog a class attribute  count = 0  that __init__ increments, so Dog.count tells you how
#    many dogs exist.
# 8. Add attributes dynamically:  rex.color = "brown"  — works. Is that a good idea? Why not?
#
# Bonus: vars(rex) / rex.__dict__  — an object is (roughly) a dict of attributes + a class.
#        type(rex), rex.__class__.__name__, isinstance(rex, Dog)


# --- your code below ---

