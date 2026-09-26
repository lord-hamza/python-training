# Day 18 | OOP 4 - Abstract Classes, classmethod/staticmethod, dataclasses, Composition
# Q3 - LeetCode 232: Implement Queue using Stacks (Easy)
# https://leetcode.com/problems/implement-queue-using-stacks/
# ------------------------------------------------------------
# Implement a FIFO queue using only two stacks, supporting:
#   push(x)   pop() -> int   peek() -> int   empty() -> bool
# You may only use standard stack operations: push to top, pop from top, peek top, size, is empty.
#
# Example:
#   ["MyQueue", "push", "push", "peek", "pop", "empty"]
#   [[],        [1],    [2],    [],     [],    []]
#   -> [null, null, null, 1, 1, False]
#
# Hint: an "in" stack and an "out" stack. Move everything from in -> out ONLY when out is empty.
# Each element moves at most once, so it's amortised O(1).
#
# COMPOSITION rule for today: first write a tiny  class Stack  (push/pop/peek/is_empty/__len__
# wrapping a list), then build MyQueue from TWO Stack objects — not from raw lists.


class Stack:
    pass


class MyQueue:
    def __init__(self):
        # your code here
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def peek(self) -> int:
        pass

    def empty(self) -> bool:
        pass


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())   # expected 1
    print(q.pop())    # expected 1
    print(q.empty())  # expected False
