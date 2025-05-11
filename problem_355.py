# write a python program to get name from the user , and then wether check that the name is encrypted , or decrypted name by using function =>
user_name = input("Please Enter The Name Of The User Is : ")
def check_user_name(name) :
    print("The Name Of The User Is : ",name)
    if(name.isalpha()) :
        print("The User Name Is Decrypted , Because Your Entered User Name Is : ",name)
    else :
        print("The User Name Is Encrypted , Because Your Entered User Name Is : ",name)
check_user_name(user_name)