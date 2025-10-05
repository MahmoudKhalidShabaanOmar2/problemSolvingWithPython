# write a python program to get the user password that contain alphanumeric characters , and the length of the user password is grater than eight , and less than twenty characters , and then restrict user if include uppercase letter , or white spaces =>
user_password = input("Please Enter The User Password Is : ")
print("The User Password Is : ",user_password)
if(not user_password.isdigit() and not user_password.isupper() and not user_password.isspace() and user_password.isalnum()):
    if(len(user_password) > 8 and len(user_password) < 20):
        print("Okay , And Welcome Back")
    else:
        print("The User Password Is Invalie , Because The Length Of The User Password Is Grater Than Eight Characters , And Less Than Twenty Characters")
else:
    print("This Is Invalie User Password , Because The User Password Container White Spaces , Capital (Uppercase Characters) , Alphabetic Characters , Or Numeric Characters Only.")