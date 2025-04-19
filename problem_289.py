# write a python program to get name from the user , to check it is in uppercase , or not , if not upper then converted to the uppercase =>
user_name = input("Please Enter The Name Of The User Is : ")
print("The Name Of The User Is : \""+user_name+"\"")
if(user_name.isupper()) :
    print("The User Name In The Uppercase")
else :
    print("The User Name In Lowercase")
    print("The User Name In The Uppercase Is : "+user_name.upper())