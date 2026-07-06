print("="*80)
print("Welcome To Student Management System".center(80))
print()
print ("Version: 1.0")
print("Developer: Tamanna Billah")
print()
print("="*80)
print()
storedStudent_name=""
storedStudent_id=""
storedStudent_age=0
storedStudent_cgpa=0.0
while True:
    print()
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Show Student List")
    print("4. Search Student")
    print("5. Exit")

    choice=input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        id = input("Enter Student ID: ")
        age = input("Enter Age: ")
        cgpa = input("Enter CGPA: ")
        storedStudent_name = name 
        storedStudent_id = id 
        storedStudent_age = age
        storedStudent_cgpa = cgpa
        print()
        print("Student Added successfully!!!".center(80))
    if choice == "5":
        print()
        print("="*80)
        print("Thank you for using student management system!!!!".center(80))    