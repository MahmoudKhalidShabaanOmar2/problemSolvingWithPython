# write a python program to get passwrd from the user , and then check that password should container aplhanumeric characters only , and the length of the password is grater then eight characters , and less then twenty characters by using function method =>
user_password = input("Please Enter The User Password Is = ")
def check_user_password(user_pass):
    print("The User Password Is : ",user_pass)
    if((user_pass.isalnum()) and (len(user_pass)> 8) and (len(user_pass) < 20)) :
        print("It Is Okay User Password")
    else:
        print("It Is Not Okay User Password")
check_user_password(user_password)