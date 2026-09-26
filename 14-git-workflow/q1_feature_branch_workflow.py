# Day 14 | Git Workflow
# Q1 - Feature Branch Workflow
# ------------------------------------------------------------
# Goal: stop coding directly on main. Do the git steps in the terminal; write the Python here.
#
# 1. Know where you are:   git status     git log --oneline -5     git branch
# 2. Create and switch to a branch:   git switch -c feature/temperature-converter
#    (older syntax you'll see everywhere:  git checkout -b ...)
# 3. In THIS file write:  celsius_to_f(c), f_to_celsius(f), and a small input() menu using them.
#    Make at least 2 SEPARATE commits with meaningful messages:
#       "add temperature conversion functions"   then   "add interactive menu"
#    NOT "update", "fix", "changes", "asdf".  Rule: a message completes the sentence
#    "If applied, this commit will ___".
# 4. git log --oneline --graph --all   — look at where the branch sits relative to main.
# 5. git switch main   -> your code is GONE from the file.   git switch feature/...  -> it's back.
#    (nothing was lost — the file just reflects the branch you're on)
# 6. Merge:   git switch main   then   git merge feature/temperature-converter
# 7. Delete the merged branch:   git branch -d feature/temperature-converter
# 8. Push:   git push origin main
# 9. Record EVERY command you ran, in order, as comments at the bottom of this file.
#
# 10. Do it again with a PR:
#       git switch -c feature/add-kelvin   -> add kelvin conversions -> commit
#       git push -u origin feature/add-kelvin
#       On GitHub: open a Pull Request, read the diff, merge it there.
#       Locally:  git switch main;  git pull;  git branch -d feature/add-kelvin
#     That's the exact workflow at every job.
#
# Bonus:  git log --oneline --graph --all   after the PR merge — find the merge commit.
#         git blame q1_feature_branch_workflow.py — who wrote each line, in which commit?


# --- your code below ---

