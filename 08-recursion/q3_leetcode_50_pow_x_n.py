# Day 08 | Recursion
# Q3 - LeetCode 50: Pow(x, n) (Medium)
# https://leetcode.com/problems/powx-n/
# ------------------------------------------------------------
# Implement pow(x, n), which calculates x raised to the power n.  n can be negative.
#
# Example 1:  x = 2.0,  n = 10   ->  1024.0
# Example 2:  x = 2.1,  n = 3    ->  9.261
# Example 3:  x = 2.0,  n = -2   ->  0.25
#
# 1. First the obvious loop (multiply n times). It's too slow for n = 2**31 - 1 — LeetCode will
#    time out. That's the point.
# 2. Recursive "fast exponentiation":
#      pow(x, n) = pow(x * x, n // 2)          if n is even
#      pow(x, n) = x * pow(x * x, n // 2)      if n is odd
#    Base case n == 0 -> 1. Negative n -> 1 / pow(x, -n).
#    Comment: how many recursive calls for n = 1,000,000? (hint: log2)
# Don't use ** or math.pow — that defeats the exercise.


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.0, 10))  # expected 1024.0
    print(s.myPow(2.1, 3))   # expected 9.261
    print(s.myPow(2.0, -2))  # expected 0.25
