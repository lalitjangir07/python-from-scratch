# ==========================================================
#                  STRINGS IN PYTHON
# ==========================================================

# A string is a sequence of characters.
# Strings are immutable (cannot be changed after creation).

# ----------------------------------------------------------
# Example 1 : Creating Strings
# ----------------------------------------------------------

print("\n------ CREATING STRINGS ------")

name = "Lalit"

print(name)
print(type(name))

# ----------------------------------------------------------
# Example 2 : Indexing
# ----------------------------------------------------------

print("\n------ INDEXING ------")

print("First Character :", name[0])
print("Second Character:", name[1])
print("Last Character  :", name[-1])

# ----------------------------------------------------------
# Example 3 : String Slicing
# ----------------------------------------------------------

print("\n------ STRING SLICING ------")

print(name[0:3])
print(name[2:])
print(name[:4])
print(name[::-1])

# ----------------------------------------------------------
# Example 4 : String Length
# ----------------------------------------------------------

print("\n------ LENGTH ------")

print(len(name))

# ----------------------------------------------------------
# Example 5 : Upper & Lower Case
# ----------------------------------------------------------

print("\n------ CASE CONVERSION ------")

print(name.upper())
print(name.lower())

# ----------------------------------------------------------
# Example 6 : Capitalize & Title
# ----------------------------------------------------------

print("\n------ CAPITALIZE & TITLE ------")

sentence = "python programming language"

print(sentence.capitalize())
print(sentence.title())

# ----------------------------------------------------------
# Example 7 : Replace
# ----------------------------------------------------------

print("\n------ REPLACE ------")

text = "I like Java"

print(text.replace("Java", "Python"))

# ----------------------------------------------------------
# Example 8 : Find & Count
# ----------------------------------------------------------

print("\n------ FIND & COUNT ------")

message = "Python is easy. Python is powerful."

print("Find Python :", message.find("Python"))
print("Count Python:", message.count("Python"))

# ----------------------------------------------------------
# Example 9 : Startswith & Endswith
# ----------------------------------------------------------

print("\n------ STARTSWITH & ENDSWITH ------")

filename = "report.pdf"

print(filename.startswith("report"))
print(filename.endswith(".pdf"))

# ----------------------------------------------------------
# Example 10 : Split & Join
# ----------------------------------------------------------

print("\n------ SPLIT & JOIN ------")

subjects = "Math,Science,English"

subject_list = subjects.split(",")

print(subject_list)

joined = " | ".join(subject_list)

print(joined)

# ----------------------------------------------------------
# Example 11 : Strip
# ----------------------------------------------------------

print("\n------ STRIP ------")

text = "      Python      "

print("Before :", repr(text))
print("After  :", repr(text.strip()))

# ----------------------------------------------------------
# Example 12 : Checking Methods
# ----------------------------------------------------------

print("\n------ STRING CHECK METHODS ------")

print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("HELLO".isupper())
print("hello".islower())

# ----------------------------------------------------------
# Example 13 : Escape Characters
# ----------------------------------------------------------

print("\n------ ESCAPE CHARACTERS ------")

print("Hello\nWorld")
print("Hello\tWorld")
print("He said \"Python is easy\"")

# ----------------------------------------------------------
# Example 14 : String Formatting
# ----------------------------------------------------------

print("\n------ STRING FORMATTING ------")

name = input("Enter Name : ")
age = int(input("Enter Age : "))

print(f"My name is {name} and I am {age} years old.")

# ----------------------------------------------------------
# Example 15 : Membership Operators
# ----------------------------------------------------------

print("\n------ MEMBERSHIP ------")

sentence = "Python Programming"

print("Python" in sentence)
print("Java" not in sentence)

# ----------------------------------------------------------
# Example 16 : Mini Project
# ----------------------------------------------------------

print("\n------ PASSWORD STRENGTH CHECKER ------")

password = input("Enter Password : ")

length = len(password)

has_upper = False
has_lower = False
has_digit = False

for ch in password:

    if ch.isupper():
        has_upper = True

    elif ch.islower():
        has_lower = True

    elif ch.isdigit():
        has_digit = True

print("\nPassword Analysis")

print("Length :", length)
print("Uppercase :", has_upper)
print("Lowercase :", has_lower)
print("Digit :", has_digit)

if length >= 8 and has_upper and has_lower and has_digit:
    print("Strong Password")
else:
    print("Weak Password")

print("\n------ PROGRAM COMPLETED ------")