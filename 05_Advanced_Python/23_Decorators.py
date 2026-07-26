# ==========================================================
#                    DECORATORS IN PYTHON
# ==========================================================

# A decorator is a function that modifies the behaviour
# of another function without changing its original code.

# Syntax:
#
# @decorator
# def function():
#     pass

# ----------------------------------------------------------
# Example 1 : Functions are Objects
# ----------------------------------------------------------

print("\n------ FUNCTIONS ARE OBJECTS ------")


def greet():
    print("Hello, Python!")


message = greet

message()

# ----------------------------------------------------------
# Example 2 : Passing Function as Argument
# ----------------------------------------------------------

print("\n------ FUNCTION AS ARGUMENT ------")


def display(function):
    print("Before Function")
    function()
    print("After Function")


def welcome():
    print("Welcome!")


display(welcome)

# ----------------------------------------------------------
# Example 3 : Returning a Function
# ----------------------------------------------------------

print("\n------ RETURNING A FUNCTION ------")


def outer():

    def inner():
        print("Inside Inner Function")

    return inner


result = outer()

result()

# ----------------------------------------------------------
# Example 4 : Creating a Decorator
# ----------------------------------------------------------

print("\n------ SIMPLE DECORATOR ------")


def decorator(function):

    def wrapper():
        print("Before Function")
        function()
        print("After Function")

    return wrapper


@decorator
def hello():
    print("Hello World")


hello()

# ----------------------------------------------------------
# Example 5 : Decorator with Arguments
# ----------------------------------------------------------

print("\n------ DECORATOR WITH ARGUMENTS ------")


def decorator(function):

    def wrapper(name):
        print("Welcome")
        function(name)
        print("Visit Again")

    return wrapper


@decorator
def greet(name):
    print("Hello", name)


greet("Lalit")

# ----------------------------------------------------------
# Example 6 : *args and **kwargs
# ----------------------------------------------------------

print("\n------ *args & **kwargs ------")


def decorator(function):

    def wrapper(*args, **kwargs):

        print("Starting Function")

        function(*args, **kwargs)

        print("Function Completed")

    return wrapper


@decorator
def add(a, b):

    print("Sum =", a + b)


add(10, 20)

# ----------------------------------------------------------
# Example 7 : Execution Time Decorator
# ----------------------------------------------------------

print("\n------ EXECUTION TIMER ------")

import time


def timer(function):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()

        print("Execution Time:", round(end - start, 6), "seconds")

        return result

    return wrapper


@timer
def calculate():

    total = 0

    for i in range(1000000):
        total += i

    return total


calculate()

# ----------------------------------------------------------
# Example 8 : Login Authentication
# ----------------------------------------------------------

print("\n------ LOGIN AUTHENTICATION ------")


def login_required(function):

    logged_in = True

    def wrapper():

        if logged_in:

            function()

        else:

            print("Access Denied")

    return wrapper


@login_required
def dashboard():

    print("Welcome to Dashboard")


dashboard()

print("\n------ PROGRAM COMPLETED ------")