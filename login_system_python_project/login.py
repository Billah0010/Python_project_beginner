print("*"*40)
welcome="Welcome to Login System"
print(welcome.center(40)) 

print("*"*40)
stored_username=""
stored_password=""

while True:
    print("1. Sign UP")
    print("2. Login")
    print("3. Exit")

    choice= input("Enter your choice: ")
    if choice=="1":
        print ("********Sign up page*********")
        user_name = input("Enter your name: ")

        while True:
            password= input("Enter your password: ")

            strength =0
            if len(password)>=8:
                strength+=1
            else:
                print("Password must be at least 8 character!!!!")
            if any(char.isupper() for char in password):
                strength+=1
            else:
                print("password must contain at least one upper case letter!!!!")
            if any(char.islower() for char in password):
                strength+=1
            else:
                print("password must contain at least one lower case character!!!!")
            if any(char.isdigit() for char in password):
                strength+=1
            else:
                print("Password must contain at least one digit!!!!!")
            if any(char in "!@#$%^&*()_[]/<>?\|~.,:;|" for char in password):
                strength+=1
            else:
                print("password must contain at least one special character!!!!")

            if strength==5:
                confirm_password= input("Confirm Your Password: ")
                
                if password==confirm_password:
                    print("Account Created successfully!!!!!")
                    stored_password=password
                    stored_username=user_name
                    break
                else:
                    print("Password doe not match!!!!")


    
    if choice=="2":
        print("*********Login Page*********")
        if stored_username=="" and stored_password=="":
            print("No Account Found , please Sign UP first!!!!!")
            continue
        attampt=3
        while attampt>0:
            user_name=input("Enter your name: ")
            password=input("Enter your password: ")

            if user_name== stored_username and password==stored_password:
                print("Congratulation, Login Successfull") 
                print("Welcome ,",user_name)
                break
            else:
                attampt-=1
                if attampt==0:
                    print("Invalid Username and Password!!!!!")
                    print("Remaining Atampt: ",attampt)
                else:
                    print("Account Locked!!!!!")
                    print("Too many failed Attampt.")

    if choice==3:
        print("Thank you")
        break
                           
                






        