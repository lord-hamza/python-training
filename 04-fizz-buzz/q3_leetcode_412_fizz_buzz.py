# Day 04 | Loops
# Q3 - LeetCode 412: Fizz Buzz (Easy)
# https://leetcode.com/problems/fizz-buzz/
# ------------------------------------------------------------
# Given an integer n, return a string list `answer` (1-indexed) where:
#   answer[i] == "FizzBuzz"  if i is divisible by 3 and 5
#   answer[i] == "Fizz"      if i is divisible by 3
#   answer[i] == "Buzz"      if i is divisible by 5
#   answer[i] == str(i)      otherwise
#
# Example:  n = 5   ->  ["1","2","Fizz","4","Buzz"]
#           n = 15  ->  ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
#
# Hint: start with  result = []  and  result.append(...)  inside a for loop over range(1, n + 1).
# Careful with the ORDER of your if/elif checks.


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(5))   # expected ['1', '2', 'Fizz', '4', 'Buzz']
    print(s.fizzBuzz(15))  # expected [... '13', '14', 'FizzBuzz']
