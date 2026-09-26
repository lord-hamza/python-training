# Day 05 | Lists, Tuples & Sets
# Q1 - Lists: Shopping Cart & Gradebook
# ------------------------------------------------------------
# Part A — cart = ["laptop", "mouse", "keyboard"]. Do each step, print the cart after it:
#   1. Add "monitor" to the end                         (.append)
#   2. Insert "webcam" at index 1                       (.insert)
#   3. Remove "mouse"                                   (.remove)
#   4. Replace "keyboard" with "mechanical keyboard"    (index assignment)
#   5. Print it sorted WITHOUT changing it (sorted()), then the original; then .sort() in place
#   6. Last item with a negative index; first two items (slice); whole cart reversed (slice -1)
#   7. Is "laptop" in the cart?  Print its index (.index)
#   8. .extend(["cable", "hub"]) — what happens if you .append a list instead?
#   9. .pop() the last item and print it; .pop(0)
#  10. prices = [999.99, 49.99, 129.99, 299.99] — total, cheapest, most expensive, average (2 dp),
#      and how many are above 100 (loop + counter)
#  11. New list of prices with 10% off each (loop + append — comprehensions come later)
#
# Part B — nested lists
#   students = [["Ali", [88, 92, 79]], ["Sara", [95, 100, 98]], ["Hamza", [60, 72, 58]], ["Zara", [70, 65, 80]]]
#  12. Print each student's name and average (2 dp). Find the student with the highest average.
#  13. Build a list of names whose average is >= 70.
#   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#  14. Print as a grid. Print the diagonal. Sum of each row, then each column.
#  15. Transpose with nested loops -> [[1,4,7],[2,5,8],[3,6,9]].  Flatten -> [1..9].
#  16. Remove duplicates from [3, 1, 3, 2, 1, 5] KEEPING order (no set()).
#  17. Merge two sorted lists [1,3,5,7] and [2,4,6] into one sorted list WITHOUT sort()/sorted()
#      (two-pointer walk — classic interview question).
#
# Bonus: a = cart   vs   a = cart.copy()   vs   a = cart[:]   — modify `a`, print `cart` each time.
#        Comment: what is a "reference"?  Then: rotate a list right by k with slicing only,
#        [1,2,3,4,5], k=2 -> [4,5,1,2,3]; make it work when k > len (hint: %).


# --- your code below ---

