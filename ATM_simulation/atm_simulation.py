print ("="*80)
start="ATM Management System"
print(start.center(80))
print("="*80)

print("Version 1.0")
print("Developer: Tamanna Billah")
print()
print("="*80)
stored_pin="1287"
balance=500
stored_diposite=""
stored_withdrawal=""
while True:
    print("1. Login")
    print("2. Exit")
    choice= input("Enter your choice: ")

    if choice == "1":
        print("="*80)
        print("User Login")
        print("="*80)
        pin=input("Enter your PIN: ")

        if stored_pin==pin:
            
            print("="*80)
            print("Login Successfull".center(80))
            print()
            while True:

                print("="*80)
                print("Main Menu".center(80))
                print("="*80)
                print()
                print("1. Check Balance")
                print("2. Deposite Money")
                print("3. Withdraw Money")
                print("4. Transiction History")
                print("5. Exit")
                choice=input("Enter your choice: ")

                if choice=="1":
                    print("Your Current Balance is: ",balance, "Taka")

                elif choice=="2":
                    deposite=float(input("Enter the amount: "))
                    pin=input("Enter the PIN: ")
                    if stored_pin==pin:
                        balance+=deposite
                        print("Blance after deposite: ", balance, "Taka")
                        stored_diposite=balance
                    else:
                        print("Invalid PIN!!!!")
                        print("Please Try Again") 
                elif choice=="3":
                    withdraw=float(input("Enter the amount: "))
                    pin=input("Enter the pin: ")
                    if stored_pin==pin:
                        if withdraw<=balance:
                            balance-=withdraw
                            print("Withdrawal Successful!")
                            print("Balance after withdrawal: ", balance, "Taka")
                            stored_withdrawal=balance
                        else:
                            print("Insufficient Balance!!!!")
                    else:
                        print("Invalid PIN!!!!")
                        print("Please Try Again")

                elif choice=="4":
                    print("="*80)
                    print("Transectio History".center(80))
                    print("="*80)
                    print()
                    print("Diposit: ",stored_diposite,"Taka")
                    print("Withdraw: ",stored_withdrawal, "Taka")
                    print("Balance: ",balance)
                    print()
                    print("-"*80)       

                

                elif choice=="5":
                    print()
                    print("Back to main menu")
                    print("="*80)
                    
                    print() 
                   
                    break
                else:
                    print("Invalid Choice!!!!")

    elif choice =="2":
        print()
        print("="*80)
        print("Thank You For Using ATM Management System".center(80))
        print() 
        
        print("Have a nice Day!".center(80))

        exit()           