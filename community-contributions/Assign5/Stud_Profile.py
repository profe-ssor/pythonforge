# Q1 variables
full_Name = str(input("Enter student name"))
Age = int(input("Enter student age"))
Course = str(input("Enter student course"))
School = str(input("Enter your school"))

#Display of variables
print(f"Print student name in uppercase: {full_Name.upper()}\ncourse: {Course}\nage: {Age+5}\nname: {len(full_Name)}")

# Q2 Ask the user to enter a sentence.
Sentence = str(input("Enter a sentence: "))
print(f"First 5 characters: {Sentence[:5]}")
print(f"Last 5 characters: {Sentence[-5:]}")
print(f"Reverse of the sentence: {Sentence[::-1]}")
print(f"Sentence in uppercase: {Sentence.upper()}")
print(f"Sentence in lowercase: {Sentence.lower()}")
print(f"Length of the sentence: {len(Sentence)}")

 #Q3 Arithmetic Calculator
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the secound number"))


Add = num1 + num2
Sub = num1 - num2
Mult = num1 * num2
Div = num1 / num2
Floor_Div = num1 // num2
Mod = num1 % num2
Expo = num1 ** num2
print(f"Addition: {Add}\nSubtraction: {Sub}\nMultiplication: {Mult}\nDivision: {Div}\nFloor Division: {Floor_Div}\nModulus: {Mod}\nExponentiation: {Expo}")




#Question 4 Comparison Operators - Ask the user for two numbers.


num_1 = int(input("Please enter number one"))
num_2 = int(input("Please enter number two"))
print(f"Is number one greater than number two? {num_1 > num_2}")
print(f"Is number one less than number two? {num_1 < num_2}")
print(f"Is number one equal to number two? {num_1 == num_2}")
print(f"Is number one not equal to number two? {num_1 != num_2}")
print(f"Is number one greater than or equal to number two? {num_1 >= num_2}")
print(f"Is number one less than or equal to number two? {num_1 <= num_2}")



#Question 5 even or odd - Ask the user to enter an integer

num = int(input("Please enter an integer"))
#Use a ternary operator to display whether the number is even or odd.
result = "is even" if num % 2 == 0 else "is odd"
print(f"{num} {result}")

#Question 6 (5 Marks) – Voting Eligibility

#Ask the user to enter their age.
age = int(input("Please enter your age"))
#Use a conditional statement to determine if the user is eligible to vote.
if age < 18:
    print("You are not eligible to vote.")
elif age < 60:
    print("You are eligible to vote.")
else:
    print("You are eligible to vote (Senior Citizen).")

#Question 7 (5 Marks) – Student Grade

#Ask the user to enter a score.
score = float(input("Please enter your score"))
#Use conditional statements to determine the grade.
if score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F")


 #Question 8 (10 Marks) – Login System

username = str(input("Enter username: "))
password = str(input("Enter password: "))
if username == "admin" and password == "python123":
    print("Welcome admin!")
else:
    print("Invalid username or password.")

#Question 9 (10 Marks) – Shopping Receipt
Cust_Name = str(input("Enter customers name"))
Item_Name = str(input("Enter item name"))
Quantity = int(input("Enter quantity"))
Price = float(input("Enter price per item"))
Total_Cost = Quantity * Price
if  Total_Cost >= 1000:
    Discount = Total_Cost * 0.10
elif Total_Cost >= 500:
    Discount = Total_Cost * 0.05
else:
    Discount = 0
    print(f"The amount for total cost: {Total_Cost}\nDiscount: {Discount}\nFinal Amount: {Total_Cost - Discount}")

#Question 10 (10 Marks) – Largest Number
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))

# Display:Use only if, elif, and else.
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

smallest = num1
if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")

# Question 11 (10 Marks) – Password Strength Checker

# Ask the user for a password.
password = input("Enter a password: ")

# Display the strength of the password.
if len(password) >= 8:
    print("Strong Password")
elif len(password) >= 6:
    print("Medium Password")
else:
    print("Weak Password")

# Question 12 (10 Marks) – Mini Bank Withdrawal

# Create:

balance = 5000

# Ask the user to enter the withdrawal amount.
withdrawal = float(input("Enter the withdrawal amount: "))

# If:
if withdrawal <= balance:
    # Deduct and display the remaining balance.
    balance -= withdrawal
    print(f"Withdrawal successful. Remaining balance: {balance}")
else:
    # Display "Insufficient Funds."
    print("Insufficient Funds.")

#Question 13 (5 Marks) – Membership Checker

languages = "python javascript java c++"

language = input("Enter a programming language: ").lower()

if language in languages:
    print(f"{language} exists in the list.")
else:
 
    print(f"{language} does not exist in the list.")

# Question 14 (5 Marks) – Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y:", x is y)
print("x is z:", x is z)
print("x == z:", x == z)

#Question 15 (10 Marks) – Student Registration System
Full_Name = input("Enter your full name: ")
Age = int(input("Enter your age: "))
Gender = input("Enter your gender (M/F): ")
Program = input("Enter your program of study: ")
Student_ID = input("Enter your student ID: ")
Score = float(input("Enter your score: "))

print("\nStudent Registration Details:")
print(f" Name: {Full_Name.upper()}")
print(f"First 4 letters of the name: {Full_Name[:4]}")
print(f"Last 4 letters of the name: {Full_Name[-4:]}")
print(f"Name length: {len(Full_Name)}")
print(f"Age: {Age}")

print("\nStudent status:")
if 80 <= Score <= 100:
    print("Score: Excellent")
elif 70 <= Score < 80:
    print("Score: Very Good")
elif 60 <= Score < 70:
    print("Score: Good")
elif 50 <= Score < 60:
    print("Score: Pass")
else:
    print("Score: Fail")

# Finally display a neatly formatted student report:
print("\n--- Student Report ---")
print(f"Name: {Full_Name.upper()}")
print(f"Age: {Age}")
print(f"Gender: {Gender}")
print(f"Program: {Program}")
print(f"Student ID: {Student_ID}")
print(f"Score: {Score}")