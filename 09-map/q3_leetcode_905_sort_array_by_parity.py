# Day 09 | Functions Advanced (map, filter, lambda)
# Q3 - LeetCode 905: Sort Array By Parity (Easy)
# https://leetcode.com/problems/sort-array-by-parity/
# ------------------------------------------------------------
# Given an integer array nums, move all the even integers to the beginning of the array
# followed by all the odd integers. Return ANY array that satisfies this.
#
# Example 1:  [3, 1, 2, 4]  ->  [2, 4, 3, 1]    ([4, 2, 3, 1], [2, 4, 1, 3] ... also accepted)
# Example 2:  [0]           ->  [0]
#
# Solve it 3 ways:
#   (a) one line:  sorted() with a key lambda  (hint:  x % 2)
#   (b) filter() twice and concatenate the lists
#   (c) in place with two pointers (left/right) and swapping — no new list


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.sortArrayByParity([3, 1, 2, 4]))  # expected evens first, e.g. [2, 4, 3, 1]
    print(s.sortArrayByParity([0]))           # expected [0]
