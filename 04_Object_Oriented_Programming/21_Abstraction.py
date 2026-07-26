# ==========================================================
#                   ABSTRACTION IN PYTHON
# ==========================================================

# Abstraction means hiding the implementation details
# and showing only the essential features.

# Python provides abstraction using the abc module.

from abc import ABC, abstractmethod

# ----------------------------------------------------------
# Example 1 : Abstract Class
# ----------------------------------------------------------

print("\n------ ABSTRACT CLASS ------")


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog says: Bark")


dog = Dog()

dog.sound()

# ----------------------------------------------------------
# Example 2 : Multiple Child Classes
# ----------------------------------------------------------

print("\n------ MULTIPLE CHILD CLASSES ------")


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


square = Square(5)
rectangle = Rectangle(10, 4)

print("Square Area    :", square.area())
print("Rectangle Area :", rectangle.area())

# ----------------------------------------------------------
# Example 3 : Abstract Method with Normal Methods
# ----------------------------------------------------------

print("\n------ NORMAL + ABSTRACT METHODS ------")


class Vehicle(ABC):

    def start(self):
        print("Vehicle Started")

    @abstractmethod
    def fuel_type(self):
        pass


class Car(Vehicle):

    def fuel_type(self):
        print("Petrol")


class ElectricCar(Vehicle):

    def fuel_type(self):
        print("Electric")


car = Car()
electric = ElectricCar()

car.start()
car.fuel_type()

electric.start()
electric.fuel_type()

# ----------------------------------------------------------
# Example 4 : Banking System
# ----------------------------------------------------------

print("\n------ BANKING SYSTEM ------")


class BankAccount(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):

    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self):
        return self.balance * 0.04


class CurrentAccount(BankAccount):

    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self):
        return 0


accounts = [
    SavingsAccount(10000),
    CurrentAccount(15000)
]

for account in accounts:
    print("Interest :", account.calculate_interest())

# ----------------------------------------------------------
# Example 5 : Payment Gateway
# ----------------------------------------------------------

print("\n------ PAYMENT GATEWAY ------")


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class NetBanking(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking")


payments = [
    CreditCard(),
    UPI(),
    NetBanking()
]

for payment in payments:
    payment.pay(500)

# ----------------------------------------------------------
# Example 6 : Employee Management System
# ----------------------------------------------------------

print("\n------ EMPLOYEE MANAGEMENT SYSTEM ------")


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTime(Employee):

    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class Freelancer(Employee):

    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


employees = [
    FullTime(50000),
    Freelancer(80, 600)
]

for employee in employees:
    print("Salary :", employee.calculate_salary())

print("\n------ PROGRAM COMPLETED ------")