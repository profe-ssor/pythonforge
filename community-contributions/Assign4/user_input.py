#Step1 Get input from the user
full_name = str(input("Enter your full name: "))
age = int(input("Enter your age: "))
fav_programming_language = str(input("Enter your favorite programming language: "))


#Step2 Display the input back to the user
print(f"Name: {full_name}")
print(f"Age: {age}")
print(f"Your favorite programming language is {fav_programming_language}")

#Total number of characters
print(f"Total number of characters in your name: {len(full_name)}")
print(f"Total number of characters in your favorite programming language: {len(fav_programming_language)}")

print(f"First 3 characters of your name: {full_name[:3]}")
print(f"First 3 characters of your favorite programming language: {fav_programming_language[:3]}")

print(f"Last 3 characters of your name: {full_name[-3:]}")

print(f"Name in uppercase: {full_name.upper()}")
print(f"Name in lowercase: {full_name.lower()}")
print(f"Name in title case: {full_name.title()}\n")


#Ask the user to enter:First Number, Second Number
num1 = int(input("Enter the first Number"))
num2 = int(input("Enter the second Number"))


Sum = num1 + num2
Diff = num1 - num2
Product = num1 * num2
Quotient = num1 / num2
Mod = num1 % num2
Exponent = num1 ** num2

#Display of inputs
print(f"The sum is: {Sum}")
print(f" The different is: {Diff}")
print(f"The product is: {Product}")
print(f"The quotient is: {Quotient}")
print(f"The modulo is: {Mod}")
print(f"The exponent is: {Exponent}\n")


#Ask the user to enter their age.
Age = int(input("Please enter your age"))
if Age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.\n")


#Ask the user to enter a password.
password = input("Please enter a password: ")
if password == "Python123":
    print("Access granted.")
else:
    print("Access denied.\n")


#Ask the user to enter a word.
word = input("Please enter a word: ")
print(f"Enter the first character of the word: {word[0]}")
print(f"Enter the last character of the word: {word[-1]}")
print(f"Reverse the word: {word[::-1]}")
print(f"Word in uppercase: {word.upper()}")
print(f"Word in lowercase: {word.lower()}\n")


#Create a simple student information program.
full_name = input("Enter your full name: ")
Age = int(input("Enter your age: "))
Course = input("Enter your course: ")
Score = float(input("Enter your score: "))

print(f"Student Information:")
print(f"Name: {full_name}")
print(f"Age: {Age}")
print(f"Course: {Course}")
if Score >= 50: 
    print("Status:  PASS")   
else:
    print("Status: FAIL\n")




 #Create a program that asks the user to enter three words.
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word3 = input("Enter the third word: ")

print(f"word1: {word1.upper()}")
print(f"word2: {word2.upper()}")
print(f"word3: {word3.upper()}\n")

print(f"word1: {word1.lower()}")
print(f"word2: {word2.lower()}")        
print(f"word3: {word3.lower()}\n")

print(f"word1: {len(word1   )}")
print(f"word2: {len(word2   )}")
print(f"word3: {len(word3   )}\n")

print(f"Enter the first character of word1: {word1[0]}")
print(f"Enter the first character of word2: {word2[0]}")
print(f"Enter the first character of word3: {word3[0]}\n")

print(f"Enter the last character of word1: {word1[-1]}")
print(f"Enter the last character of word2: {word2[-1]}")
print(f"Enter the last character of word3: {word3[-1]}\n")

#Then ask the user to enter a number.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")