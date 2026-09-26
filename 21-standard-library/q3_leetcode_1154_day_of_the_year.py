# Day 21 | Standard Library
# Q3 - LeetCode 1154: Day of the Year (Easy)
# https://leetcode.com/problems/day-of-the-year/
# ------------------------------------------------------------
# Given a string date in the format YYYY-MM-DD, return the day number of the year.
#
# Example 1:  "2019-01-09"  ->  9
# Example 2:  "2019-02-10"  ->  41
# Example 3:  "2004-03-01"  ->  61   (2004 is a leap year)
#
# Solve it 2 ways:
#   (a) with datetime:  strptime/fromisoformat, then  .timetuple().tm_yday  or subtract Jan 1st
#   (b) WITHOUT datetime: a list of month lengths + the leap-year rule
#       (divisible by 4, EXCEPT centuries, EXCEPT centuries divisible by 400)


class Solution:
    def dayOfYear(self, date: str) -> int:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.dayOfYear("2019-01-09"))  # expected 9
    print(s.dayOfYear("2019-02-10"))  # expected 41
    print(s.dayOfYear("2004-03-01"))  # expected 61
    print(s.dayOfYear("1900-03-01"))  # expected 60  (1900 is NOT a leap year)
