# ==========================================================
#                     SETS IN PYTHON
# ==========================================================

# A Set is an unordered collection of unique elements.
# Sets do not allow duplicate values.
# Sets are mutable, but their elements must be immutable.

# ----------------------------------------------------------
# Example 1 : Creating Sets
# ----------------------------------------------------------

print("\n------ CREATING SETS ------")

fruits = {"Apple", "Banana", "Mango", "Orange", "Apple"}

print("Set :", fruits)
print("Notice that duplicate values are removed.")

# ----------------------------------------------------------
# Example 2 : Adding Elements
# ----------------------------------------------------------

print("\n------ ADDING ELEMENTS ------")

fruits.add("Pineapple")

print(fruits)

# ----------------------------------------------------------
# Example 3 : Updating Sets
# ----------------------------------------------------------

print("\n------ UPDATE ------")

fruits.update(["Kiwi", "Watermelon", "Grapes"])

print(fruits)

# ----------------------------------------------------------
# Example 4 : Removing Elements
# ----------------------------------------------------------

print("\n------ REMOVING ELEMENTS ------")

fruits.remove("Banana")

print(fruits)

fruits.discard("Papaya")

print("discard() does not give an error if the item is missing.")

print(fruits)

# ----------------------------------------------------------
# Example 5 : Membership
# ----------------------------------------------------------

print("\n------ MEMBERSHIP ------")

search = input("Enter a fruit: ")

if search in fruits:
    print(search, "is available.")
else:
    print(search, "is NOT available.")

# ----------------------------------------------------------
# Example 6 : Looping Through Sets
# ----------------------------------------------------------

print("\n------ LOOPING ------")

for fruit in fruits:
    print(fruit)

# ----------------------------------------------------------
# Example 7 : Union
# ----------------------------------------------------------

print("\n------ UNION ------")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set 1 :", set1)
print("Set 2 :", set2)

print("Union :", set1.union(set2))

# ----------------------------------------------------------
# Example 8 : Intersection
# ----------------------------------------------------------

print("\n------ INTERSECTION ------")

print("Intersection :", set1.intersection(set2))

# ----------------------------------------------------------
# Example 9 : Difference
# ----------------------------------------------------------

print("\n------ DIFFERENCE ------")

print("Set1 - Set2 :", set1.difference(set2))
print("Set2 - Set1 :", set2.difference(set1))

# ----------------------------------------------------------
# Example 10 : Symmetric Difference
# ----------------------------------------------------------

print("\n------ SYMMETRIC DIFFERENCE ------")

print(set1.symmetric_difference(set2))

# ----------------------------------------------------------
# Example 11 : Length
# ----------------------------------------------------------

print("\n------ LENGTH ------")

print(len(fruits))

# ----------------------------------------------------------
# Example 12 : Copy & Clear
# ----------------------------------------------------------

print("\n------ COPY & CLEAR ------")

copy_set = fruits.copy()

print("Copied Set :", copy_set)

copy_set.clear()

print("After clear() :", copy_set)

# ----------------------------------------------------------
# Example 13 : Student Attendance
# ----------------------------------------------------------

print("\n------ STUDENT ATTENDANCE ------")

students = set()

total = int(input("How many students are present? "))

for i in range(total):

    name = input(f"Enter Student {i + 1}: ")

    students.add(name)

print("\nStudents Present:")

for student in students:
    print(student)

print("Total Unique Students :", len(students))

# ----------------------------------------------------------
# Example 14 : Frozen Set
# ----------------------------------------------------------

print("\n------ FROZEN SET ------")

numbers = frozenset([1, 2, 3, 4, 5])

print(numbers)

print("Frozen sets cannot be modified.")

print("\n------ PROGRAM COMPLETED ------")