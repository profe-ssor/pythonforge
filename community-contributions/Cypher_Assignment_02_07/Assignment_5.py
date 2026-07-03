#!/usr/bin/python

# Question 1 (5 Marks) – Student Profile
full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
school = input("Enter your school: ")

print("Name in uppercase:", full_name.upper())
print("Course in title case:", course.title())
print("Age after adding 5 years:", age + 5)
print("Total number of characters in the name:", len(full_name))



# Question 2
sentence = input("Enter a sentence: ")
print("First 5 characters:", sentence[:5])
print("Last 5 characters:", sentence[-5:])
print("Reverse of the sentence:", sentence[::-1])
print("Sentence in uppercase:", sentence.upper())
print("Sentence in lowercase:", sentence.lower())
print("Length of the sentence:", len(sentence))



#   Question 3 Arithmetic Calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponentiation:", num1 ** num2)



# Question 4 Comparison Operators
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("num1 > num2:", num1 > num2)
print("num1 < num2:", num1 < num2)
print("num1 >= num2:", num1 >= num2)
print("num1 <= num2:", num1 <= num2)
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)



# Question 5 Even or Odd
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number {number} is {result}.")



# Question 6 Voting Eligibility
age = int(input("Enter your age: "))
if age <= 18:
    print("Not eligible to vote.")
elif 18 <= age <= 59:
    print("Eligible to vote.")
else:
    print("Eligible to vote (Senior citizen).")



# Question 7 Grade Calculation
score = float(input("Enter your score: "))
if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score <= 79:
    print("Grade: B")
elif 60 <= score <= 69:
    print("Grade: C")
elif 50 <= score <= 59:
    print("Grade: D")
else:
    print("Grade: F")



#   Question 8  Login System
username = "admin"
password = "Python123"

input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

if input_username == username and input_password == password:
    print("Welcome Admin!")
else:
    print("Invalid username or password.")



#   Question 9 Shopping Receipt
customer_name = input("Enter customer name: ")
item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
total_cost = quantity * price
if total_cost >= 1000:
    discount = total_cost * 0.10
elif total_cost >= 500:
    discount = total_cost * 0.05
else:
    discount = 0
final_amount = total_cost - discount



# Question 10 Largest Number 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")



#   Question 11 Password Strength Checker
password = input("Enter your password: ")
length = len(password)
if length >= 8:
    print("Strong password")
elif 6 <= length < 7:
    print("Medium password")
else:
    print("Weak password")



# Question 12 Mini bank
balance = 5000
withdrawal = float(input("Enter the amount to withdraw: "))
if withdrawal <= balance:
    balance -= withdrawal
    print(f"Withdrawal successful. Remaining balance: {balance}")
else:
    print("Insufficient funds.")



# Question 13 Membership Checker
languages = ["Python", "Java", "C++", "JavaScript"]
language = input("Enter a programming language: ")
if language in languages:
    print("You are a member.")
else:
    print("You are not a member.")


# Question 14 Identity operator
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)
print("x is z:", x is z)
print("x == z:", x == z)


# Question 15 Student Registration System
full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
programme = input("Enter your programme: ")
level = input("Enter your level: ")
student_id = input("Enter your student ID: ")
score = float(input("Enter your score: "))

name_upper = full_name.upper()
first_4 = full_name[:4]
last_4 = full_name[-4:]
name_length = len(full_name)

if 80 <= score <= 100:
    status = "Excellent"
elif 70 <= score <= 79:
    status = "Very Good"
elif 60 <= score <= 69:
    status = "Good"
elif 50 <= score <= 59:
    status = "Pass"
else:
    status = "Fail"

print("\nStudent Registration Details:")
print("Name in uppercase: ", name_upper)
print("First 4 letters of the name: ", first_4)
print("Last 4 letters of the name: ", last_4)
print("Name length: ", name_length)

print("\n -----Academic Status-----")
print("score: ", score)
print("Status: ", status)

