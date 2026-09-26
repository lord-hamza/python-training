# Day 12 | File Handling
# Q1 - Text Files: Notes & Logs
# ------------------------------------------------------------
# Use  with open(...) as f:  for EVERYTHING. Never leave a file open.
#
# 1. Write 5 lines to notes.txt ("w" mode), then append 2 more ("a" mode).
#    Run it twice — what happens to the file each time? (why "w" is dangerous)
# 2. Read it back three ways: f.read(), f.readlines(), and  for line in f:  — strip the "\n".
# 3. Count lines, words, and characters in the file.
# 4. longest_line(path) -> str
# 5. Search: print every line (with its line number) containing a word the user types.
# 6. log_event(message) appends  "2026-09-16 14:05:33 | message"  to app.log
#    (from datetime import datetime; datetime.now().strftime(...)). Call it 3 times.
# 7. Copy a file line by line into a new file with every line UPPERCASED.
# 8. Reading a file that doesn't exist -> catch FileNotFoundError and print a clean message.
# 9. Modes: "r", "w", "a", "x", "r+" — try "x" on an existing file. Explain each in a comment.
# 10. Encoding: always pass  encoding="utf-8". Write a line with "café ☕" and read it back.
# 11. Write a simple TODO app: add / list / mark done / remove — persists to todo.txt so the
#     todos survive restarting the program. (one todo per line, "[x]" / "[ ]" prefix)
#
# Bonus: pathlib —  from pathlib import Path;  p = Path("notes.txt")
#        p.read_text(), p.write_text(), p.exists(), p.stat().st_size, p.suffix, p.with_suffix(".bak")
# Decide consciously: should generated .txt/.log files be committed? Add them to .gitignore if not.


# --- your code below ---

