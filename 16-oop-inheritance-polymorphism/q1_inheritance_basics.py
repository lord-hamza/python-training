# Day 16 | OOP 2 - Inheritance & Polymorphism
# Q1 - Inheritance Basics
# ------------------------------------------------------------
# 1. class Animal:  name;  speak() -> "...";  describe() -> "<name> is a <class name>"
#    (use type(self).__name__ so subclasses get the right name for free)
#    class Dog(Animal):  speak() -> "Woof"       class Cat(Animal):  speak() -> "Meow"
#    class Puppy(Dog):  __init__(name, age_weeks) — call super().__init__(name);
#                       speak() -> super().speak() + " (squeaky)"
#    animals = [Dog("Rex"), Cat("Tom"), Puppy("Bit", 6)]
#    Loop and call speak() and describe() on each — same call, different behaviour = polymorphism.
# 2. Print and think about:  isinstance(puppy, Dog), isinstance(puppy, Animal),
#    isinstance(dog, Puppy), issubclass(Puppy, Animal), type(puppy) == Dog, type(puppy) is Puppy
# 3. Employee(name, salary) with annual_pay();  Manager(Employee) adds bonus and OVERRIDES
#    annual_pay() to include it (call super().annual_pay() inside);  Developer(Employee) adds
#    `language`. Print everyone's annual pay from ONE loop with no if/isinstance.
# 4. Method Resolution Order:  print(Puppy.__mro__)  — that's the order Python searches for a method.
# 5. Multiple inheritance:  class Flyer: fly();  class Swimmer: swim();
#    class Duck(Animal, Flyer, Swimmer). Print Duck.__mro__. Call all three methods on a duck.
#    Give Flyer and Swimmer both a  move()  method — which one does Duck get? Swap the base order.
# 6. Override __init__ in a subclass WITHOUT calling super().__init__() — what attribute is
#    missing, what error do you get? Explain in a comment.
# 7. Extend, don't replace: a subclass that adds a method the parent doesn't have, and a subclass
#    that overrides one but still calls the parent's version first.
#
# Bonus: hasattr(obj, "fly"), getattr(obj, "speak")(), object.__subclasses__()


# --- your code below ---

