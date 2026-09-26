# Day 04 | Loops
# Q3 - LeetCode 1281: Subtract the Product and Sum of Digits of an Integer (Easy)
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# ------------------------------------------------------------
# Given an integer n, return the difference between the PRODUCT of its digits and the SUM
# of its digits.
#
# Example 1:  n = 234   ->  product 2*3*4 = 24,  sum 2+3+4 = 9   ->  24 - 9 = 15
# Example 2:  n = 4421  ->  product 32,  sum 11   ->  21
#
# Solve it with a while loop that peels off one digit at a time:
#     digit = n % 10      n = n // 10
# Then a second way: loop over str(n) and convert each character back to int.
#
# Also do 04-fizz-buzz/q3_leetcode_412_fizz_buzz.py today — same folder rules apply.


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.subtractProductAndSum(234))   # expected 15
    print(s.subtractProductAndSum(4421))  # expected 21
