# ----------------------------------------
# CONDITIONAL STATEMENTS IN PYTHON
# ----------------------------------------

# A conditional statment allows the program to make decisions
# based on wheather a condition is True or False

# ----------------------------------------
# Example 1: Simple if Statement
# ----------------------------------------

print("\n---------- EXAMPLE 1 : IF ----------")

age = int(input("Enter your Age: "))

if age >= 18:
    print("You are eligible to vote")

# ----------------------------------------
# Example 2: if - else
# ----------------------------------------

print("\n---------- EXAMPLE 2 : IF - ELSE ----------")

marks = int(input("Enter your Marks: "))

if marks >= 40:
    print("Result : PASS")
else:
    print("Result : FAIL")

# ----------------------------------------
# Example 3: if - elif - else
# ----------------------------------------

print("\n---------- EXAMPLE 3 : IF - ELIF - ELSE ----------")

percentage = float(input("Enter your Percentage: "))

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade ="D"
else:
    grade = "F"

print("Grade :", grade)

# ----------------------------------------
# Example 4: Multiple Conditions
# ----------------------------------------

print("\n---------- EXAMPLE 4 : AND / OR ----------")

age - int(input("Enter your Age: "))
citizen = input ("Are you an Indian Citizen? (Yes/No): ").lower()

if age >= 18 and citizen == "yes":
    print("Eligible to Vote.")
else:
    print("Not Eligible to Vote.")

# ----------------------------------------
# Example 5: Nested if
# ----------------------------------------

print("\n---------- EXAMPLE 5 : NESTED IF ----------")

username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("User Not Found")

# ----------------------------------------
# Example 6: Largest of Three Numbers
# ----------------------------------------

print("\n---------- EXAMPLE 6 : LARGEST NUMBER ----------")

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
num3 = int(input("Third Number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else: 
    largest = num3

print("Largest Number: ", largest)

# ---------------------------------------
# Example 7: Even or Odd
# ---------------------------------------

print("\n---------- EXAMPLE 7 : EVEN OR ODD ----------")

number = int(input("Enter a Number: "))

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

# ----------------------------------------
# Example 8: Leap Year Checker
# ----------------------------------------

print("\n---------- EXAMPLE 8 : LEAP YEAR ----------")

year = int(input("Enter Year: "))

if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else: 
    print(year, "is NOT a Leap Year")

print("\n---------- PROGRAM COMPLETED ----------")