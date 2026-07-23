# tuple of five countries
countriesT = ('Ghana', 'Togo', 'US', 'Itali', 'Germany')
print(countriesT[3])

#  tuple of numbers 
num = ( 34, 60, 70, 100, 80)
print(num[-1])


# Slice a tuple to display the first three items
fruits = ('Banana', 'Apple', 'Mango','Pineple', 'Orange')
print(fruits[:3])

# Count how many times 5 appears in a tuple.
numbers = (5, 10, 5, 15, 5)
count = numbers.count(5)
print(f"The number 5 appears {count} times in the tuple.")


# Find the index of "Python" in a tuple of programming languages.
languages = ('Java', 'C++', 'Python', 'JavaScript')
index = languages.index('Python')
print(f"The index of 'Python' in the tuple is: {index}")  



# Concatenate two tuples.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(f"The concatenated tuple is: {concatenated_tuple}")


# Repeat a tuple three times.
repeated_tuple = tuple1 * 3
print(f"The repeated tuple is: {repeated_tuple}")


 # Unpack a tuple
# containing a student's name, age, and grade.
student = ("Alice", 20, "A")
name, age, grade = student
print(f"Name: {name}, Age: {age}, Grade: {grade}")


# Reverse a tuple using slicing.
reversed_tuple = fruits[::-1]
print(f"The reversed tuple is: {reversed_tuple}")

# Convert a tuple to a list, modify one element, and convert it back to a tuple.
fruits_list = list(fruits)
fruits_list[0] = "Grape"
fruits = tuple(fruits_list)
print(f"The modified tuple is: {fruits}")