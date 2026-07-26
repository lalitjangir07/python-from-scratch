# ==========================================================
#              EXCEPTION HANDLING IN PYTHON
# ==========================================================

# Exception Handling allows a program to handle errors
# without crashing.

# ----------------------------------------------------------
# Example 1 : Basic try-except
# ----------------------------------------------------------

print("\n------ BASIC TRY-EXCEPT ------")

try:
    num = int(input("Enter a Number: "))
    print("You entered:", num)

except ValueError:
    print("Invalid Input! Please enter an integer.")

# ----------------------------------------------------------
# Example 2 : Division by Zero
# ----------------------------------------------------------

print("\n------ DIVISION BY ZERO ------")

try:
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

# ----------------------------------------------------------
# Example 3 : Multiple Exceptions
# ----------------------------------------------------------

print("\n------ MULTIPLE EXCEPTIONS ------")

try:
    number = int(input("Enter a Number: "))
    answer = 100 / number

    print(answer)

except ValueError:
    print("Please enter only numbers.")

except ZeroDivisionError:
    print("Zero is not allowed.")

# ----------------------------------------------------------
# Example 4 : else Block
# ----------------------------------------------------------

print("\n------ ELSE BLOCK ------")

try:
    age = int(input("Enter your Age: "))

except ValueError:
    print("Invalid Age")

else:
    print("Age Accepted")

# ----------------------------------------------------------
# Example 5 : finally Block
# ----------------------------------------------------------

print("\n------ FINALLY BLOCK ------")

try:
    print("Opening File...")
    file = open("demo.txt", "w")
    file.write("Python Exception Handling")

except Exception as e:
    print("Error:", e)

finally:
    file.close()
    print("File Closed Successfully.")

# ----------------------------------------------------------
# Example 6 : Catching Any Exception
# ----------------------------------------------------------

print("\n------ GENERIC EXCEPTION ------")

try:
    number = int(input("Enter Number: "))
    print(50 / number)

except Exception as e:
    print("Error:", e)

# ----------------------------------------------------------
# Example 7 : Raising an Exception
# ----------------------------------------------------------

print("\n------ RAISE ------")

age = int(input("Enter Age: "))

try:

    if age < 18:
        raise ValueError("You must be at least 18 years old.")

    print("Access Granted")

except ValueError as e:
    print(e)

# ----------------------------------------------------------
# Example 8 : Mini Project
# ----------------------------------------------------------

print("\n------ SIMPLE CALCULATOR ------")

try:

    num1 = float(input("Enter First Number : "))
    operator = input("Enter Operator (+ - * /): ")
    num2 = float(input("Enter Second Number: "))

    if operator == "+":
        print("Result =", num1 + num2)

    elif operator == "-":
        print("Result =", num1 - num2)

    elif operator == "*":
        print("Result =", num1 * num2)

    elif operator == "/":

        if num2 == 0:
            raise ZeroDivisionError

        print("Result =", num1 / num2)

    else:
        raise ValueError("Invalid Operator")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError as e:
    print("Error:", e)

print("\n------ PROGRAM COMPLETED ------")