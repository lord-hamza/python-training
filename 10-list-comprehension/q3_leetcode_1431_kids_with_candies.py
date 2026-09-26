# Day 10 | List Comprehension
# Q3 - LeetCode 1431: Kids With the Greatest Number of Candies (Easy)
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# ------------------------------------------------------------
# There are n kids; candies[i] is how many the i-th kid has. You have extraCandies.
# Return a boolean list result where result[i] is True if, after giving the i-th kid ALL
# the extraCandies, they will have the greatest number of candies among all the kids
# (ties count as greatest).
#
# Example 1:  candies = [2, 3, 5, 1, 3], extraCandies = 3  ->  [True, True, True, False, True]
# Example 2:  candies = [4, 2, 1, 1, 2], extraCandies = 1  ->  [True, False, False, False, False]
#
# One-line list comprehension. Compute max(candies) ONCE, outside the comprehension.
# Why does that matter? (hint: max() walks the whole list every time it's called)


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.kidsWithCandies([2, 3, 5, 1, 3], 3))  # expected [True, True, True, False, True]
    print(s.kidsWithCandies([4, 2, 1, 1, 2], 1))  # expected [True, False, False, False, False]
