# ==========================================================
#                FILE HANDLING IN PYTHON
# ==========================================================

# File Handling allows Python programs to create, read,
# write, append and delete files.

# ----------------------------------------------------------
# Example 1 : Creating & Writing to a File
# ----------------------------------------------------------

print("\n------ WRITE MODE (w) ------")

file = open("sample.txt", "w")

file.write("Welcome to Python File Handling.\n")
file.write("This file was created using Python.\n")

file.close()

print("Data written successfully.")

# ----------------------------------------------------------
# Example 2 : Reading a File
# ----------------------------------------------------------

print("\n------ READ MODE (r) ------")

file = open("sample.txt", "r")

print(file.read())

file.close()

# ----------------------------------------------------------
# Example 3 : Appending Data
# ----------------------------------------------------------

print("\n------ APPEND MODE (a) ------")

file = open("sample.txt", "a")

file.write("Appending a new line.\n")

file.close()

print("Data appended successfully.")

# ----------------------------------------------------------
# Example 4 : Reading Line by Line
# ----------------------------------------------------------

print("\n------ READLINE() ------")

file = open("sample.txt", "r")

for line in file:
    print(line.strip())

file.close()

# ----------------------------------------------------------
# Example 5 : readlines()
# ----------------------------------------------------------

print("\n------ READLINES() ------")

file = open("sample.txt", "r")

lines = file.readlines()

print(lines)

file.close()

# ----------------------------------------------------------
# Example 6 : Using with Statement
# ----------------------------------------------------------

print("\n------ WITH STATEMENT ------")

with open("sample.txt", "r") as file:
    print(file.read())

print("File closed automatically.")

# ----------------------------------------------------------
# Example 7 : File Exists Check
# ----------------------------------------------------------

print("\n------ FILE EXISTS ------")

import os

if os.path.exists("sample.txt"):
    print("File Exists")
else:
    print("File Does Not Exist")

# ----------------------------------------------------------
# Example 8 : File Information
# ----------------------------------------------------------

print("\n------ FILE INFORMATION ------")

if os.path.exists("sample.txt"):

    print("File Size :", os.path.getsize("sample.txt"), "bytes")

# ----------------------------------------------------------
# Example 9 : Renaming a File
# ----------------------------------------------------------

print("\n------ RENAME FILE ------")

if os.path.exists("sample.txt"):

    if os.path.exists("python_notes.txt"):

        choice = input(
            "python_notes.txt already exists. Replace it? (yes/no): "
        ).lower()

        if choice == "yes":
            os.remove("python_notes.txt")
            os.rename("sample.txt", "python_notes.txt")
            print("File Replaced Successfully.")
        else:
            print("Rename Cancelled.")

    else:
        os.rename("sample.txt", "python_notes.txt")
        print("File Renamed Successfully.")

else:
    print("sample.txt not found.")
# ----------------------------------------------------------
# Example 10 : Reading Renamed File
# ----------------------------------------------------------

print("\n------ READ RENAMED FILE ------")

if os.path.exists("python_notes.txt"):

    with open("python_notes.txt", "r") as file:
        print(file.read())

# ----------------------------------------------------------
# Example 11 : Copy File
# ----------------------------------------------------------

print("\n------ COPY FILE ------")

import shutil

if os.path.exists("python_notes.txt"):

    shutil.copy("python_notes.txt", "backup_notes.txt")

    print("Backup Created")

# ----------------------------------------------------------
# Example 12 : Delete Backup File
# ----------------------------------------------------------

print("\n------ DELETE FILE ------")

if os.path.exists("backup_notes.txt"):

    os.remove("backup_notes.txt")

    print("Backup Deleted")

# ----------------------------------------------------------
# Example 13 : Mini Project
# ----------------------------------------------------------

print("\n------ STUDENT RECORD SYSTEM ------")

filename = "students.txt"

while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":

        name = input("Enter Student Name : ")

        with open(filename, "a") as file:
            file.write(name + "\n")

        print("Student Added Successfully.")

    elif choice == "2":

        if os.path.exists(filename):

            with open(filename, "r") as file:
                print("\nStudent List\n")
                print(file.read())

        else:
            print("No Student Records Found.")

    elif choice == "3":

        print("Exiting Program...")
        break

    else:

        print("Invalid Choice.")

print("\n------ PROGRAM COMPLETED ------")