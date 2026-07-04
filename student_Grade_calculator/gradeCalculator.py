print("="*80)
welcome_message="Welcome to the Grade Calculator! "
print(welcome_message.center(80))

print("="*80)
student_name = input("Enter your name : ")
student_ID = input("Enter your student ID : ")

while True:
    
    subject_name = input("Enter the Subject : ")
    midTerm_marks = float (input ("Enter your mid term marks : "))
    
    if subject_marks >=90:
        print("Your grade is A+")
        grade = "A+"
    elif subject_marks>=85:
        print("Your grade is A")
        grade = "A"
    elif subject_marks>=80:
        print("Your grade is B+")
        grade ="B+"    
    elif subject_marks>=75:
        print("Your grade is B")
        grade = "B"
    elif subject_marks>=70:
        print("Your grade is C+ ")
        grade = "C+"
    elif subject_marks>=65:
        print("Your grade is C")
        grade = "C"
    elif subject_marks>=60:
        print ("Your grade is D+")
        grade = "D+"
    elif subject_marks>=50 :
        print("Your gade is D")
        grade = "D"
    else:
        print("Your grade is F")
        grade = "F"
