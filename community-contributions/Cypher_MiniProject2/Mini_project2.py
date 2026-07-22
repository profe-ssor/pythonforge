#!/usr/bin/python

# ATM Simulator

print("===================================")
print("      WELCOME TO CYPHER ATM")
print("===================================")

# Step 1: Insert Card
card = input("Please insert your ATM card (type 'insert'): ").lower()

if card != "insert":
    print("No card detected. Transaction cancelled.")
    exit()

print("\nCard inserted successfully.")

# Step 2: Enter PIN
correct_pin = "1234"
balance = 5000.00
attempts = 3

while attempts > 0:
    pin = input("Enter your 4-digit PIN: ")

    if pin == correct_pin:
        print("\nLogin Successful!")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. Attempts left: {attempts}")

if attempts == 0:
    print("Too many incorrect attempts.")
    print("Your card has been blocked.")
    exit()

# Step 3: ATM Menu
while True:
    print("\n========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        print(f"\nYour current balance is: ${balance:.2f}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: GHS "))

        if amount > 0:
            balance += amount
            print(f"Deposit successful!")
            print(f"New Balance: GHS {balance:.2f}")
        else:
            print("Invalid amount.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: GHS "))

        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Please collect your cash.")
            print(f"Remaining Balance: GHS {balance:.2f}")

    elif choice == "4":
        print("\nPlease take your card.")
        print("Thank you for using CYPHER ATM.")
        break

    else:
        print("Invalid option. Please try again.")