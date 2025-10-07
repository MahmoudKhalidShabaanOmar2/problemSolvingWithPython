# write a python program to get password from the user then check if the user password only contains alphabetic characters , numeric characters , special characters , the length is grater than eight , and less than twenty , and the user restrict if the password contain uppercase (capital) characters , or white spaces by using function method =>
user_password = input("Please Enter The User Password Is : ")
def check_user_password(u_pass):
    print("The User Password Is : ",u_pass)
    if(not user_password.isdigit() and not user_password.isalpha() and not user_password.isupper() and not user_password.isspace() and user_password.isalnum()):
       if(len(user_password) > 8 and len(user_password) < 20): 
            print("Password Is Okay")
       else:
           print("The Password Is Not Okay , Because The Length Is Less Than Eight , Or Grater Than Twenty , Please Enter Another Valid User Password")
    else:
        print("The Password Is Not Okay , Because It Contains Only Numeric Character , Alphabetic Characters Only , Or The User Enter Uppercase (Capital) Characters , Or White Spaces")
check_user_password(user_password)