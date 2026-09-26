# Day 08 | Recursion
# Q2 - Recursion Applied
# ------------------------------------------------------------
# Real problems where recursion is the natural fit:
#
#  1. flatten(nested)           [1, [2, [3, [4]]], 5] -> [1, 2, 3, 4, 5]   (any depth)
#  2. binary_search(sorted_list, target, low, high) -> index or -1.  Then time it against a
#     plain  `in`  on a list of 1,000,000 numbers. Comment: O(log n) vs O(n) in one sentence.
#  3. permutations(s)           "abc" -> ["abc", "acb", "bac", "bca", "cab", "cba"]
#  4. subsets(items)            [1, 2, 3] -> [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
#  5. hanoi(n, source, target, spare)  prints the moves for the Tower of Hanoi. n=3 -> 7 moves.
#  6. total_size(folder)        walk a nested dict that represents a folder tree
#       tree = {"docs": {"a.txt": 120, "b.txt": 300, "old": {"c.txt": 50}}, "readme.md": 80}
#     and return the total size. Then  print_tree(tree)  with indentation per level.
#  7. deep_count(nested_list, target)   count how many times target appears at any depth
#  8. Memoisation by hand: fib(n, cache={})  — store results in the dict, look them up first.
#     Time fib(35) again. (You'll formalise this as a decorator on the closures/decorators day.)
#  9. Mutual recursion:  is_even(n) calls is_odd(n - 1) and vice versa. Just to see it.
#
# Bonus: a recursive JSON pretty-printer — walk any nested dict/list and print it with
#        indentation, without json.dumps.


# --- your code below ---

