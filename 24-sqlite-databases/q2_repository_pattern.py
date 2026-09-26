# Day 24 | SQLite Databases
# Q2 - Repository Pattern: OOP + SQLite
# ------------------------------------------------------------
# Goal: in your final project, SQL must never leak into business logic or the UI.
# This file is the blueprint for the project's data layer.
#
#  1. @dataclass Customer(id: int | None, name, email, phone)     id is None until saved
#     @dataclass Shipment(id: int | None, customer_id, origin, dest, miles, vehicle_type,
#                         price, status = "quoted", created_at = ...)
#  2. class Database(path):
#       opens the connection in __init__ (row_factory = sqlite3.Row, foreign_keys ON)
#       create_tables()  /  close()  /  execute(sql, params=()) -> cursor  /  __enter__ / __exit__
#       so  with Database("app.db") as db:  works and always closes.
#  3. class CustomerRepository(db):
#       add(customer) -> Customer    sets customer.id from cursor.lastrowid
#       get(id) -> Customer | None   all() -> list[Customer]    find_by_email(email)
#       update(customer)             delete(id) -> bool
#     Row -> dataclass conversion in ONE private method  _row_to_customer(row).
#  4. class ShipmentRepository(db):
#       add, get, all(status=None), update_status(id, status), for_customer(customer_id),
#       revenue_by_state() -> dict[str, float], count_by_status() -> dict
#  5. Both repositories implement an ABC  Repository  with abstract add/get/all/delete (Day 18).
#  6. Service layer — class DispatchService(customer_repo, shipment_repo):
#       create_quote(customer_email, origin, dest, miles, vehicle_type, ...) -> Shipment
#         looks up the customer (or raises CustomerNotFound), computes price (Day 07 rules), saves
#       dispatch(id) / deliver(id) / cancel(id) — validate transitions (Day 17), raise custom errors
#       The service knows NOTHING about SQL. The repos know NOTHING about pricing.
#  7. Tests (Day 22): use  Database(":memory:")  in a fixture — fast, isolated, no files.
#     Write at least 6 tests across the repositories and the service.
#  8. Migrations (simple): a  schema_version  table; migrate(db) applies numbered SQL scripts
#     in order and records which ran. Add a column via a migration without losing data.
#
# Bonus: read the first page of the SQLAlchemy docs. What problem does an ORM solve compared to
#        what you just wrote by hand? What does it cost you?


# --- your code below ---

