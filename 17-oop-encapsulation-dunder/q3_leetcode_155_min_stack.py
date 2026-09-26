# Day 17 | OOP 3 - Encapsulation, @property, Dunder Methods
# Q3 - LeetCode 155: Min Stack (Medium — but easy with the right idea)
# https://leetcode.com/problems/min-stack/
# ------------------------------------------------------------
# Design a stack that supports push, pop, top, and retrieving the minimum element —
# ALL in O(1) time.
#   MinStack()      push(val)      pop()      top() -> int      getMin() -> int
#
# Example:
#   ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
#   [[],         [-2],   [0],    [-3],   [],       [],    [],    []]
#   -> [null, null, null, null, -3, null, 0, -2]
#
# Hint: keep a SECOND stack that stores the minimum "so far" at each level. Push to it
# min(val, current_min); pop both together.
# Add __len__ and __repr__ so you can print it — today's topic.


class MinStack:
    def __init__(self):
        # your code here
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin())  # expected -3
    ms.pop()
    print(ms.top())     # expected 0
    print(ms.getMin())  # expected -2
