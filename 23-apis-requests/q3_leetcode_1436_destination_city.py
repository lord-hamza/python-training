# Day 23 | APIs & JSON
# Q3 - LeetCode 1436: Destination City (Easy)
# https://leetcode.com/problems/destination-city/
# ------------------------------------------------------------
# You are given paths, where paths[i] = [cityA_i, cityB_i] means there's a direct path from
# cityA_i to cityB_i. Return the destination city — the city with NO outgoing path.
# The paths form a single line with no loops, so exactly one such city exists.
#
# Example 1:  [["London","New York"], ["New York","Lima"], ["Lima","Sao Paulo"]]  ->  "Sao Paulo"
# Example 2:  [["B","C"], ["D","B"], ["C","A"]]  ->  "A"
#
# Hint: a set of every origin city; the answer is the destination that isn't in it.
#
# Extra: represent the paths as a dict {origin: dest}, find the START city (never a destination),
# and walk the chain to print the full route:  London -> New York -> Lima -> Sao Paulo.
# That's how you'd chain multi-leg shipments.


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))  # expected Sao Paulo
    print(s.destCity([["B", "C"], ["D", "B"], ["C", "A"]]))                                    # expected A
