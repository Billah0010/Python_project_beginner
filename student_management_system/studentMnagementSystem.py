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
    print("3. Show Student Information")
    print("4. Search Student")
    print("5. Update Student information")
    print("6. Exit")

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
        print("Student Added successfully!!!")

    if choice == "2":
        search = input("Enter ID: ")
        
        if search == storedStudent_id:
            storedStudent_name=""
            storedStudent_id=""
            storedStudent_age=""
            storedStudent_cgpa=""
            print("Delete Successfull!!!!")
        else:
            print("No Student Found!!")    


    elif choice == "3":
        if storedStudent_id == "":
            print("No Student Found!!!!!!!")
        else:    
            print("="*80)
            print("Student Information")
            print()
            print("Name: ",storedStudent_name)
            print("ID: ",storedStudent_id)
            print("Age: ",storedStudent_age)
            print("CGPA: ",storedStudent_cgpa)

    elif choice == "4":
        search = input ("Enter ID: ")
        if search == storedStudent_id:
            print("Name: ",storedStudent_name)
            print("ID: ",storedStudent_id)
            print("Age: ",storedStudent_age)
            print("CGPA: ",storedStudent_cgpa)

    elif choice == "5":
        search = input("Enter ID: ")
        if search == storedStudent_id :
            storedStudent_name = input("Enter New Name: ")
            storedStudent_id = input("Enter New ID: ")
            storedStudent_age = input("Enter New Age: ")
            storedStudent_cgpa = input("Enter New cgpa: ")

            print()
            print("Inforation Update Successfull!!!!")

        else:
            print("No Student Found")    


    elif choice == "6":
        print()
        print("Thank you for using student management system!!!!".center(80)) 
        print("="*80)
        exit()   