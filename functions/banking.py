# Banking Program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = int(input("Enter the amount to deposit: "))
    if amount < 0:
        print("Invalid amount! Please enter a positive number.")
    else:
        return amount

def withdraw(balance):
    amount = int(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds!")
        return 0
    elif amount < 0:
        print("Invalid amount! Please enter a positive number.")
        return 0
    else:
        return amount


def main():
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
            show_balance(balance)
        elif choose == 2:
            balance += deposit()
        elif choose == 3:
            balance -= withdraw(balance)
        elif choose == 4:
            is_running = False
        else:
            print("Invalid choice! Choose the right option.")

    print("Thank you!")

if __name__ == "__main__":
    main()