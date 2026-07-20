#!/usr/bin/python

# Question 6: PIN Verification System
correct_pin = "4321"
attempts = 3

while attempts > 0:
    pin = input("Enter your 4-digit PIN: ")

    if pin == correct_pin:
        print("Access Granted.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect PIN.")
            print("Attempts remaining:", attempts)
        else:
            print("Account Locked.")


# Question 7: Find the largest number
largest = None

while True:
    number = int(input("Enter a number (-1 to stop): "))

    if number == -1:
        break

    if largest is None or number > largest:
        largest = number

if largest is None:
    print("No numbers were entered.")
else:
    print("Largest number:", largest)


# Question 8: Count positive, negative and zero numbers
positive = 0
negative = 0
zero = 0

while True:
    number = int(input("Enter an integer (999 to stop): "))

    if number == 999:
        break

    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)



# Question 9: Student mark analyzer
count = 0
total = 0
highest = None
lowest = None

while True:
    mark = int(input("Enter student mark (0-100, -1 to stop): "))
    if mark == -1:
        break
    if mark < 0 or mark > 100:
        print("Invalid mark. Enter a value between 0 and 100.")
        continue
    count += 1
    total += mark
    if highest is None or mark > highest:
        highest = mark
    if lowest is None or mark < lowest:
        lowest = mark
if count == 0:
    print("No marks were entered.")
else:
    average = total / count

    print("Total marks entered:", count)
    print("Average mark:", average)
    print("Highest mark:", highest)
    print("Lowest mark:", lowest)

