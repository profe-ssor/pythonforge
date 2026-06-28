#text = "Computer Science"

# Extract and print "Computer"
print(text[:8])

# Extract and print "Science"
print(text[9:])

# Print the last 3 characters
print(text[-3:])

#2 word = "programming"
word = "Programming"

# Print the 2nd to 6th character
print(word[1:6])

# Print the word in reverse
print(word[::-1])


#3fullname = "Cypher, Adjei"

parts = fullname.split(", ")

print("First Name:", parts[0])
print("Last Name:", parts[1])


#4 data = "HTML-CSS-JAVASCRIPT-PYTHON"

techs = data.split("-")

for tech in techs:
    print(tech)

#Setion C
    sentence = "I love Java"
print(sentence.replace("Java", "Python"))

#5
text = "banana banana banana"
print(text.replace("banana", "mango", 2))

#6
text = "banana banana banana"
parts = text.split()
parts[1] = "mango"
print(" ".join(parts))


#7
email = "   student@gmail.com   "
print(email.strip())


#8
name = "   Cypher Adjei   "
print(name.strip().upper())


 #Section E: Case Conversion

 #9
text = "python programming is fun"
print(text.upper())
print(text.title())


#10
text = "DATA SCIENCE"
print(text.lower())

#Section F: Mixed Challenge
#text = "  cypher, adjei  "

text = "  cypher, adjei  "
clean_text = text.strip().title()
names = clean_text.split(", ")
print("First Name:", names[0])
print("Last Name:", names[1])

#Given:
text = "Hello, Hello World"

text = "Hello, Hello World"
print(text.replace("Hello", "Mello", 1))



