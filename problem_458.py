# write a python program to get user password from the user , and then check if the user password container alphanumeric , and more tham eight characters , and less than twenty characters by using function method =>
user_password = input("Please Enter Ths User Password Is : ")
def check_user_password(u_pass):
    print("The User Password Is : ",u_pass)
    if(not user_password.isdigit() and not user_password.isalpha() and user_password.isalnum()):
        if(len(user_password) > 8 and len(user_password) < 20):
            print("Password Is Okay")
        else:
            print("The Length Of The Password Is Less Than Eight , Or Grater Than Twenty , Please Enter New User Password.")
    else:
        print("The User Password Is Not Okay , Because User Password Only Contains Numeric Characters , Or Alphabetic Characters Only.")
check_user_password(user_password)