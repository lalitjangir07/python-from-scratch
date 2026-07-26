# ------------------------------
# LOOPS IN PYTHON
# ------------------------------

# A loop is used to execute a block of code repeatedly

# ------------------------------
# Example 1 : FOR LOOP 
# ------------------------------

print("\n---------- FOR LOOP ----------")

for i in range(1, 6):
    print("Count: ", i)

# ------------------------------
# Example 2 : WHILE LOOP
# ------------------------------

print("\n---------- WHILE LOOP ----------")

count = 1

while count <=5:
    print ("Count: ", count)
    count += 1

# ------------------------------
# Example 3 : RANGE FUNCTION
# ------------------------------

print("\n---------- RANGE FUNCTION ----------")

print("range(5)")
for i in range(5):
    print(i)

print("\nrange(2, 8)")
for i in range(2, 8):
    print(i)

print("\nrange(2, 21, 2)")
for i in range(2, 21, 2):
    print(i)

# ------------------------------
# Example 4 : BREAK
# ------------------------------

print("\n---------- BREAK ----------")

for i in range(1, 11):
    if i == 6:
        break
    print(i)

# ------------------------------
# Example 5 : CONTINUE
# ------------------------------

print("\n---------- CONTINUE ----------")

for i in range(1, 11):
    if i == 6:
        continue
    print(i)

# ------------------------------
# Example 6 : PASS
# ------------------------------

print("\n---------- PASS ----------")

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

# ------------------------------
# Example 7 : MULTIPLICATION TABLE
# ------------------------------

print("\n---------- MULTIPLICATION TABLE ----------")

number = int(input("Enter a Number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# ------------------------------
# Example 8 : FACTORIAL
# ------------------------------

print("\n---------- FACTORIAL ----------")

num = int(input("Enter a Number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial: ", factorial)

# ----------------------------------------------------------
# Example 9 : SUM OF FIRST N NUMBERS
# ----------------------------------------------------------

print("\n------ SUM OF N NUMBERS ------")

n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

# ----------------------------------------------------------
# Example 10 : EVEN NUMBERS
# ----------------------------------------------------------

print("\n------ EVEN NUMBERS ------")

for i in range(2, 21, 2):
    print(i)

# ----------------------------------------------------------
# Example 11 : ODD NUMBERS
# ----------------------------------------------------------

print("\n------ ODD NUMBERS ------")

for i in range(1, 20, 2):
    print(i)

# ----------------------------------------------------------
# Example 12 : PRIME NUMBER CHECK
# ----------------------------------------------------------

print("\n------ PRIME NUMBER ------")

number = int(input("Enter a number: "))

is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, number):

        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is Prime")
else:
    print(number, "is NOT Prime")

# ----------------------------------------------------------
# Example 13 : FIBONACCI SERIES
# ----------------------------------------------------------

print("\n------ FIBONACCI SERIES ------")

terms = int(input("Enter number of terms: "))

first = 0
second = 1

for i in range(terms):

    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number

print()

# ----------------------------------------------------------
# Example 14 : NESTED LOOP
# ----------------------------------------------------------

print("\n------ NESTED LOOP ------")

for row in range(1, 4):

    for col in range(1, 4):
        print(col, end=" ")

    print()

# ----------------------------------------------------------
# Example 15 : STAR PATTERN
# ----------------------------------------------------------

print("\n------ STAR PATTERN ------")

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):

    for j in range(i):
        print("*", end=" ")

    print()

print("\n------ PROGRAM COMPLETED ------")