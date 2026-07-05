# ===========================================================
# QUESTION 1
# ===========================================================


full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
school = input("Enter your school: ")

print("\nName in uppercase:", full_name.upper())
print("Course in title case:", course.title())
print("Age after 5 years:", age + 5)
print("Total number of characters:", len(full_name))


# ==========================================================
# QUESTION 2
# ==========================================================


sentence = input("Enter a sentence: ")

print("First 5 characters:", sentence[:5])
print("Last 5 characters:", sentence[-5:])
print("Reverse:", sentence[::-1])
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Length:", len(sentence))


# ============================================================
# QUESTION 3
# ============================================================
 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponentiation = num1 ** num2

print("\nResults")
print("Addition =", addition)
print("Subtraction =", subtraction)
print("Multiplication =", multiplication)
print("Division =", division)
print("Floor Division =", floor_division)
print("Modulus =", modulus)
print("Exponentiation =", exponentiation)


# ======================================================
# QUESTION 4
# ======================================================

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nComparison Results")
print("num1 > num2 =", num1 > num2)
print("num1 < num2 =", num1 < num2)
print("mun1 >= num2 =", num1 >= num2)
print("num1 <= num2 =", num1 <= num2)
print("num1 == num2 =", num1 == num2)
print("num1 != num2 =", num1 != num2)


# ====================================================
# QUESTION 5 - EVEN OR ODD
# ====================================================

number = int(input("Enter an integer: "))

result = "The number is even." if number % 2 == 0 else "The number is odd"

print(result)


# ======================================================
# QUESTION 6 - VOTING ELIGIBILITY
# ======================================================

age = int(input("Enter your age: "))
if age < 18:
    print("Not eligible to vote.")
elif age >= 18 and age < 60:
    print("Eligible to vote")
else:
    print("Eligible to vote(Senior citizen).")


 # ======================================================
# QUESTION 7 - STUDENTS GRADE
# ======================================================

score = int(input("Enter your score: "))
if score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: C")
elif score >= 40:
    print("Grade: D")
else:
    print("Grade: F")


# ======================================================
# QUESTION 8 - LOGIN SYSTEM
# ======================================================

username = "admin"
password = "python123"

entered_username = input("Enter username: ")
entered_password = input("Enter password: ")

if entered_username == username and entered_password == password:
    print("Welcome Admin!")
else:
    print("Invalid Username or Password.")


# ======================================================
# QUESTION 9 - SHOPPING RECEIPT
# ======================================================

customer_name = input("Enter customer name: ")
item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

total = quantity * price

if total >= 1000:
    discount = total * 0.10
elif total >= 500:
    discount = total * 0.05
else:
    discount = 0

final_amount = total - discount

print("\n===============SHOPPING RECEIPT")
print("Customer Name:", customer_name)
print("Item Name:", item_name)
print("Quantity:", quantity)
print("Price per Item: GHS", total)
print("Discount: GHS", discount)
print("Final Amount: GHS", final_amount)


# ======================================================
# QUESTION 10 - LARGEST NUMBER
# ======================================================

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number"))

if num1 >= num2 and num1 >= num3:
    largest = num1

elif num2 >= num1 and num2 >= num3:
    largest = num2
else: largest = num3

if num1 <= num2 and num1 <= num3:
    smallest = num1

elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print("\nResults")
print("Largest number =", largest)
print("Smallest number =", smallest)


 # ======================================================
# QUESTION 11 - STRENGH OF PASSWORD
# ======================================================

password = input("Enter your password")
if len(password) >= 8:
    print("Strong Password")
elif len(password) >= 6:
    print("Medium Password")
else:
    print("Weak Password")


# ======================================================
# QUESTION 12 - MINI BANK WITHDRAWAL
# ======================================================

balance = 5000

withdrawal = float(input("Enter withdrawl amount: "))

if withdrawal <= balance:
    balance = balance - withdrawal
    print("Withdrawal successful.")
    print("Remaining Balance: GHS", balance)
else:
    print("Insufficient Funds.")


# ======================================================
# QUESTION 13 - MEMBERSHIP CHECKER
# ======================================================

languages = "python javascript java c++"

language = input("Enter a programming language: ")
if language in languages:
    print(language, "exists in the list.")
else:
    print(language, "does not exist in the list")


# ======================================================
# QUESTION 14 - IDENTITY OPERATOR
# ======================================================

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y =", x is y)
print("x is z=", x is z)
print("x == z =", x == z)

print("\nDifference:")
print("'is' checks whether two variables refer to the same object in memory.")
print("'=' checks whether two variables have the same value")