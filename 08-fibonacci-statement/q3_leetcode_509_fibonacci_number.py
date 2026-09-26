# Day 08 | Recursion
# Q3 - LeetCode 509: Fibonacci Number (Easy)
# https://leetcode.com/problems/fibonacci-number/
# ------------------------------------------------------------
# F(0) = 0,  F(1) = 1,  F(n) = F(n - 1) + F(n - 2)  for n > 1.
# Given n, return F(n).
#
# Example:  n = 2 -> 1      n = 3 -> 2      n = 4 -> 3      n = 10 -> 55
#
# Solve it 2 ways:
#   (a) recursive  (fib calls fib)
#   (b) iterative with two variables  (a, b = b, a + b)
# Time both with n = 35 using time.perf_counter(). The difference is why Day 20 exists.


class Solution:
    def fib(self, n: int) -> int:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.fib(2))   # expected 1
    print(s.fib(4))   # expected 3
    print(s.fib(10))  # expected 55
