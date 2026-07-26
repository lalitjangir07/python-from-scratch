# ==========================================================
#                  FUNCTIONS IN PYTHON
# ==========================================================

# A function is a block of reusable code that performs
# a specific task. Instead of writing the same code again
# and again, we can write it once and call it whenever needed.

# ----------------------------------------------------------
# Example 1 : Simple Function
# ----------------------------------------------------------

print("\n------ SIMPLE FUNCTION ------")

def greet():
    print("Welcome to Python!")

greet()

# ----------------------------------------------------------
# Example 2 : Function with Parameters
# ----------------------------------------------------------

print("\n------ FUNCTION WITH PARAMETERS ------")

def greet_user(name):
    print("Hello,", name)

greet_user("Lalit")
greet_user("Rahul")

# ----------------------------------------------------------
# Example 3 : Function with Return Value
# ----------------------------------------------------------

print("\n------ RETURN VALUE ------")

def add(a, b):
    return a + b

result = add(15, 25)

print("Sum =", result)

# ----------------------------------------------------------
# Example 4 : Multiple Return Values
# ----------------------------------------------------------

print("\n------ MULTIPLE RETURN VALUES ------")

def calculate(a, b):
    return a + b, a - b, a * b, a / b

addition, subtraction, multiplication, division = calculate(20, 5)

print("Addition       :", addition)
print("Subtraction    :", subtraction)
print("Multiplication :", multiplication)
print("Division       :", division)

# ----------------------------------------------------------
# Example 5 : Default Parameters
# ----------------------------------------------------------

print("\n------ DEFAULT PARAMETERS ------")

def country(name, nation="India"):
    print(name, "belongs to", nation)

country("Lalit")
country("John", "USA")

# ----------------------------------------------------------
# Example 6 : Keyword Arguments
# ----------------------------------------------------------

print("\n------ KEYWORD ARGUMENTS ------")

def student(name, age, course):
    print("Name   :", name)
    print("Age    :", age)
    print("Course :", course)

student(course="MCA", age=24, name="Lalit")

# ----------------------------------------------------------
# Example 7 : Local and Global Variables
# ----------------------------------------------------------

print("\n------ LOCAL & GLOBAL VARIABLES ------")

college = "OM Sterling Global University"

def show():
    department = "Computer Science"

    print("College   :", college)
    print("Department:", department)

show()

print("College:", college)

# ----------------------------------------------------------
# Example 8 : Even or Odd using Function
# ----------------------------------------------------------

print("\n------ EVEN OR ODD ------")

def even_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"

num = int(input("Enter a Number: "))

print(num, "is", even_odd(num))

# ----------------------------------------------------------
# Example 9 : Factorial using Function
# ----------------------------------------------------------

print("\n------ FACTORIAL ------")

def factorial(number):

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact

num = int(input("Enter a Number: "))

print("Factorial =", factorial(num))

# ----------------------------------------------------------
# Example 10 : Prime Number using Function
# ----------------------------------------------------------

print("\n------ PRIME NUMBER ------")

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):

        if number % i == 0:
            return False

    return True

num = int(input("Enter a Number: "))

if is_prime(num):
    print(num, "is Prime")
else:
    print(num, "is NOT Prime")

# ----------------------------------------------------------
# Example 11 : Calculator using Functions
# ----------------------------------------------------------

print("\n------ SIMPLE CALCULATOR ------")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):

    if b == 0:
        return "Cannot divide by zero"

    return a / b

num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number: "))

print("Addition       :", add(num1, num2))
print("Subtraction    :", subtract(num1, num2))
print("Multiplication :", multiply(num1, num2))
print("Division       :", divide(num1, num2))

print("\n------ PROGRAM COMPLETED ------")