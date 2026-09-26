# Day 13 | Modules & Packages
# Q3 - LeetCode 169: Majority Element (Easy)
# https://leetcode.com/problems/majority-element/
# ------------------------------------------------------------
# Given an array nums of size n, return the majority element — the one that appears
# MORE than n / 2 times. It always exists.
#
# Example 1:  [3, 2, 3]              ->  3
# Example 2:  [2, 2, 1, 1, 1, 2, 2]  ->  2
#
# Solve 3 ways:
#   (a) a dict counting occurrences (Day 06)
#   (b) one line with the stdlib:  collections.Counter(nums).most_common(1)
#   (c) Boyer-Moore Voting Algorithm — O(1) extra space. Google it, understand it, implement it.


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))              # expected 3
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # expected 2
