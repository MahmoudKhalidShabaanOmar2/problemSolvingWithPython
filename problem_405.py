# write a python program to get user password that contain alpha numeric , and more than eight characters , and less than twenty characters =>
user_name=input("Please Enter The User Name Is : ")
print("The User Name Is : \""+user_name+"\"")
user_password=input("Please Enter The User Password Is : ")
print("The User Password Is : \""+user_password,"\"")
if((user_password.isalnum()) and (8 <= len(user_password) <= 20)):
    print("Hi , And Welcome ",user_name," Your Entered User Password Is Okay")
else:
    print("Sorry ",user_name," Your Entered User Password Is Not Okay , Please Enter A Valid User Password...")