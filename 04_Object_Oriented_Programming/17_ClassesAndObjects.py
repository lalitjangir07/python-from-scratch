# ==========================================================
#              CLASSES & OBJECTS IN PYTHON
# ==========================================================

# A Class is a blueprint for creating objects.
# An Object is an instance of a class.

# ----------------------------------------------------------
# Example 1 : Creating a Class & Object
# ----------------------------------------------------------

print("\n------ CLASS & OBJECT ------")


class Student:

    name = "Lalit"
    age = 24


student1 = Student()

print("Name :", student1.name)
print("Age  :", student1.age)

# ----------------------------------------------------------
# Example 2 : Constructor (__init__)
# ----------------------------------------------------------

print("\n------ CONSTRUCTOR (__init__) ------")


class Employee:

    def __init__(self, name, department, salary):

        self.name = name
        self.department = department
        self.salary = salary


employee1 = Employee("Lalit", "IT", 50000)

print("Name       :", employee1.name)
print("Department :", employee1.department)
print("Salary     :", employee1.salary)

# ----------------------------------------------------------
# Example 3 : Multiple Objects
# ----------------------------------------------------------

print("\n------ MULTIPLE OBJECTS ------")

employee2 = Employee("Rahul", "HR", 45000)

print(employee2.name)
print(employee2.department)
print(employee2.salary)

# ----------------------------------------------------------
# Example 4 : Methods
# ----------------------------------------------------------

print("\n------ METHODS ------")


class Car:

    def __init__(self, company, model):

        self.company = company
        self.model = model

    def display(self):

        print("Company :", self.company)
        print("Model   :", self.model)


car1 = Car("Toyota", "Fortuner")

car1.display()

# ----------------------------------------------------------
# Example 5 : Updating Object Data
# ----------------------------------------------------------

print("\n------ MODIFY OBJECT ------")

car1.model = "Innova"

car1.display()

# ----------------------------------------------------------
# Example 6 : Deleting Object Attribute
# ----------------------------------------------------------

print("\n------ DELETE ATTRIBUTE ------")

student2 = Student()

student2.city = "Hanumangarh"

print(student2.city)

del student2.city

print("Attribute Deleted")

# ----------------------------------------------------------
# Example 7 : Class Variables
# ----------------------------------------------------------

print("\n------ CLASS VARIABLES ------")


class College:

    college_name = "OM Sterling Global University University"

    def __init__(self, student):

        self.student = student


c1 = College("Lalit")
c2 = College("Rahul")

print(c1.student)
print(c2.student)

print(College.college_name)

# ----------------------------------------------------------
# Example 8 : Instance Variables
# ----------------------------------------------------------

print("\n------ INSTANCE VARIABLES ------")

print(c1.student)
print(c2.student)

# ----------------------------------------------------------
# Example 9 : Mini Project
# ----------------------------------------------------------

print("\n------ STUDENT MANAGEMENT SYSTEM ------")


class Student:

    def __init__(self, roll, name, marks):

        self.roll = roll
        self.name = name
        self.marks = marks

    def display(self):

        print("\nStudent Details")
        print("Roll Number :", self.roll)
        print("Name        :", self.name)
        print("Marks       :", self.marks)

        if self.marks >= 40:
            print("Result      : PASS")
        else:
            print("Result      : FAIL")


students = []

count = int(input("How many students? "))

for i in range(count):

    print(f"\nStudent {i + 1}")

    roll = int(input("Roll Number : "))
    name = input("Name : ")
    marks = int(input("Marks : "))

    student = Student(roll, name, marks)

    students.append(student)

print("\n------ STUDENT RECORDS ------")

for student in students:
    student.display()

print("\n------ PROGRAM COMPLETED ------")