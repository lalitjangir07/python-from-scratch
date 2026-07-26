# -------------------------------
# TYPE CASTING IN PYTHON
# -------------------------------
# String
name = str(input("Enter your Name: "))
# Integer
age = int(input("Enter your Age: "))
# Float
height = float(input("Enter your Height(in feet): "))
# Boolean
student = input("Are you a Student? (True/False): ")
student = student == "True"

print("\n----- USER DETAILS -----")
print("Name     :", name)
print("Age      :", age)
print("Height   :", height)
print("Student  :", student)

print("\n----- DATA TYPES -----")
print(type(name))
print(type(age))
print(type(height))
print(type(student))