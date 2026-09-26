# Day 06 | Dictionaries
# Q3 - LeetCode 242: Valid Anagram (Easy)
# https://leetcode.com/problems/valid-anagram/
# ------------------------------------------------------------
# Given two strings s and t, return True if t is an anagram of s, False otherwise.
# (An anagram uses exactly the same letters the same number of times.)
#
# Example 1:  s = "anagram", t = "nagaram"  ->  True
# Example 2:  s = "rat",     t = "car"      ->  False
#
# Solve with a dict that counts characters (that's the point of today).
# sorted(s) == sorted(t) also works — do that afterwards as a check, and think about which
# is faster for very long strings.
#
# THEN: go back to 05-lists/q3_leetcode_1_two_sum.py and solve Two Sum in one pass
# with a dict  {value: index}  — for each number, check if  target - number  is already in it.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # your code here
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # expected True
    print(sol.isAnagram("rat", "car"))          # expected False
