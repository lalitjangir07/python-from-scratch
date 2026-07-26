# ==========================================================
#                     LISTS IN PYTHON
# ==========================================================

# A list is a collection of multiple items.
# Lists are ordered, mutable (changeable), and allow duplicates.

# ----------------------------------------------------------
# Example 1 : Creating a List
# ----------------------------------------------------------

print("\n------ CREATING A LIST ------")

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("List :", fruits)

# ----------------------------------------------------------
# Example 2 : Accessing Elements
# ----------------------------------------------------------

print("\n------ ACCESSING ELEMENTS ------")

print("First Fruit :", fruits[0])
print("Second Fruit:", fruits[1])
print("Last Fruit  :", fruits[-1])

# ----------------------------------------------------------
# Example 3 : Updating Elements
# ----------------------------------------------------------

print("\n------ UPDATING ELEMENTS ------")

fruits[1] = "Grapes"

print("Updated List :", fruits)

# ----------------------------------------------------------
# Example 4 : Adding Elements
# ----------------------------------------------------------

print("\n------ ADDING ELEMENTS ------")

fruits.append("Pineapple")
print("append() :", fruits)

fruits.insert(2, "Watermelon")
print("insert() :", fruits)

# ----------------------------------------------------------
# Example 5 : Removing Elements
# ----------------------------------------------------------

print("\n------ REMOVING ELEMENTS ------")

fruits.remove("Apple")
print("remove() :", fruits)

removed = fruits.pop()

print("pop() removed :", removed)
print("List :", fruits)

# ----------------------------------------------------------
# Example 6 : List Length
# ----------------------------------------------------------

print("\n------ LENGTH OF LIST ------")

print("Total Items :", len(fruits))

# ----------------------------------------------------------
# Example 7 : Loop Through a List
# ----------------------------------------------------------

print("\n------ LOOPING THROUGH LIST ------")

for fruit in fruits:
    print(fruit)

# ----------------------------------------------------------
# Example 8 : Membership Operators
# ----------------------------------------------------------

print("\n------ MEMBERSHIP ------")

search = input("Enter a fruit to search: ")

if search in fruits:
    print(search, "is available.")
else:
    print(search, "is NOT available.")

# ----------------------------------------------------------
# Example 9 : Sorting
# ----------------------------------------------------------

print("\n------ SORTING ------")

numbers = [45, 12, 89, 3, 56, 22]

print("Original :", numbers)

numbers.sort()

print("Ascending:", numbers)

numbers.sort(reverse=True)

print("Descending:", numbers)

# ----------------------------------------------------------
# Example 10 : Reverse
# ----------------------------------------------------------

print("\n------ REVERSE ------")

numbers.reverse()

print(numbers)

# ----------------------------------------------------------
# Example 11 : Copying a List
# ----------------------------------------------------------

print("\n------ COPYING LIST ------")

copy_numbers = numbers.copy()

print(copy_numbers)

# ----------------------------------------------------------
# Example 12 : List Slicing
# ----------------------------------------------------------

print("\n------ LIST SLICING ------")

print(numbers[0:3])
print(numbers[2:])
print(numbers[:4])
print(numbers[::-1])

# ----------------------------------------------------------
# Example 13 : Nested Lists
# ----------------------------------------------------------

print("\n------ NESTED LIST ------")

students = [
    ["Lalit", 24],
    ["Rahul", 22],
    ["Aman", 23]
]

print(students)

print("First Student :", students[0])
print("Name :", students[0][0])
print("Age  :", students[0][1])

# ----------------------------------------------------------
# Example 14 : Mini Project
# ----------------------------------------------------------

print("\n------ STUDENT MARKS ------")

marks = []

subjects = int(input("How many subjects? "))

for i in range(subjects):

    mark = int(input(f"Enter marks for Subject {i + 1}: "))
    marks.append(mark)

print("\nMarks :", marks)

print("Highest :", max(marks))
print("Lowest  :", min(marks))
print("Total   :", sum(marks))
print("Average :", sum(marks) / len(marks))

print("\n------ PROGRAM COMPLETED ------")