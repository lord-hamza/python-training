# Day 14 | Git Workflow
# Q2 - Merge Conflicts, .gitignore, Undoing Things
# ------------------------------------------------------------
# Part A — cause a merge conflict ON PURPOSE and fix it
#   1. On main, put   GREETING = "hello"   in this file and commit.
#   2. git switch -c feature/greeting-a   -> change to   GREETING = "hi there"   -> commit
#   3. git switch main   ->   git switch -c feature/greeting-b   -> change to   GREETING = "hey"   -> commit
#   4. git switch main   ->   git merge feature/greeting-a   (clean, fast-forward)
#                        ->   git merge feature/greeting-b   (CONFLICT!)
#   5. git status. Open this file: find the  <<<<<<<  =======  >>>>>>>  markers. Pick one version
#      (or combine), delete the markers,   git add   this file,   git commit.
#   6. git log --oneline --graph --all   — see the diamond.
#
# Part B — .gitignore
#   7. Create /.gitignore at the repo root (if you haven't already) containing at least:
#         __pycache__/     .venv/     *.log     .DS_Store     *.db     .env
#      Create a fake  secret.log  -> git status must NOT show it.
#   8. A file that's ALREADY tracked won't be ignored by adding it to .gitignore. Learn:
#         git rm --cached <file>      then commit. Try it with a throwaway file.
#
# Part C — undoing things (do each on a throwaway change)
#   9.  Change this file, DON'T stage — throw the change away:      git restore <file>
#   10. Stage a change, then unstage it:                            git restore --staged <file>
#   11. Make a bad commit, then undo it SAFELY (new commit):         git revert HEAD
#   12. Inspect:  git diff     git diff --staged     git show HEAD     git log -p -1
#   13. Fix a typo in your LAST commit message:  git commit --amend   — only if not pushed. Why?
#   14. git stash  /  git stash pop  — you're mid-change and need to switch branches. Try it.
#   15. git reset --soft HEAD~1   vs   git reset --hard HEAD~1   — try both on a scratch branch.
#       Comment: which one loses work? When is --hard OK?
#
# Python part: write  greet(name) -> f"{GREETING}, {name}!"  and call it.
# Record ALL commands as comments at the bottom.
#
# Bonus: git tag v0.1.0 && git push --tags. git checkout <old-commit-hash> -> "detached HEAD" —
#        what does that mean? How do you get back? (git switch main)


# --- your code below ---

