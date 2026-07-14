#!/usr/bin/python

# Question 1: Student Login System
username = input("Enter your username: ")
password = input("Enter your password: ")
while username != "Cypher" or password != "Python123":
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username != "Cypher" or password != "Python123":
        print("Invalid username or password. Try again.\n")
print("Welcome, Cypher!")


# Question 2: Multiplication Table Generator
number = int(input("Enter a positive integer: "))
count = 1
while count <= 12:
    product = number * count
    print(f"{number} x {count} = {product}")
    count += 1


# Question 3: Sum of user-entered numbers
total = 0
count = 0
number = int(input("Enter a number (0 to stop): "))
while number != 0:
    total += number
    count += 1
    number = int(input("Enter another number (0 to stop): "))
print("Total sum:", total)
print("Number of values entered:", count)


# Question 4: Number Guessing Game
secret = 25
attempts = 0
guess = 0
while guess != secret:
    guess = int(input("Guess the secret number: "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print("Congratulations! you guessed correctly.")
print("Total attempts:", attempts)


# Question 5: ATM Menu Simulation
balance = 1000
choice = 0
while choice != 4:
    print("\n==== ATM Menu ====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Current balance: GHS", balance)
    elif choice == 2:
        deposit = float(input("Enter amount to deposit: GHS "))
        balance += deposit
        print("Deposit successful. Updated balance: GHS", balance)
    elif choice == 3:
        withdraw = float(input("Enter amount to withdraw: GHS "))
        if withdraw <= balance:
            balance -= withdraw
            print("Withdrawal successful. New balance: GHS", balance)
        else:
            print("Insufficient funds.")
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
    else:
        print("Invalid choice. Please try again.")