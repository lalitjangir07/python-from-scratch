# ==========================================================
#              SPECIAL (MAGIC / DUNDER) METHODS
# ==========================================================

# Dunder means Double UNDERscore.
# Examples:
# __init__()
# __str__()
# __repr__()
# __len__()
# __add__()
# __eq__()

# These methods allow our objects to behave like
# Python's built-in data types.

# ----------------------------------------------------------
# Example 1 : __init__()
# ----------------------------------------------------------

print("\n------ __init__() ------")


class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age


student = Student("Lalit", 24)

print(student.name)
print(student.age)

# ----------------------------------------------------------
# Example 2 : __str__()
# ----------------------------------------------------------

print("\n------ __str__() ------")


class Car:

    def __init__(self, company, model):

        self.company = company
        self.model = model

    def __str__(self):

        return f"{self.company} {self.model}"


car = Car("Toyota", "Fortuner")

print(car)

# ----------------------------------------------------------
# Example 3 : __repr__()
# ----------------------------------------------------------

print("\n------ __repr__() ------")


class Book:

    def __init__(self, title, author):

        self.title = title
        self.author = author

    def __repr__(self):

        return f"Book('{self.title}', '{self.author}')"


book = Book("Python", "Guido")

print(repr(book))

# ----------------------------------------------------------
# Example 4 : __len__()
# ----------------------------------------------------------

print("\n------ __len__() ------")


class Playlist:

    def __init__(self, songs):

        self.songs = songs

    def __len__(self):

        return len(self.songs)


playlist = Playlist(["Song A", "Song B", "Song C"])

print(len(playlist))

# ----------------------------------------------------------
# Example 5 : __add__()
# ----------------------------------------------------------

print("\n------ __add__() ------")


class Number:

    def __init__(self, value):

        self.value = value

    def __add__(self, other):

        return self.value + other.value


num1 = Number(25)
num2 = Number(30)

print(num1 + num2)

# ----------------------------------------------------------
# Example 6 : __eq__()
# ----------------------------------------------------------

print("\n------ __eq__() ------")


class Employee:

    def __init__(self, emp_id):

        self.emp_id = emp_id

    def __eq__(self, other):

        return self.emp_id == other.emp_id


emp1 = Employee(101)
emp2 = Employee(101)
emp3 = Employee(102)

print(emp1 == emp2)
print(emp1 == emp3)

# ----------------------------------------------------------
# Example 7 : __lt__() and __gt__()
# ----------------------------------------------------------

print("\n------ __lt__() & __gt__() ------")


class Product:

    def __init__(self, price):

        self.price = price

    def __lt__(self, other):

        return self.price < other.price

    def __gt__(self, other):

        return self.price > other.price


product1 = Product(1500)
product2 = Product(2500)

print(product1 < product2)
print(product1 > product2)

# ----------------------------------------------------------
# Example 8 : Student Result System
# ----------------------------------------------------------

print("\n------ STUDENT RESULT SYSTEM ------")


class Student:

    def __init__(self, roll, name, marks):

        self.roll = roll
        self.name = name
        self.marks = marks

    def __str__(self):

        return f"{self.roll} - {self.name}"

    def __eq__(self, other):

        return self.roll == other.roll

    def __lt__(self, other):

        return self.marks < other.marks


students = [
    Student(1, "Lalit", 91),
    Student(2, "Rahul", 84),
    Student(3, "Amit", 96)
]

print("\nStudent List")

for student in students:
    print(student)

print("\nHighest Marks")

highest = max(students)

print(highest)

print("\nEquality Test")

print(Student(1, "Lalit", 91) == Student(1, "Someone", 55))

print("\n------ PROGRAM COMPLETED ------")