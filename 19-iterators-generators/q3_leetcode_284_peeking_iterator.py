# Day 19 | Iterators & Generators
# Q3 - LeetCode 284: Peeking Iterator (Medium)
# https://leetcode.com/problems/peeking-iterator/
# ------------------------------------------------------------
# Design an iterator that supports peek() on top of an existing iterator that has
# next() and hasNext():
#   PeekingIterator(iterator)
#   next()    -> returns the next element and moves the pointer
#   peek()    -> returns the next element WITHOUT moving the pointer
#   hasNext() -> True if there are still elements
#
# Example:
#   ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
#   [[[1, 2, 3]],       [],     [],     [],     [],     []]
#   -> [null, 1, 2, 2, 3, False]
#
# Hint: cache ONE element ahead in __init__ and after every next().
# The Iterator class below is what LeetCode gives you — don't change it.


class Iterator:
    def __init__(self, nums):
        self._nums = nums
        self._i = 0

    def hasNext(self) -> bool:
        return self._i < len(self._nums)

    def next(self) -> int:
        value = self._nums[self._i]
        self._i += 1
        return value


class PeekingIterator:
    def __init__(self, iterator: Iterator):
        # your code here
        pass

    def peek(self) -> int:
        pass

    def next(self) -> int:
        pass

    def hasNext(self) -> bool:
        pass


if __name__ == "__main__":
    pi = PeekingIterator(Iterator([1, 2, 3]))
    print(pi.next())     # expected 1
    print(pi.peek())     # expected 2
    print(pi.next())     # expected 2
    print(pi.next())     # expected 3
    print(pi.hasNext())  # expected False
