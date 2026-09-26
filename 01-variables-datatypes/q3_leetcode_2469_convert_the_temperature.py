# Day 01 | Variables & Data Types
# Q3 - LeetCode 2469: Convert the Temperature (Easy)
# https://leetcode.com/problems/convert-the-temperature/
# ------------------------------------------------------------
# You are given a non-negative floating point number `celsius`.
# Return a list [kelvin, fahrenheit] where:
#   Kelvin     = Celsius + 273.15
#   Fahrenheit = Celsius * 1.80 + 32.00
#
# Example 1:  celsius = 36.50   ->  [309.65, 97.70]
# Example 2:  celsius = 122.11  ->  [395.26, 251.798]
#
# NOTE: LeetCode wraps every solution in `class Solution` with a method.
# You haven't learned functions (Day 07) or classes (Day 15) yet — ignore that
# part. Just write your code where it says "your code here" and hand the answer
# back with:   return [kelvin, fahrenheit]
# Run this file to test, then paste the class into LeetCode and submit.


class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.convertTemperature(36.50))   # expected [309.65, 97.7]
    print(s.convertTemperature(122.11))  # expected [395.26, 251.798]
