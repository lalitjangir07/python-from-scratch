# ==========================================================
#              MODULES & PACKAGES IN PYTHON
# ==========================================================

# A Module is a Python file containing variables,
# functions or classes.
#
# A Package is a collection of multiple modules.

# ----------------------------------------------------------
# Example 1 : Importing a Module
# ----------------------------------------------------------

print("\n------ IMPORT MODULE ------")

import math

print("Square Root of 25 :", math.sqrt(25))
print("Power :", math.pow(2, 5))
print("Value of PI :", math.pi)

# ----------------------------------------------------------
# Example 2 : Import Specific Functions
# ----------------------------------------------------------

print("\n------ IMPORT SPECIFIC FUNCTION ------")

from math import factorial, ceil

print("Factorial of 5 :", factorial(5))
print("Ceil of 5.2 :", ceil(5.2))

# ----------------------------------------------------------
# Example 3 : Import with Alias
# ----------------------------------------------------------

print("\n------ IMPORT WITH ALIAS ------")

import math as m

print("Floor :", m.floor(8.9))
print("Square Root :", m.sqrt(64))

# ----------------------------------------------------------
# Example 4 : Random Module
# ----------------------------------------------------------

print("\n------ RANDOM MODULE ------")

import random

print("Random Integer :", random.randint(1, 100))
print("Random Choice :", random.choice(["Apple", "Mango", "Banana"]))
print("Random Float :", random.random())

# ----------------------------------------------------------
# Example 5 : Datetime Module
# ----------------------------------------------------------

print("\n------ DATETIME MODULE ------")

import datetime

today = datetime.datetime.now()

print("Current Date & Time :", today)

# ----------------------------------------------------------
# Example 6 : OS Module
# ----------------------------------------------------------

print("\n------ OS MODULE ------")

import os

print("Current Working Directory :")
print(os.getcwd())

# ----------------------------------------------------------
# Example 7 : Statistics Module
# ----------------------------------------------------------

print("\n------ STATISTICS MODULE ------")

import statistics

numbers = [10, 20, 30, 40, 50]

print("Mean :", statistics.mean(numbers))
print("Median :", statistics.median(numbers))

# ----------------------------------------------------------
# Example 8 : Creating Your Own Module
# ----------------------------------------------------------

print("\n------ CUSTOM MODULE ------")

print("Create a file named calculator.py")
print("Store functions inside it.")
print("Then import it using:")
print("import calculator")

# ----------------------------------------------------------
# Example 9 : Mini Project
# ----------------------------------------------------------

print("\n------ GUESS THE NUMBER ------")

secret = random.randint(1, 10)

while True:

    guess = int(input("Guess a number (1-10): "))

    if guess == secret:
        print("Correct!")
        break

    elif guess < secret:
        print("Too Low")

    else:
        print("Too High")

print("\n------ PROGRAM COMPLETED ------")