# Day 21 | Standard Library
# Q2 - collections, pathlib, os, shutil, argparse, logging
# ------------------------------------------------------------
# collections
#  1. Counter: word frequency in one line;  .most_common(3);  Counter arithmetic (a + b, a - b);
#     Counter of vehicle types in your fake shipments.
#  2. defaultdict(list): group shipments by origin with NO "if key not in" check.
#     defaultdict(int) for counting.  defaultdict(lambda: defaultdict(int)) for a 2-level count.
#  3. namedtuple("Shipment", "id origin dest miles") — vs a dataclass: when is which enough?
#  4. deque: append/appendleft/popleft;  deque(maxlen=5) as a rolling "last 5 log lines" window.
#  5. ChainMap — config layering: cli_args over env_vars over defaults. Look one key up.
#
# pathlib / os / shutil
#  6. Path.cwd(), Path.home(), Path(__file__).parent, Path("data") / "shipments.csv"  (the / operator)
#     .name .stem .suffix .parent .exists() .is_file() .mkdir(parents=True, exist_ok=True)
#  7. Create  data/2026/09/  , write a file inside, list every *.csv recursively (rglob), then
#     delete the whole tree (shutil.rmtree). Handle "already exists" / "doesn't exist".
#  8. Walk THIS repo (Path(__file__).parent.parent) and print every .py file with its size in KB,
#     sorted by size. Count the total lines of Python you've written in 21 days.
#  9. os.environ.get(), os.getpid(), os.path.join vs pathlib — write the same path both ways.
#
# argparse
# 10. python q2_collections_pathlib_argparse.py quote --miles 1300 --vehicle suv --enclosed
#     python q2_collections_pathlib_argparse.py list --status delivered --limit 5
#     Subcommands (quote / list), typed args, defaults, a store_true flag, --help for free.
#
# logging
# 11. Replace print-debugging: logging.basicConfig(level=logging.INFO, format=..., filename="app.log")
#     logger = logging.getLogger(__name__);  logger.debug/info/warning/error/exception.
#     Log to file AND console (two handlers). Comment: why logging beats print in real apps.
#
# Bonus: tempfile.TemporaryDirectory() for scratch files in tests;  shutil.copy / move;
#        Path.rename;  json.dumps(default=str) for Paths and datetimes.


# --- your code below ---

