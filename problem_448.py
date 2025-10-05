# write a python program to get password from the user , and then check if the user password contains alpha numeric , and more than eight , and less than twenty characters =>
user_password = input("Please Enter The User Password Is : ")
print("The User Password Is : ",user_password)
if(user_password.isalnum() and not user_password.isalpha() and not user_password.isdigit()):
    if(len(user_password) > 8 and len(user_password) < 20):
        print("Hello , And Welcome Back")
    else:
        print("The User Password Is Invalid , Because The Length Of The Password Is Less Than Eight , Or Grater Than Twenty.")
else:
    print("The User Password Is Invalid , Because The User Password Is Only Container Alphabetics Charaters , Or Numeric Characters Only , But You Should Use Merge Of Numeric Charaters , And Alphabetic Character In The Same Time.")