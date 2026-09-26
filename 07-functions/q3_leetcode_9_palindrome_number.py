# Day 07 | Functions
# Q3 - LeetCode 9: Palindrome Number (Easy)
# https://leetcode.com/problems/palindrome-number/
# ------------------------------------------------------------
# Given an integer x, return True if x is a palindrome (reads the same backward and forward).
#
# Example 1:  121   ->  True
# Example 2:  -121  ->  False   (reads as 121- backward)
# Example 3:  10    ->  False
#
# Solve it twice:
#   (a) the easy way: convert to str and compare with its reverse
#   (b) WITHOUT converting to a string — write a helper function  reverse_number(n) -> int
#       that peels digits off with  % 10  and  // 10, then compare. That's the interview answer.
# Keep the helper as its own function with a docstring — today is about functions.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))   # expected True
    print(s.isPalindrome(-121))  # expected False
    print(s.isPalindrome(10))    # expected False
    print(s.isPalindrome(0))     # expected True
