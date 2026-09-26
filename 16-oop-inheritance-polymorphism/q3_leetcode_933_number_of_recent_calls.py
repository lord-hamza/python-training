# Day 16 | OOP 2 - Inheritance & Polymorphism
# Q3 - LeetCode 933: Number of Recent Calls (Easy)
# https://leetcode.com/problems/number-of-recent-calls/
# ------------------------------------------------------------
# Implement class RecentCounter:
#   ping(t) -> int   adds a new request at time t (milliseconds) and returns the number of
#                    requests that happened in the inclusive range [t - 3000, t].
#   Every call to ping uses a strictly larger t than the previous call.
#
# Example:
#   ["RecentCounter", "ping", "ping", "ping", "ping"]
#   [[],              [1],    [100],  [3001], [3002]]
#   -> [null, 1, 2, 3, 3]
#
# Hint: collections.deque — append t, then popleft() while the oldest is < t - 3000.
# Then len() is the answer. Why is deque better than a list here? (popleft is O(1))


class RecentCounter:
    def __init__(self):
        # your code here
        pass

    def ping(self, t: int) -> int:
        # your code here
        pass


if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(1))     # expected 1
    print(rc.ping(100))   # expected 2
    print(rc.ping(3001))  # expected 3
    print(rc.ping(3002))  # expected 3
