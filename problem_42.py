# write a python program to get user name , and password from the user and then make sure that password should contain numbers , and alphabetic =>
user_name = input("please enter the name of the user is : ")
user_password = input("please enter the password of the user is : ")
print("the name of the user is : \""+user_name+"\"")
print("the password of the user is : \""+user_password+"\"")
if(user_password . isalnum()) :
    print("HI \""+user_name+"\" , your user password is OKAY , because your entered user password is : \""+user_password+" , because it contains numeric , or alphabetic characters , and it does not contain special characters , or symbols")
else :
    print("SORRY \""+user_name+"\" , your user password is NOT-OKAY , because your entered user password is : \""+user_password+" , because it contains numeric , alphabetic characters , and it also contains special characters , or symbols")