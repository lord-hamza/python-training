# Day 14 | Git Workflow
# Q3 - LeetCode 20: Valid Parentheses (Easy)
# https://leetcode.com/problems/valid-parentheses/
# ------------------------------------------------------------
# Given a string s containing only '(', ')', '{', '}', '[' and ']', determine if it is valid:
#   - open brackets must be closed by the SAME type of bracket
#   - open brackets must be closed in the CORRECT order
#   - every close bracket has a corresponding open bracket
#
# "()"      ->  True        "()[]{}"  ->  True        "(]"    ->  False
# "([)]"    ->  False       "{[]}"    ->  True        "(("    ->  False
#
# Hint: a STACK (a list with .append / .pop) and a dict mapping each closer to its opener.
# Push openers; on a closer, pop and compare. At the end the stack must be empty.
#
# GIT RULE for this file: solve it on a branch  feature/valid-parentheses, commit, merge into
# main, delete the branch, push. From today, every day's work goes through a branch.


class Solution:
    def isValid(self, s: str) -> bool:
        # your code here
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))      # expected True
    print(sol.isValid("()[]{}"))  # expected True
    print(sol.isValid("(]"))      # expected False
    print(sol.isValid("([)]"))    # expected False
    print(sol.isValid("{[]}"))    # expected True
