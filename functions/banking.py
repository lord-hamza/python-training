# Banking Program

def show_balance():
    print(f"Your balance is ${balance.2f}")

def deposit(amount):
    amount = int(input("Enter the amount to deposit: "))
    amount += balance

def withdraw(amount):
    amount = int(input("Enter the amount to withdraw: "))
    amount -= balance

balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choose = int(input("Enter your choice (1-4): "))

    if choose == 1:
        show_balance()
    elif choose == 2:
        deposit(amount)
    elif choose == 3:
        withdraw(amount)
    elif choose == 4:
        is_running = False
    else:
        print("Invalid choice! Choose the right option.")