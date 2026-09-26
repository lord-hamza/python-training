# Day 24 | SQLite Databases
# Q3 - LeetCode 595: Big Countries (Easy, SQL)
# https://leetcode.com/problems/big-countries/
# ------------------------------------------------------------
# Table World(name, continent, area, population, gdp).
# A country is BIG if area >= 3,000,000 OR population >= 25,000,000.
# Return name, population, area of the big countries, in any order.
#
# Example rows:
#   Afghanistan  Asia    652230   25500100  20343000000
#   Albania      Europe  28748    2831741   12960000000
#   Algeria      Africa  2381741  37100000  188681000000
#   Andorra      Europe  468      78115     3712000000
#   Angola       Africa  1246700  20609294  100990000000
#   -> Afghanistan, Algeria
#
# Do it in Python: create the table in an IN-MEMORY sqlite3 DB (":memory:"), insert the rows with
# executemany, run your SQL, print the result rows. Then submit just the SQL on LeetCode.
#
# More SQL practice (all Easy on LeetCode, do them the same way):
#   1757 Recyclable and Low Fat Products      1148 Article Views I
#   183  Customers Who Never Order (JOIN)     1068 Product Sales Analysis I (JOIN)
#   596  Classes More Than 5 Students (GROUP BY / HAVING)

import sqlite3

QUERY = """
-- your SQL here
"""

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    # create table + insert the example rows, then:
    # for row in conn.execute(QUERY): print(row)
    conn.close()
