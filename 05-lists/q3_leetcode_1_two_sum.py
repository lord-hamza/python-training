# Day 05 | Lists, Tuples & Sets
# Q3 - LeetCode 1: Two Sum (Easy)
# https://leetcode.com/problems/two-sum/
# ------------------------------------------------------------
# Given an array of integers nums and an integer target, return the INDICES of the
# two numbers that add up to target. Exactly one solution exists, and you may not
# use the same element twice. Return the answer in any order.
#
# Example 1:  nums = [2, 7, 11, 15], target = 9   ->  [0, 1]      (2 + 7 = 9)
# Example 2:  nums = [3, 2, 4],      target = 6   ->  [1, 2]
# Example 3:  nums = [3, 3],         target = 6   ->  [0, 1]
#
# TODAY: solve it with two nested loops (brute force, O(n^2)). Make sure j starts after i.
# DAY 06 (dictionary): come back and solve it in ONE pass with a dictionary {value: index}.
#         That's the answer interviewers want — this is the most-asked question on LeetCode.


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # expected [0, 1]
    print(s.twoSum([3, 2, 4], 6))       # expected [1, 2]
    print(s.twoSum([3, 3], 6))          # expected [0, 1]
