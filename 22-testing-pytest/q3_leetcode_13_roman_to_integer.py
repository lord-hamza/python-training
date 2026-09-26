# Day 22 | Testing with pytest
# Q3 - LeetCode 13: Roman to Integer (Easy) — test-first
# https://leetcode.com/problems/roman-to-integer/
# ------------------------------------------------------------
# I=1  V=5  X=10  L=50  C=100  D=500  M=1000
# Normally larger-to-smaller left to right and you add. Six subtractive cases:
#   IV=4  IX=9  XL=40  XC=90  CD=400  CM=900
# Rule: if a symbol is smaller than the one AFTER it, subtract it instead of adding.
#
# "III" -> 3      "LVIII" -> 58      "MCMXCIV" -> 1994
#
# TODAY'S RULE: write the TESTS FIRST. @pytest.mark.parametrize with the 3 examples plus
# "IV", "IX", "XL", "XC", "CD", "CM", "MMXXVI", "I", "MMMCMXCIX". Run — all red. Then implement.
# Run:   pytest 22-testing-pytest/q3_leetcode_13_roman_to_integer.py -v
#
# Then: implement intToRoman (LeetCode 12) and a ROUND-TRIP test:
#       for n in range(1, 4000): assert romanToInt(intToRoman(n)) == n


class Solution:
    def romanToInt(self, s: str) -> int:
        # your code here
        pass


# --- tests below (pytest collects test_* functions from this file when you pass its path) ---

