# write a python program to get the user password that contain alphanumeric character , and more than eight characters , and less than twenty characters by using function method =>
# user_name = input("Please Enter The User Name Is : ")
# user_password = input("Please Enter The User Password Is : ")
# def check_user_password(u_name , u_pass):
#     print("The User Name Is : ",u_name)
#     print("The User Password Is : ",u_pass)
#     if((u_pass.isalnum()) and (8 <= len(u_pass) <= 20)) :
#         print("Hi , And Welcome ",u_name," Your Entered User Password Is Okay")
#     else:
#         print("Sorry ",u_name," Your Entered User Password Is Not Okay")
# check_user_password(user_name , user_password)

def check_user_password(u_name , u_pass):
    print("The User Name Is : ",u_name)
    print("The User Password Is : ",u_pass)
    if((u_pass.isalnum()) and (8 <= len(u_pass) <= 20)) :
        return("Hi , And Welome "+u_name+" Your Entered User Password Is Okay")
    else:
        return("Sorry "+u_name+" Your Entered User Password Is Not Okay")
user_name=input("Please Enter The User Name Is : ")
user_password=input("Please Enter The User Password Is : ")
check_user_pass=check_user_password(user_name , user_password)
print(check_user_pass)