# write a python program to get the user password that contain alphanumeric characters , and the length of the user password is grater than eight , and less than twenty characters , and then restrict user if include uppercase letter , or white spaces =>
user_password = input("Please Enter The User Password Is : ")
print("The User Password Is : ",user_password)
if(user_password.isalnum() and not user_password.isalpha() and not user_password.isdigit() and not user_password.upper() and not user_password.isspace()):
    if(len(user_password) > 8 and len(user_password) < 20):
        print("Hello , And Welccome Back")
    else: 
        print("Sorry , This Is Invalid User Password , Because The Length Of The User Password Is Less Than Eight Characters , Or Grater Than Twenty Characters.")
else:
    print("This Is Invalid User Password , Because The User Password Contains Alphabetic Characters , Numeric Characters Only , Capital Characters (UpperCase Characters) , or White Spaces.")