# Day 23 | APIs & JSON
# Q2 - POST / PUT / DELETE and an API Client Class
# ------------------------------------------------------------
# Still https://jsonplaceholder.typicode.com — it fakes writes (returns success, stores nothing).
#
#  1. POST /posts with  json={"title": "...", "body": "...", "userId": 1}  -> status 201, the
#     response JSON contains an id. What's the difference between  json=  and  data=  ?
#  2. PUT /posts/1 (full replace), PATCH /posts/1 (partial), DELETE /posts/1 -> check each status.
#     Comment: GET vs POST vs PUT vs PATCH vs DELETE, and what 200 / 201 / 204 / 400 / 401 / 403 /
#     404 / 429 / 500 mean. You WILL be asked this in interviews.
#  3. Headers: send  {"Accept": "application/json", "User-Agent": "python-training/1.0"}.
#     Send  Authorization: Bearer faketoken  to https://api.github.com/user -> read the 401 body.
#  4. class ApiClient(base_url, timeout=5):
#       uses one  requests.Session()  (why? connection reuse, shared headers)
#       get(path, **params) / post(path, payload) / put / patch / delete
#       each returns parsed JSON, or raises  ApiError(status_code, message)  (your exception)
#       __enter__/__exit__ close the session
#     client = ApiClient("https://jsonplaceholder.typicode.com");  client.get("/users/1")
#  5. class PostsRepository(client):  list(), get(id), create(title, body), update(id, **fields),
#     delete(id)  — returns  @dataclass Post  objects, NOT dicts. Repository HAS a client
#     (composition, Day 18). The rest of the program never sees requests or JSON.
#  6. Pagination: /posts?_page=1&_limit=10 — a GENERATOR  iter_posts()  that yields every post,
#     fetching page after page until a page comes back empty.
#  7. Test PostsRepository with a FAKE client (Day 22) — no network in tests.
#
# Bonus: a tiny CLI with argparse subcommands:
#        python q2_...py posts list  |  posts get 3  |  posts create "title" "body"  |  posts delete 3


# --- your code below ---

