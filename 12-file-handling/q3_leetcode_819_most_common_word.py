# Day 12 | File Handling
# Q3 - LeetCode 819: Most Common Word (Easy)
# https://leetcode.com/problems/most-common-word/
# ------------------------------------------------------------
# Given a string paragraph and a list of banned words, return the most frequent word that
# is NOT banned. It is guaranteed there's at least one non-banned word and the answer is unique.
# Words are case-insensitive, punctuation is not part of a word, and the answer is lowercase.
#
# Example:  paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
#           banned = ["hit"]
#           ->  "ball"
#
# Steps: lowercase -> replace each punctuation char "!?',;." with a space -> split -> count with a
# dict skipping banned -> pick the max.
#
# Extra: read the paragraph from a text file (paragraph.txt) instead of a string, and read the
# banned words from banned.txt (one per line).


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # your code here
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))  # expected ball
    print(s.mostCommonWord("a.", []))  # expected a
