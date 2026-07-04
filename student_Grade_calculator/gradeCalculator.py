print("="*80)
welcome_message="Welcome to the Grade Calculator! "
print(welcome_message.center(80))
print("="*80)
print()
print("Version 1.0")
print("Developer: Tamanna Billah")
print("="*80)
print()
student_name = input("Enter your name : ")
student_ID = input("Enter your student ID : ")
subject_name = input("Enter your subject name : ")
stored_midTerm_mark = 0
stored_finalTerm_mark = 0   
while True:
    print("******** Main Menu*********")
    print()
    print ("Which grade do you want to calculate?")
    print()
    print ("1. Mid Term Grade")
    print ("2. Final Term Grade")
    print("3. Exit")

    choice = input ("Enter your choice: ")

    if choice=="1":
        print("="*50)
        print("Calculating Midterm Grade")
        print("="*50)
        print()
        term_marks = float(input("Enter your term marks: "))
        quiz_marks = float(input("Enter your quiz marks: "))
        attendance_marks = float(input("Enter your attendance marks: "))
        assignment_marks = float(input("Enter your assignment marks: "))
        performance_marks= float(input("Enter your performance marks: "))
        
        if term_marks>100 or quiz_marks>20 or attendance_marks>5 or assignment_marks>20 or performance_marks>5:
            print("Invalid marks entered. please enter valid marks.")
            continue
        else:
            total_marks = (term_marks*0.5) + (quiz_marks) + (attendance_marks) + (assignment_marks) + (performance_marks)
            print("Your total marks is: ", total_marks)
            if total_marks >=90:
                print("your grade is A+")
            elif total_marks >=85:
                print("your grade is A")
            elif total_marks >=80:
                print("your grade is B+")
            elif total_marks >=75:
                print("your grade is B")
            elif total_marks >=70:
                print("your grade is C+")
            elif total_marks >=65:
                print("your grade is C")
            elif total_marks >=60:
                print("your grade is D+")
            else:
                print("your grade is F")
            
            stored_midTerm_mark = total_marks

            
        

    
    
    elif choice=="2":
        print("="*50)
        print("Calculating Final Grade")
        print("="*50)

        term_marks = float(input("Enter your term marks: "))
        quiz_marks = float(input("Enter your quiz marks: "))
        attendance_marks = float(input("Enter your attendance marks: "))
        assignment_marks = float(input("Enter your assignment marks: "))
        performance_marks = float(input("Enter your performance marks: "))

        if term_marks>100 or quiz_marks>20 or attendance_marks>5 or assignment_marks>20 or performance_marks>5:
            print("Invalid marks entered. please enter valid marks.")
            continue
        else:
            total_marks = (term_marks*0.5) + (quiz_marks) + (attendance_marks) + (assignment_marks) + (performance_marks)
            print("Your total marks is: ", total_marks)
            if total_marks >=90:
                print("your grade is A+")
            elif total_marks >=85:
                print("your grade is A")
            elif total_marks >=80:
                print("your grade is B+")
            elif total_marks >=75:
                print("your grade is B")
            elif total_marks >=70:
                print("your grade is C+")
            elif total_marks >=65:
                print("your grade is C")
            elif total_marks >=60:
                print("your grade is D+")
            else:
                print("your grade is F")

            stored_finalTerm_mark = total_marks

        if stored_midTerm_mark!=0 and stored_finalTerm_mark!=0 :
            print ("Do you want to calculate your final grade ? (yes/no)")
            final_grade_choice = input("Enter your choice: ")
            if final_grade_choice.lower() == "yes":
                
                total_marks = (0.4 * stored_midTerm_mark) + (0.6 * stored_finalTerm_mark)
                print("Your total marks is: ", total_marks)
                if total_marks >=90:
                    print("Your grade is A+")
                    grade = "A+"
                elif total_marks>=85:
                    print("Your grade is A")
                    grade = "A"
                elif total_marks>=80:
                    print("Your grade is B+")
                    grade ="B+"    
                elif total_marks>=75:
                    print("Your grade is B")
                    grade = "B"
                elif total_marks>=70:
                    print("Your grade is C+ ")
                    grade = "C+"
                elif total_marks>=65:
                    print("Your grade is C")
                    grade = "C"
                elif total_marks>=60:
                    print ("Your grade is D+")
                    grade = "D+"
                elif total_marks>=50 :
                    print("Your gade is D")
                    grade = "D"
                else:
                    print("Your grade is F")
                    grade = "F"
            elif final_grade_choice.lower() == "no":
                print("\nReturning to Main Menu...\n")
                continue
            else:
                print("\nInvalid choice! Please enter Yes or No.\n")
                continue

            print("="*80)
            print("Final Grade Report") 
            print("="*80)
            print(f"Student name:  {student_name}")
            print(f"Student ID: {student_ID}")
            print(f"Subject: {subject_name}")
            print(f"Mid-Term Grade: {stored_midTerm_mark}")
            print(f"Final-Term Grade: {stored_finalTerm_mark}")
            print(f"Total Grade: {total_marks}")
            print(f"Overall Grade: {grade}")
            print("="*80)

    
    
    
    
    elif choice == "3":
        print("Thank you for using my Grade Calculator. ")
        exit()    
    else:
        print("Invalid Choice")