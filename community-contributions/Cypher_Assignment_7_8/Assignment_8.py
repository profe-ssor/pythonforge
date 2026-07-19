#!/usr/bin/python

# Question 1: Student Information Manager
students = {}

for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    mark = float(input("Enter mark: "))
    students[name] = mark

print("\nStudent Records")
for name, mark in students.items():
    print(name, "-", mark)

marks = list(students.values())

print("\nHighest Mark:", max(marks))
print("Lowest Mark:", min(marks))
print("Average Mark:", sum(marks) / len(marks))

print("\nStudents scoring 50 or above:")
for name, mark in students.items():
    if mark >= 50:
        print(name)


# Question 2: Word Analyzer
sentence = input("Enter a sentence: ")

print("Total characters:", len(sentence))

words = sentence.split()
print("Total words:", len(words))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Reversed:", sentence[::-1])

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for ch in sentence:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

frequency = {}

for word in words:
    word = word.lower()
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequency")
for word, count in frequency.items():
    print(word, ":", count)


# Question 3: Sales Report
products = {
    "Rice": 20,
    "Sugar": 15,
    "Milk": 10,
    "Bread": 8,
    "Soap": 5
}

sales = {}
grand_total = 0

for product, price in products.items():
    qty = int(input(f"Enter quantity sold for {product}: "))
    total = price * qty
    sales[product] = total
    grand_total += total

print("\nSales Report")
print("Product\tPrice\tQty\tSales")

for product, price in products.items():
    qty = sales[product] // price
    print(product, "\t", price, "\t", qty, "\t", sales[product])

print("\nGrand Total:", grand_total)

highest = max(sales, key=sales.get)
lowest = min(sales, key=sales.get)

print("Highest Sales:", highest, "-", sales[highest])
print("Lowest Sales:", lowest, "-", sales[lowest])


# Question 4: Employee Salary Processor
employees = []

for i in range(5):
    name = input("Enter employee name: ")
    salary = float(input("Enter basic salary: "))

    tax = salary * 0.10
    bonus = salary * 0.05
    net = salary - tax + bonus

    employees.append([name, salary, tax, bonus, net])

print("\nSalary Report")
print("Name\tSalary\tTax\tBonus\tNet Salary")

for emp in employees:
    print(emp[0], "\t", emp[1], "\t", emp[2], "\t", emp[3], "\t", emp[4])


# Question 5: Inventory Management System
inventory = {}

while True:
    print("\nInventory Menu")
    print("1. Add Item")
    print("2. Update Quantity")
    print("3. Remove Item")
    print("4. Display Items")
    print("5. Search Item")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Item name: ")
        qty = int(input("Quantity: "))
        inventory[item] = qty

    elif choice == "2":
        item = input("Enter item: ")
        if item in inventory:
            qty = int(input("New quantity: "))
            inventory[item] = qty
        else:
            print("Item not found.")

    elif choice == "3":
        item = input("Item to remove: ")
        if item in inventory:
            del inventory[item]
        else:
            print("Item not found.")

    elif choice == "4":
        print("\nInventory")
        for item, qty in inventory.items():
            print(item, ":", qty)

    elif choice == "5":
        item = input("Search item: ")
        if item in inventory:
            print(item, "Quantity:", inventory[item])
        else:
            print("Item not found.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")


# Question 6: Student Grade Report
students = {}

grades = {"A":0, "B":0, "C":0, "D":0, "F":0}

for i in range(10):
    name = input("Student name: ")
    mark = float(input("Mark: "))
    students[name] = mark

print("\nGrade Report")

for name, mark in students.items():

    if mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "F"

    grades[grade] += 1

    print(name, "-", mark, "-", grade)

marks = list(students.values())

print("\nGrade Counts")
for grade, count in grades.items():
    print(grade, ":", count)

print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks)/len(marks))


# Question 7: Dictionary and Set Challenge
countries = {
    "Ghana":"Accra",
    "Nigeria":"Abuja",
    "Kenya":"Nairobi",
    "France":"Paris",
    "Germany":"Berlin",
    "Brazil":"Brasilia",
    "Japan":"Tokyo",
    "Canada":"Ottawa"
}

continents = {
    "Africa",
    "Europe",
    "South America",
    "Asia",
    "North America"
}

print("Countries")
for country in countries.keys():
    print(country)

print("\nCapitals")
for capital in countries.values():
    print(capital)

print("\nCountries and Capitals")
for country, capital in countries.items():
    print(country, "-", capital)

print("\nContinents")
for continent in continents:
    print(continent)

print("Number of unique continents:", len(continents))

search = input("\nEnter country to search: ")

if search in countries:
    print("Capital:", countries[search])
else:
    print("Country not found.")


# Question 8: Mini Banking System
balance = 2000
history = []

total_deposit = 0
total_withdraw = 0

while True:

    print("\nBank Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Transaction History")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        print("Balance: GHS", balance)

    elif choice == "2":
        amount = float(input("Deposit amount: "))
        balance += amount
        total_deposit += amount
        history.append("Deposited GHS " + str(amount))

    elif choice == "3":
        amount = float(input("Withdraw amount: "))

        if amount <= balance:
            balance -= amount
            total_withdraw += amount
            history.append("Withdrew GHS " + str(amount))
        else:
            print("Insufficient funds.")

    elif choice == "4":
        print("\nTransaction History")
        if len(history) == 0:
            print("No transactions.")
        else:
            for transaction in history:
                print(transaction)

    elif choice == "5":
        break

    else:
        print("Invalid choice.")

print("\nFinal Report")
print("Final Balance: GHS", balance)
print("Total Deposited: GHS", total_deposit)
print("Total Withdrawn: GHS", total_withdraw)
print("Transactions:", len(history))