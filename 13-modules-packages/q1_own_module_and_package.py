# Day 13 | Modules & Packages
# Q1 - Make Your Own Module & Package
# ------------------------------------------------------------
# In THIS folder create two new files:
#   mathutils.py   ->  add, subtract, is_prime, factorial, and a constant PI = 3.14159
#   strutils.py    ->  slugify(text), is_palindrome(text), word_count(text)
#   (pull the code from Day 07 — you're building a reusable library)
#
# Then, in this file, show all four import styles and use one function from each:
#   1. import mathutils                    ->  mathutils.add(2, 3)
#   2. from strutils import slugify, word_count
#   3. import mathutils as mu              ->  mu.PI
#   4. from mathutils import *             ->  write in a comment why this is discouraged
#
# 5. Add  if __name__ == "__main__":  to mathutils.py with a few test prints.
#    Run  python mathutils.py  and then import it from here — the prints only happen once.
#    Explain in a comment what __name__ equals in each case.
# 6. Make a PACKAGE: create a folder  helpers/  with an (empty) __init__.py, move both modules
#    inside. Now import as:
#       from helpers.mathutils import is_prime
#       from helpers import strutils
#    Then put  from .mathutils import add  in __init__.py so  from helpers import add  works.
# 7. Print mathutils.__file__ and dir(mathutils). What is  __pycache__ ? Add it to .gitignore.
# 8. Circular import: make strutils import mathutils and mathutils import strutils. Run it.
#    Read the error, then undo it. Comment: how do you avoid circular imports?
# 9. sys.path — print it. That's where Python looks for modules. Why does importing from a
#    sibling folder (e.g. 07-functions/) NOT work directly? (not on sys.path; hyphenated names can't be imported anyway)
#
# Bonus: python -m helpers.mathutils  — what does -m do differently from  python helpers/mathutils.py ?


# --- your code below ---

