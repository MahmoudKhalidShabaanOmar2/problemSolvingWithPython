# write a python program to get name from the user , and then check wether that the user name is encrypted , or decrypted form =>
user_name = input("Please Enter The Name Of The User Is : ")
print("The Name Of The User Is : "+user_name)
if(user_name.isalpha()) :
    print("The User Name In Decrypted Form Because Your Entered User Name Is : "+user_name)
else :
    print("The User Name In Encrypted Form Decause Your Entered User Name Is : "+user_name)