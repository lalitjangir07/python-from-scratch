# ==========================================================
#                 POLYMORPHISM IN PYTHON
# ==========================================================

# Polymorphism means "Many Forms".
# The same method name can perform different tasks depending
# on the object that calls it.

# ----------------------------------------------------------
# Example 1 : Method Overriding
# ----------------------------------------------------------

print("\n------ METHOD OVERRIDING ------")


class Animal:

    def sound(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def sound(self):
        print("Dog says: Bark")


class Cat(Animal):

    def sound(self):
        print("Cat says: Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# ----------------------------------------------------------
# Example 2 : One Function, Different Objects
# ----------------------------------------------------------

print("\n------ SAME FUNCTION, DIFFERENT OBJECTS ------")


def make_sound(animal):
    animal.sound()


make_sound(dog)
make_sound(cat)

# ----------------------------------------------------------
# Example 3 : Built-in Polymorphism
# ----------------------------------------------------------

print("\n------ BUILT-IN POLYMORPHISM ------")

print(len("Python"))
print(len([10, 20, 30, 40]))
print(len((1, 2, 3)))
print(len({"A": 1, "B": 2}))

# ----------------------------------------------------------
# Example 4 : Operator Polymorphism
# ----------------------------------------------------------

print("\n------ OPERATOR POLYMORPHISM ------")

print(10 + 20)
print("Python " + "Programming")
print([1, 2] + [3, 4])

# ----------------------------------------------------------
# Example 5 : Method Overloading Simulation
# ----------------------------------------------------------

print("\n------ METHOD OVERLOADING ------")


class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(10))
print(calc.add(10, 20))
print(calc.add(10, 20, 30))

# ----------------------------------------------------------
# Example 6 : Different Classes, Same Method
# ----------------------------------------------------------

print("\n------ DIFFERENT CLASSES ------")


class Car:

    def move(self):
        print("Car is driving.")


class Plane:

    def move(self):
        print("Plane is flying.")


class Boat:

    def move(self):
        print("Boat is sailing.")


vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()

# ----------------------------------------------------------
# Example 7 : Employee Salary System
# ----------------------------------------------------------

print("\n------ EMPLOYEE SALARY SYSTEM ------")


class Employee:

    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class PartTimeEmployee(Employee):

    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


employees = [
    FullTimeEmployee(50000),
    PartTimeEmployee(80, 500)
]

for employee in employees:
    print("Salary :", employee.calculate_salary())

print("\n------ PROGRAM COMPLETED ------")