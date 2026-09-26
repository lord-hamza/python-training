# Day 20 | Closures & Decorators
# Q3 - LeetCode 70: Climbing Stairs (Easy)
# https://leetcode.com/problems/climbing-stairs/
# ------------------------------------------------------------
# You are climbing a staircase with n steps. Each time you can climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
#
# Example:  n = 2 -> 2   (1+1, 2)
#           n = 3 -> 3   (1+1+1, 1+2, 2+1)
#           n = 5 -> 8
#
# Solve it 4 ways, in this order:
#   1. Naive recursion:  ways(n) = ways(n-1) + ways(n-2).  Try n = 40. Wait. Give up.
#   2. Add YOUR @memoize decorator from Q1 on top of the SAME function -> instant.
#   3. @functools.lru_cache(maxsize=None) version.
#   4. Bottom-up iterative with two variables — it's Fibonacci in disguise.
# Comment: which one would you submit and why?


class Solution:
    def climbStairs(self, n: int) -> int:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(2))   # expected 2
    print(s.climbStairs(3))   # expected 3
    print(s.climbStairs(5))   # expected 8
    print(s.climbStairs(45))  # expected 1836311903
