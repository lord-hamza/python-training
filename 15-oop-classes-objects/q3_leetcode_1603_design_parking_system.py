# Day 15 | OOP 1 - Classes & Objects
# Q3 - LeetCode 1603: Design Parking System (Easy)
# https://leetcode.com/problems/design-parking-system/
# ------------------------------------------------------------
# A parking lot has three kinds of spaces: big, medium, small, with a fixed number of each.
#   ParkingSystem(big, medium, small)  -> number of slots of each size
#   addCar(carType) -> bool             carType: 1 = big, 2 = medium, 3 = small.
#                                        Return True if a slot of that size is free (and take it),
#                                        otherwise False.
#
# Example:
#   ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
#   [[1, 1, 0],       [1],      [2],      [3],      [1]]
#   -> [null, True, True, False, False]
#
# Hint: store the three counts in a list and index it with carType - 1.


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        # your code here
        pass

    def addCar(self, carType: int) -> bool:
        # your code here
        pass


if __name__ == "__main__":
    p = ParkingSystem(1, 1, 0)
    print(p.addCar(1))  # expected True
    print(p.addCar(2))  # expected True
    print(p.addCar(3))  # expected False
    print(p.addCar(1))  # expected False
