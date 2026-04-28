import csv

def menu():
    print("\n--- Personal Budget Tracker ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. Exit")

def add_transaction(type):
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([type, amount, description])

    print("Transaction added!")

def view_balance():
    total_income = 0
    total_expense = 0

    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == "Income":
                    total_income += float(row[1])
                else:
                    total_expense += float(row[1])
    except FileNotFoundError:
        print("No data found!")

    balance = total_income - total_expense

    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance: {balance}")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_transaction("Income")
    elif choice == "2":
        add_transaction("Expense")
    elif choice == "3":
        view_balance()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")