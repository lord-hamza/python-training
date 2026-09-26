# Day 13 | Modules & Packages
# Q2 - pip, venv, requirements.txt, stdlib tour
# ------------------------------------------------------------
# Do steps 1-5 in the TERMINAL, then record the exact commands you ran as comments here.
#
# 1. Create a virtual environment at the REPO ROOT:   python3 -m venv .venv
#    Activate it:  source .venv/bin/activate    (Windows: .venv\Scripts\activate)
#    Verify:       which python   -> must point inside .venv.   python --version
# 2. python -m pip install requests      then    pip list      and    pip show requests
# 3. pip freeze > requirements.txt   — open it and read it. That file is how teammates/servers
#    install exactly what you have.
# 4. deactivate, delete .venv, recreate it, and reinstall everything with:
#       python -m pip install -r requirements.txt
# 5. Add  .venv/  to .gitignore. NEVER commit a venv. ALWAYS commit requirements.txt.
#
# In THIS file:
# 6. import requests; print(requests.__version__)   — proves the venv works
# 7. Stdlib tour — one or two lines each:
#      sys       sys.argv, sys.version, sys.exit(code)
#      os        os.getcwd(), os.listdir("."), os.environ.get("HOME"), os.environ.get("NOPE", "default")
#      platform  platform.system(), platform.python_version()
#      time      time.time(), time.sleep(0.5), time.perf_counter()
#      random    random.choice, random.randint
#      math      math.sqrt, math.ceil, math.pi
#      string    string.ascii_letters, string.digits
# 8. Print this script's own command-line arguments:  python q2_pip_venv_stdlib.py a b c
#    Then use them: python q2_pip_venv_stdlib.py 1300 suv  -> print a quote using Day 07's function
#    (copy it in, or import it from helpers — see Q1).
# 9. Look up a package on https://pypi.org  that does something you'd use (rich, tabulate,
#    python-dotenv, httpx...). Install it, use it in 3 lines, add it to requirements.txt.
#
# Bonus: `pip install x` vs `python -m pip install x` — why is the second one safer?
#        What's pyproject.toml? (just read about it — you'll meet it in every modern repo)


# --- your code below ---

