# Day 11 | Error Handling
# Q3 - LeetCode 8: String to Integer (atoi)  [MEDIUM]
# https://leetcode.com/problems/string-to-integer-atoi/
# ------------------------------------------------------------
# This one is Medium — it's really an exercise in handling messy input gracefully.
# Implement myAtoi(s):
#   1. Ignore leading whitespace
#   2. Optional single '+' or '-' sign
#   3. Read digits until the first non-digit (or end). No digits at all -> 0
#   4. Clamp to the 32-bit signed range  [-2**31, 2**31 - 1]
#
# "42"             ->  42
# "   -042"        ->  -42
# "1337c0d3"       ->  1337
# "0-1"            ->  0
# "words and 987"  ->  0
# "-91283472332"   ->  -2147483648   (clamped)
#
# RULE: do NOT call int() on the whole string. Walk it character by character with an
# index — that's the point. str.isdigit() on a single char is fine.


class Solution:
    def myAtoi(self, s: str) -> int:
        # your code here
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("42"))             # expected 42
    print(sol.myAtoi("   -042"))        # expected -42
    print(sol.myAtoi("1337c0d3"))       # expected 1337
    print(sol.myAtoi("0-1"))            # expected 0
    print(sol.myAtoi("words and 987"))  # expected 0
    print(sol.myAtoi("-91283472332"))   # expected -2147483648
