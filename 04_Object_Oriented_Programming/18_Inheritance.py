# ==========================================================
#                  INHERITANCE IN PYTHON
# ==========================================================

# Inheritance allows one class to inherit the properties
# and methods of another class.

# Parent Class (Base Class)
# Child Class (Derived Class)

# ----------------------------------------------------------
# Example 1 : Single Inheritance
# ----------------------------------------------------------

print("\n------ SINGLE INHERITANCE ------")


class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):

    def bark(self):
        print("Dog is barking.")


dog = Dog()

dog.eat()
dog.bark()

# ----------------------------------------------------------
# Example 2 : Constructor Inheritance
# ----------------------------------------------------------

print("\n------ CONSTRUCTOR INHERITANCE ------")


class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    def study(self):
        print(self.name, "is studying.")


student = Student("Lalit")

print("Student :", student.name)

student.study()

# ----------------------------------------------------------
# Example 3 : Using super()
# ----------------------------------------------------------

print("\n------ SUPER() ------")


class Employee:

    def __init__(self, name):

        self.name = name


class Manager(Employee):

    def __init__(self, name, department):

        super().__init__(name)

        self.department = department

    def display(self):

        print("Name       :", self.name)
        print("Department :", self.department)


manager = Manager("Rahul", "IT")

manager.display()

# ----------------------------------------------------------
# Example 4 : Method Overriding
# ----------------------------------------------------------

print("\n------ METHOD OVERRIDING ------")


class Bird:

    def sound(self):

        print("Bird makes a sound.")


class Parrot(Bird):

    def sound(self):

        print("Parrot says Hello!")


bird = Bird()
parrot = Parrot()

bird.sound()
parrot.sound()

# ----------------------------------------------------------
# Example 5 : Multilevel Inheritance
# ----------------------------------------------------------

print("\n------ MULTILEVEL INHERITANCE ------")


class Grandparent:

    def family(self):
        print("Grandparent")


class Parent(Grandparent):

    def parent(self):
        print("Parent")


class Child(Parent):

    def child(self):
        print("Child")


child = Child()

child.family()
child.parent()
child.child()

# ----------------------------------------------------------
# Example 6 : Multiple Inheritance
# ----------------------------------------------------------

print("\n------ MULTIPLE INHERITANCE ------")


class Father:

    def father_skill(self):
        print("Driving")


class Mother:

    def mother_skill(self):
        print("Cooking")


class Son(Father, Mother):

    def own_skill(self):
        print("Programming")


son = Son()

son.father_skill()
son.mother_skill()
son.own_skill()

# ----------------------------------------------------------
# Example 7 : issubclass() & isinstance()
# ----------------------------------------------------------

print("\n------ issubclass() & isinstance() ------")

print(issubclass(Dog, Animal))

print(isinstance(dog, Dog))

print(isinstance(dog, Animal))

# ----------------------------------------------------------
# Example 8 : Student Result System
# ----------------------------------------------------------

print("\n------ STUDENT RESULT SYSTEM ------")


class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age


class Student(Person):

    def __init__(self, name, age, marks):

        super().__init__(name, age)

        self.marks = marks

    def display(self):

        print("\nStudent Details")

        print("Name  :", self.name)
        print("Age   :", self.age)
        print("Marks :", self.marks)

        if self.marks >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")


students = []

count = int(input("How many students? "))

for i in range(count):

    print(f"\nStudent {i + 1}")

    name = input("Name : ")
    age = int(input("Age : "))
    marks = int(input("Marks : "))

    students.append(Student(name, age, marks))

print("\n------ STUDENT RECORDS ------")

for student in students:
    student.display()

print("\n------ PROGRAM COMPLETED ------")