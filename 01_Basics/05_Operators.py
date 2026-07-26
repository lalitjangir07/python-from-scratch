# ------------------------------
# PYTHON OPERATORS
# ------------------------------

# Taking input from the user
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("\n---------- ARITHMETIC OPERATORS ----------")

print("Addition          :", num1 + num2)
print("Subtraction       :", num1 - num2)
print("Multiplication    :", num1 * num2)
print("Division          :", num1 / num2)
print("Floor Division    :", num1 // num2)
print("Modulus           :", num1 % num2)
print("Exponent          :", num1 ** num2)

print("\n---------- COMPARISON OPERATORS ----------")

print("num1 == num2 :", num1 == num2)
print("num1 != num2 :", num1 != num2)
print("num1 > num2  :", num1 > num2)
print("num1 < num2  :", num1 < num2)
print("num1 >= num2 :", num1 >= num2)
print("num1 <= num2 :", num1 <= num2)

print("\n---------- ASSIGNMENT OPERATORS ----------")

x = num1
print("Initial Value:",x)
x += 5
print("After += 5:",x)
x -= 2
print("After -= 2:",x)
x *= 3
print("After *= 3:",x)
x //= 2
print("After //= 2:",x)

print("\n---------- LOGICAL OPERATORS ----------")

age = int(input("Enter your Age: "))
citizen = input("Are you an Indian Citizen? (Yes/No):").lower()
eligible = age >= 18 and citizen == "yes"
print("Eligible to Vote:", eligible)
print("\nNot Operatore Example")
print(not eligible)

print("\n---------- MEMBERSHIP OPERATORS ----------")

name = input("Enter your Name: ")
print("'a' in name      :", "a" in name.lower())
print("'z' not in name  :", "z" not in name.lower())

print("\n---------- IDENTITY OPERATORS ----------")

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b    :", a is b)
print("a is c    :", a is c)
print("a == c    :", a == c)

print("\n---------- PROGRAM COMPLETED ----------")