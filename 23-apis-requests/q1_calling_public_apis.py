# Day 23 | APIs & JSON
# Q1 - Calling Public APIs with requests
# ------------------------------------------------------------
# pip install requests  (you did on Day 13). Free, no-key APIs:
#   https://jsonplaceholder.typicode.com      https://api.github.com      https://api.zippopotam.us/us/75201
#
#  1. r = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
#     print r.status_code, r.headers["Content-Type"], r.json()[0]. Print each user's name, email,
#     and city (nested: user["address"]["city"]).
#  2. Query params:  requests.get(".../posts", params={"userId": 1})  — print the titles.
#     GET  /posts/9999  -> 404. Check status_code and handle it — don't call .json() on it blindly.
#  3. Errors, properly:
#       r.raise_for_status()  inside  try/except requests.HTTPError
#       except requests.Timeout  /  requests.ConnectionError  (use a bogus host to trigger it)
#       except requests.RequestException as the catch-all base
#  4. GET https://api.github.com/users/<your-github-username>/repos -> print name, stars,
#     language of each repo. Count languages with Counter. Print the X-RateLimit-Remaining header.
#  5. Zip lookup: https://api.zippopotam.us/us/<zip> -> city + state. Wrap in  lookup_zip(zip) ->
#     tuple | None. Use it to validate origin/destination zips for a shipment.
#  6. Wrap it all:  get_json(url, params=None, retries=3, timeout=5) -> dict | list | None
#     Handles every error above, retries on timeout/connection errors with backoff
#     (time.sleep(2 ** attempt)), logs what happened (Day 21 logging). Reuse your Day 20 @retry if you like.
#  7. Simple cache: save the users response to users.json. Next run, if the file exists and is
#     less than 1 hour old (Path.stat().st_mtime vs time.time()), load it instead of calling the API.
#
# Bonus: pretty-print any response with json.dumps(data, indent=2).
#        Pick an API that needs a key (OpenWeather, NewsAPI...). Put the key in a  .env  file,
#        load it with os.environ / python-dotenv. NEVER hardcode a key. NEVER commit .env.


# --- your code below ---

