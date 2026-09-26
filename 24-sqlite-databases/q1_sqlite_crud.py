# Day 24 | SQLite Databases
# Q1 - SQLite CRUD  (sqlite3 is in the standard library — nothing to install)
# ------------------------------------------------------------
#  1. conn = sqlite3.connect("shipments.db")  (creates the file). Create tables with
#     CREATE TABLE IF NOT EXISTS:
#       customers(id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE, phone TEXT)
#       shipments(id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id),
#                 origin TEXT, dest TEXT, miles INTEGER, price REAL,
#                 status TEXT DEFAULT 'quoted', created_at TEXT)
#     Turn on  PRAGMA foreign_keys = ON.
#  2. INSERT 3 customers and 6 shipments. ALWAYS use  ?  placeholders — NEVER f-strings in SQL.
#     Google "Bobby Tables" and write one line about SQL injection. Use executemany for bulk.
#     conn.commit() — forget it once and reopen the DB to see what happened.
#  3. SELECTs:
#       all shipments  /  WHERE status = ?  /  ORDER BY price DESC LIMIT 3
#       COUNT(*) ... GROUP BY status  /  SUM(price) WHERE status = 'delivered'  /  AVG(miles)
#       shipments JOIN customers -> customer name + origin + dest
#       shipments per customer (JOIN + GROUP BY + COUNT)
#  4. UPDATE a shipment's status;  DELETE a cancelled one. Check  cursor.rowcount.
#  5. conn.row_factory = sqlite3.Row  -> access columns by name:  row["origin"]. Convert rows to
#     Day 18 dataclasses.
#  6. Transactions:  with conn:  auto-commits on success and rolls back on an exception.
#     Prove the rollback: inside one  with conn:  insert a valid customer THEN a duplicate email
#     -> sqlite3.IntegrityError -> reopen and confirm NEITHER was saved.
#  7. Wrap everything in functions that take the connection:
#       add_customer(conn, name, email, phone) -> id      add_shipment(conn, ...) -> id
#       list_shipments(conn, status=None)                 update_status(conn, id, status)
#       revenue_by_state(conn) -> dict                    delete_shipment(conn, id)
#     Demo under  if __name__ == "__main__":
#  8. Explore the file from the terminal:   sqlite3 shipments.db ".tables"   then  .schema
#     (or install "DB Browser for SQLite"). Add  *.db  to .gitignore.
#
# Bonus: CREATE INDEX idx_shipments_status ON shipments(status) — what's an index, when does it help,
#        when does it hurt?  EXPLAIN QUERY PLAN SELECT ...


# --- your code below ---

