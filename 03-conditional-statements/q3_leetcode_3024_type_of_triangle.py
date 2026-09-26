# Day 03 | Conditionals
# Q3 - LeetCode 3024: Type of Triangle (Easy)
# https://leetcode.com/problems/type-of-triangle/
# ------------------------------------------------------------
# You are given an integer array nums of size 3 which can form the sides of a triangle.
#   - "equilateral"  if all three sides are equal
#   - "isosceles"    if exactly two sides are equal
#   - "scalene"      if all sides are different
#   - "none"         if the sides cannot form a triangle
# A triangle is valid only if the sum of ANY two sides is greater than the third side.
#
# Example 1:  [3, 3, 3]  ->  "equilateral"
# Example 2:  [3, 4, 5]  ->  "scalene"
# Example 3:  [1, 2, 3]  ->  "none"        (1 + 2 is not > 3)
#
# Lists are Day 05 — all you need today is indexing:  nums[0], nums[1], nums[2]
# Check validity FIRST, then the type.


class Solution:
    def triangleType(self, nums: list[int]) -> str:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.triangleType([3, 3, 3]))  # expected equilateral
    print(s.triangleType([3, 4, 5]))  # expected scalene
    print(s.triangleType([1, 2, 3]))  # expected none
    print(s.triangleType([3, 3, 5]))  # expected isosceles
