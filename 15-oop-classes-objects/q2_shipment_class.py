# Day 15 | OOP 1 - Classes & Objects
# Q2 - Model a Real Thing: Shipment
# ------------------------------------------------------------
# class Shipment:
#   attributes:  id, customer_name, origin, destination, miles, vehicle_type, price, status
#                status starts as "quoted"
#   __init__ computes price by calling  self.calculate_price()  — port your Day 07
#            calculate_quote() rules into that method (use self.miles, self.vehicle_type ...).
#   methods:
#     dispatch()    quoted     -> dispatched      (any other current status: raise ValueError)
#     pick_up()     dispatched -> picked_up
#     deliver()     picked_up  -> delivered
#     cancel()      allowed only from quoted or dispatched
#     summary()     returns "#101 TX -> FL 1300mi sedan $890.00 [delivered]"
#     is_active()   True unless delivered or cancelled
#
# Then:
#   - Create 4 Shipment objects in a list; walk some through the lifecycle; try an illegal
#     transition inside try/except; print all summaries.
#   - Module-level functions that take the list:
#       total_revenue(shipments)  -> delivered only
#       by_status(shipments)      -> {status: [shipments]}
#       find(shipments, id)       -> Shipment or None
#   - A class attribute  _next_id = 101  so ids are auto-assigned (101, 102, ...) in __init__
#     without being passed in.
#   - A  to_dict()  method, and use it to json.dump the whole list to shipments.json.
#
# Bonus: a  history  list attribute that records every status change with a timestamp.
#        Print it for one shipment at the end.


# --- your code below ---

