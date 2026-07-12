# Q1 Variables
full_Name = str(input("Enter your full name."))
age = int(input("Please enter your age."))
school = str(input("Please enter your school."))
fav_Subject = str(input("Please enter your favorite subject."))


#2. Displays the information in a neat format.
print(f"Name: {full_Name}\nAge: {age}\nSchool: {school}\nFavorite Subject: {fav_Subject}")


# 3 Converts the student's name to uppercase.

print(f"Converts the student's name to uppercase: {full_Name.upper()}")


# 4 Displays the first 3 characters of the student's name.
print(f"Displays the first 3 characters of the student's name: {full_Name[:3]}")

# 5  Displays the last 3 characters of the student's name.
print(f"Displays the last 3 characters of the student's name: {full_Name[-3:]}")


# 6  Calculates the student's age after 5 years.
print(f"Calculates the student's age after 5 years: {age + 5}")

# 7 Displays the total number of characters in the student's full name.

print(f"Displays the total number of characters in the student's full name: {len(full_Name)}")