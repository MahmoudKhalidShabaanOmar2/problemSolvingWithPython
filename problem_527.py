# write a returned function to get passwrd from the user , and then check that password should container aplhanumeric characters only , and the length of the password is grater then eight characters , and less then twenty characters by using python language =>
def check_user_password(u_pass):
    print("The User Password Is : ",str(u_pass))
    if((u_pass.isalnum()) and (len(u_pass) > 8) and (len(u_pass) <= 20)):
        return ("It Is Okay , Because Your Entered Passord Is "+u_pass)
    else:
        return ("It Is Not Okay , Because Your Entered Password Is "+u_pass)
user_password = input("Please Enter The User Password Is : ")
check_user_pass = check_user_password(user_password)
print(check_user_pass)