print("="*40)
welcome="💙💙💙💙💙  Welcome To Password Checker  💙💙💙💙💙"
print(welcome.center(40))
print("="*40)
while True:
   password = input("Enter the Password :")
   print("="*40)
   upper_case=False
   lower_case=False
   digit=False
   special_char=False

   strength=0
   if len(password) >=8:
      print ("Password length: passed")
      strength +=1
   else:
      print ("Password should be at least 8 character long  ")

   if any(char.isupper() for char in password):
      upper_case=True
      print ("Upper case: passs")
      strength+=1
   else:
      print ("Password should have at least one upper case character ")

   if any(char.islower() for char in password):
      lower_case=True
      print ("Lower case: passs")
      strength += 1
   else:
      print ("Password should have at least one lower case character ")

   if any(char.isdigit() for char in password):
      digit=True
      print ("Digit: passs")
      strength += 1
   else:
      print("Password should at least one digit ")

   if any(char in "!@#$%^&*()_+~[]:<>,./?\\|`" for char in password):
      special_char=True
      print ("Special character: passs")
      strength += 1
   else:
      print ("Password should have at least one special character ")

   print("*"*40)

   if strength >= 5:
      print ("Your password is strong")
   elif strength >= 3:
      print ("Your password is medium")
   else:
      print("Your password is weak")      

   print("="*40)


   

    

   while True:

        choice = input("\nDo you want to check another password? (Yes/No): ").strip().lower()

        if choice == "yes":
            break         

        elif choice == "no":
            print("\nThank you for using Password Strength Checker! 💙")
            exit()

        else:
            print("Invalid choice! Please enter Yes or No.")