# ==========================================================
#                 DICTIONARIES IN PYTHON
# ==========================================================

# A Dictionary stores data in key-value pairs.
# Dictionaries are mutable, ordered (Python 3.7+),
# and keys must be unique.

# ----------------------------------------------------------
# Example 1 : Creating a Dictionary
# ----------------------------------------------------------

print("\n------ CREATING A DICTIONARY ------")

student = {
    "name": "Lalit",
    "age": 24,
    "course": "MCA",
    "percentage": 85.5
}

print(student)

# ----------------------------------------------------------
# Example 2 : Accessing Values
# ----------------------------------------------------------

print("\n------ ACCESSING VALUES ------")

print("Name       :", student["name"])
print("Age        :", student["age"])
print("Course     :", student["course"])
print("Percentage :", student["percentage"])

# ----------------------------------------------------------
# Example 3 : Using get()
# ----------------------------------------------------------

print("\n------ GET METHOD ------")

print(student.get("name"))
print(student.get("city"))
print(student.get("city", "Not Available"))

# ----------------------------------------------------------
# Example 4 : Updating Values
# ----------------------------------------------------------

print("\n------ UPDATING VALUES ------")

student["age"] = 25

print(student)

# ----------------------------------------------------------
# Example 5 : Adding New Key-Value Pair
# ----------------------------------------------------------

print("\n------ ADDING DATA ------")

student["city"] = "Hanumangarh"

print(student)

# ----------------------------------------------------------
# Example 6 : Removing Data
# ----------------------------------------------------------

print("\n------ REMOVING DATA ------")

removed = student.pop("percentage")

print("Removed Percentage :", removed)
print(student)

# ----------------------------------------------------------
# Example 7 : Keys, Values and Items
# ----------------------------------------------------------

print("\n------ KEYS, VALUES & ITEMS ------")

print("Keys   :", student.keys())
print("Values :", student.values())
print("Items  :", student.items())

# ----------------------------------------------------------
# Example 8 : Looping Through Dictionary
# ----------------------------------------------------------

print("\n------ LOOPING ------")

for key, value in student.items():
    print(key, ":", value)

# ----------------------------------------------------------
# Example 9 : Copy & Clear
# ----------------------------------------------------------

print("\n------ COPY & CLEAR ------")

student_copy = student.copy()

print("Copied Dictionary :", student_copy)

temp = student.copy()
temp.clear()

print("After clear() :", temp)

# ----------------------------------------------------------
# Example 10 : Nested Dictionary
# ----------------------------------------------------------

print("\n------ NESTED DICTIONARY ------")

students = {
    101: {"Name": "Lalit", "Age": 24},
    102: {"Name": "Rahul", "Age": 22},
    103: {"Name": "Aman", "Age": 23}
}

for roll, details in students.items():
    print("Roll No :", roll)
    print("Name    :", details["Name"])
    print("Age     :", details["Age"])
    print()

# ----------------------------------------------------------
# Example 11 : Dictionary from User Input
# ----------------------------------------------------------

print("\n------ USER INPUT ------")

employee = {}

employee["ID"] = int(input("Enter Employee ID : "))
employee["Name"] = input("Enter Employee Name : ")
employee["Department"] = input("Enter Department : ")
employee["Salary"] = float(input("Enter Salary : "))

print("\nEmployee Details")

for key, value in employee.items():
    print(key, ":", value)

# ----------------------------------------------------------
# Example 12 : Mini Project
# ----------------------------------------------------------

print("\n------ STUDENT RESULT SYSTEM ------")

student = {}

student["Name"] = input("Student Name : ")
student["Maths"] = int(input("Maths Marks : "))
student["Science"] = int(input("Science Marks : "))
student["English"] = int(input("English Marks : "))

total = (
    student["Maths"] +
    student["Science"] +
    student["English"]
)

average = total / 3

student["Total"] = total
student["Average"] = average

print("\n------ RESULT ------")

for key, value in student.items():
    print(key, ":", value)

print("\n------ PROGRAM COMPLETED ------")