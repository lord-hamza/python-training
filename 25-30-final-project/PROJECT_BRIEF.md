# Final Project — Auto Transport Dispatch System (Days 25–30)

## The rules

- **Build it alone.** No Claude Code, no ChatGPT, no Copilot. Google, YouTube, the official
  Python docs, and your own topic folders are allowed — that's what a job looks like.
- Every feature goes on a **branch** and gets merged into `main`. Meaningful commit messages.
  At least one Pull Request to yourself on GitHub. Push every day.
- Nothing in this folder except this file exists yet. You design the structure.

## What you're building

A command-line app a dispatcher at an auto-transport company would actually use to manage
customers, their vehicles, shipments, drivers, and invoices. Data lives in SQLite and survives
restarts.

## Domain

| Entity | Fields |
|---|---|
| Customer | name, email (unique), phone |
| Vehicle | belongs to a customer; make, model, year, VIN (17 chars, no I/O/Q), type (`sedan` / `suv` / `pickup` / `motorcycle`), operable (bool) |
| Driver | name, license number, truck capacity (how many vehicles), status (`available` / `on_route`) |
| Shipment | customer, vehicle, origin (city, state), destination (city, state), miles, transport type (`open` / `enclosed`), price, status, pickup date, delivery ETA, driver (optional), created_at |
| Invoice | built from a delivered shipment; line items, total, `paid` / `unpaid`, issued date |

### Business rules

- **Status lifecycle:** `quoted → booked → dispatched → picked_up → in_transit → delivered`.
  `cancelled` is allowed only from `quoted` or `booked`. Any other transition must raise a
  custom exception — never silently do nothing.
- **Pricing** (base per mile by vehicle type): sedan 0.60, suv 0.75, pickup 0.95,
  motorcycle 0.45 + $100 crate fee. Inoperable +$150 flat. Enclosed +40%. Minimum charge $250.
  Over 2000 miles: 10% off the total. Use `Decimal`, not `float`, for money.
- **ETA:** pickup date + 1 business day per 500 miles (round up). Weekends don't count.
- **Dispatching:** a driver must be `available` and under capacity. Assigning a driver moves the
  shipment to `dispatched` and the driver to `on_route`. Delivery frees the driver.
- **Invoices** can only be generated for `delivered` shipments, once per shipment.

## Must-have features

1. **Customers** — add, list, search by name/email, update
2. **Vehicles** — add to a customer (VIN validated), list per customer
3. **Shipments** — create quote (auto price + ETA), book, dispatch (assign driver), advance status,
   cancel, list with filters (status / customer / origin state), view details with history
4. **Drivers** — add, list, show current load
5. **Invoices** — generate for a delivered shipment, mark paid, export as a `.txt` file
6. **Reports** — revenue by state, revenue by month, top 5 customers, shipments per status,
   driver utilisation
7. **Persistence** — SQLite via the repository pattern (Day 24 Q2). No SQL outside the repositories.
8. **Import / export** — import shipments from CSV; export any report to CSV and JSON
9. **Error handling** — the app never crashes on bad input. Custom exception hierarchy
   (`DispatchError` → `InvalidTransitionError`, `DriverUnavailableError`, `CustomerNotFoundError`, …).
   Friendly messages at the UI layer only.
10. **Logging** — every state change and every error goes to `dispatch.log`
11. **Tests** — pytest, minimum 25 tests, in-memory DB. Must cover pricing, ETA, status
    transitions, driver assignment, every repository, the service layer, CSV import.
12. **README** — setup (venv, `requirements.txt`), how to run, how to test, a short architecture
    section explaining the layers and why.

## Nice-to-have (only after every must-have is done and tested)

- `argparse` CLI mode alongside the menu: `python -m dispatch shipments list --status delivered`
- Live distance between origin and destination via a free API (with a cached fallback)
- `rich` tables in the terminal
- Config via env vars / `.env` (database path, log level)
- Type hints everywhere and a clean `mypy` run; `ruff` for lint/format
- A `Makefile` or `tasks.py` with `test`, `lint`, `run`

## Technical checklist — everything from the 24 days must show up

- [ ] Package layout: `dispatch/` with `models.py`, `pricing.py`, `exceptions.py`, `db.py`,
      `repositories.py`, `services.py`, `reports.py`, `cli.py`, `__main__.py`; `tests/`;
      `requirements.txt`; `.gitignore`; `README.md`
- [ ] dataclasses for models; `__post_init__` validation; `__str__` / `__repr__` / `__eq__`
- [ ] Inheritance + polymorphism for vehicle types (each knows its own rate) — no `if type ==` chains
- [ ] An ABC for the repository interface; `@classmethod` constructors (`from_row`, `from_dict`)
- [ ] `@property` with validation for shipment status
- [ ] Generators for CSV import and paginated listing
- [ ] At least two decorators of your own (`@log_call`, `@require_status(...)`)
- [ ] A context manager for the database connection
- [ ] `collections`, `datetime`, `pathlib`, `logging`, `decimal`, `csv`, `json`, `sqlite3`
- [ ] Feature branches, a PR, a `v1.0.0` tag on the final commit

## Day-by-day milestones

| Day | Deliverable | Done when |
|---|---|---|
| 25 | Plan + skeleton. Write the README plan first (entities, features, package layout). Then `models.py`, `exceptions.py`, `pricing.py` with tests. | `pytest` green; pricing + ETA + VIN validation tested |
| 26 | Data layer: `db.py`, schema, repositories for every entity. | Repository tests green on `:memory:` |
| 27 | Services: `DispatchService` (quote, book, dispatch, transitions, driver assignment, ETA), `InvoiceService`. | Service tests green; illegal transitions raise |
| 28 | CLI: menu-driven interface covering every must-have. Logging. Input validation. Manually walk a shipment from quote to invoice. | You can do everything from the menu without touching code |
| 29 | Reports + CSV import + CSV/JSON export + invoice `.txt` export. Edge cases. More tests. | 25+ tests green; a CSV of 50 shipments imports cleanly |
| 30 | Polish: README, docstrings, type hints, remove duplication, full test run, `git tag v1.0.0`, push. Write a "what I'd do differently" section in the README. | Fresh clone → follow README → app runs → `pytest` passes |

## Definition of done

Someone who has never seen this repo can clone it, follow the README, run the app, run the
tests, and use it to quote, dispatch, deliver and invoice a shipment — without asking you anything.
