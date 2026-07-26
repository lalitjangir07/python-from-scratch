# ==========================================================
#                 ENCAPSULATION IN PYTHON
# ==========================================================

# Encapsulation means wrapping data (variables) and methods
# into a single unit (class) while restricting direct access
# to the data.

# Public     -> Accessible from anywhere
# Protected  -> Accessible inside the class and subclasses
# Private    -> Accessible only inside the class

# ----------------------------------------------------------
# Example 1 : Public Members
# ----------------------------------------------------------

print("\n------ PUBLIC MEMBERS ------")


class Student:

    def __init__(self, name):

        self.name = name


student = Student("Lalit")

print(student.name)

student.name = "Rahul"

print(student.name)

# ----------------------------------------------------------
# Example 2 : Protected Members
# ----------------------------------------------------------

print("\n------ PROTECTED MEMBERS ------")


class Employee:

    def __init__(self, salary):

        self._salary = salary


employee = Employee(50000)

print(employee._salary)

# ----------------------------------------------------------
# Example 3 : Private Members
# ----------------------------------------------------------

print("\n------ PRIVATE MEMBERS ------")


class BankAccount:

    def __init__(self, account_holder, balance):

        self.account_holder = account_holder
        self.__balance = balance

    def show_balance(self):

        print("Balance :", self.__balance)


account = BankAccount("Lalit", 10000)

account.show_balance()

# print(account.__balance)   # Error

# ----------------------------------------------------------
# Example 4 : Name Mangling
# ----------------------------------------------------------

print("\n------ NAME MANGLING ------")

print(account._BankAccount__balance)

# ----------------------------------------------------------
# Example 5 : Getter and Setter
# ----------------------------------------------------------

print("\n------ GETTERS & SETTERS ------")


class Person:

    def __init__(self):

        self.__age = 0

    def set_age(self, age):

        if age >= 0:
            self.__age = age
        else:
            print("Invalid Age")

    def get_age(self):

        return self.__age


person = Person()

person.set_age(24)

print("Age :", person.get_age())

# ----------------------------------------------------------
# Example 6 : Property Decorator
# ----------------------------------------------------------

print("\n------ @property DECORATOR ------")


class Circle:

    def __init__(self, radius):

        self.__radius = radius

    @property
    def radius(self):

        return self.__radius

    @radius.setter
    def radius(self, value):

        if value > 0:
            self.__radius = value
        else:
            print("Radius must be positive.")


circle = Circle(10)

print("Radius :", circle.radius)

circle.radius = 20

print("Updated Radius :", circle.radius)

# ----------------------------------------------------------
# Example 7 : ATM System
# ----------------------------------------------------------

print("\n------ ATM SYSTEM ------")


class ATM:

    def __init__(self, pin, balance):

        self.__pin = pin
        self.__balance = balance

    def check_balance(self, entered_pin):

        if entered_pin == self.__pin:
            print("Balance :", self.__balance)
        else:
            print("Incorrect PIN")

    def deposit(self, entered_pin, amount):

        if entered_pin == self.__pin:

            self.__balance += amount

            print("Deposit Successful")

        else:

            print("Incorrect PIN")

    def withdraw(self, entered_pin, amount):

        if entered_pin != self.__pin:

            print("Incorrect PIN")

        elif amount > self.__balance:

            print("Insufficient Balance")

        else:

            self.__balance -= amount

            print("Withdrawal Successful")


atm = ATM(1234, 5000)

atm.check_balance(1234)

atm.deposit(1234, 1000)

atm.withdraw(1234, 2000)

atm.check_balance(1234)

print("\n------ PROGRAM COMPLETED ------")