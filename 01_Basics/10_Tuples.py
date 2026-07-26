# ==========================================================
#                    TUPLES IN PYTHON
# ==========================================================

# A tuple is an ordered collection of items.
# Tuples are immutable (cannot be changed after creation).
# They allow duplicate values.

# ----------------------------------------------------------
# Example 1 : Creating Tuples
# ----------------------------------------------------------

print("\n------ CREATING TUPLES ------")

fruits = ("Apple", "Banana", "Mango", "Orange")

print("Tuple :", fruits)

# ----------------------------------------------------------
# Example 2 : Accessing Elements
# ----------------------------------------------------------

print("\n------ ACCESSING ELEMENTS ------")

print("First Fruit :", fruits[0])
print("Second Fruit:", fruits[1])
print("Last Fruit  :", fruits[-1])

# ----------------------------------------------------------
# Example 3 : Tuple Length
# ----------------------------------------------------------

print("\n------ LENGTH OF TUPLE ------")

print("Total Items :", len(fruits))

# ----------------------------------------------------------
# Example 4 : Loop Through Tuple
# ----------------------------------------------------------

print("\n------ LOOP THROUGH TUPLE ------")

for fruit in fruits:
    print(fruit)

# ----------------------------------------------------------
# Example 5 : Membership Operators
# ----------------------------------------------------------

print("\n------ MEMBERSHIP ------")

search = input("Enter a fruit to search: ")

if search in fruits:
    print(search, "is available.")
else:
    print(search, "is NOT available.")

# ----------------------------------------------------------
# Example 6 : Counting Elements
# ----------------------------------------------------------

print("\n------ COUNT ------")

numbers = (10, 20, 30, 20, 40, 20, 50)

print("Tuple :", numbers)
print("20 appears", numbers.count(20), "times")

# ----------------------------------------------------------
# Example 7 : Finding Index
# ----------------------------------------------------------

print("\n------ INDEX ------")

print("Index of 30 :", numbers.index(30))

# ----------------------------------------------------------
# Example 8 : Tuple Slicing
# ----------------------------------------------------------

print("\n------ TUPLE SLICING ------")

print(numbers[1:5])
print(numbers[:4])
print(numbers[3:])
print(numbers[::-1])

# ----------------------------------------------------------
# Example 9 : Tuple Packing & Unpacking
# ----------------------------------------------------------

print("\n------ PACKING & UNPACKING ------")

student = ("Lalit", 24, "MCA")

name, age, course = student

print("Name   :", name)
print("Age    :", age)
print("Course :", course)

# ----------------------------------------------------------
# Example 10 : Nested Tuple
# ----------------------------------------------------------

print("\n------ NESTED TUPLE ------")

students = (
    ("Lalit", 24),
    ("Rahul", 22),
    ("Aman", 23)
)

for student in students:
    print(student)

# ----------------------------------------------------------
# Example 11 : Tuple Immutability
# ----------------------------------------------------------

print("\n------ IMMUTABILITY ------")

print("Original Tuple :", fruits)

print("\nTrying to change a tuple...")

try:
    fruits[0] = "Pineapple"
except TypeError as e:
    print("Error :", e)

print("Tuple remains unchanged :", fruits)

# ----------------------------------------------------------
# Example 12 : Convert Between List and Tuple
# ----------------------------------------------------------

print("\n------ LIST <-> TUPLE ------")

fruit_list = list(fruits)

fruit_list.append("Pineapple")

new_tuple = tuple(fruit_list)

print("List  :", fruit_list)
print("Tuple :", new_tuple)

# ----------------------------------------------------------
# Example 13 : Student Record
# ----------------------------------------------------------

print("\n------ STUDENT RECORD ------")

student = (
    input("Name : "),
    int(input("Age : ")),
    input("Course : "),
    float(input("Percentage : "))
)

print("\nStudent Details")
print("Name       :", student[0])
print("Age        :", student[1])
print("Course     :", student[2])
print("Percentage :", student[3])

print("\n------ PROGRAM COMPLETED ------")
