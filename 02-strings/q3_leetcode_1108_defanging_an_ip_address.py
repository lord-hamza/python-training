# Day 02 | Strings
# Q3 - LeetCode 1108: Defanging an IP Address (Easy)
# https://leetcode.com/problems/defanging-an-ip-address/
# ------------------------------------------------------------
# Given a valid (IPv4) IP address, return a defanged version of it.
# A defanged IP address replaces every period "." with "[.]".
#
# Example 1:  "1.1.1.1"       ->  "1[.]1[.]1[.]1"
# Example 2:  "255.100.50.0"  ->  "255[.]100[.]50[.]0"
#
# Solve it twice:
#   (a) with .replace()
#   (b) without .replace() — use .split(".") and "[.]".join(...)


class Solution:
    def defangIPaddr(self, address: str) -> str:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.defangIPaddr("1.1.1.1"))       # expected 1[.]1[.]1[.]1
    print(s.defangIPaddr("255.100.50.0"))  # expected 255[.]100[.]50[.]0
