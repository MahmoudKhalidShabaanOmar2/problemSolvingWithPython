# write  a python program to get user name , and then check if it is in uppercase , or not , and it if it is not in the uppercase then converted to uppercase by using function method =>
user_name = input("Please Enter The Name Of The User Is : ")
def get_user_name(name) :
    print("The Name Of The User Is : ",name)
    print("Check If The Name Of The User Is In Uppercase , Or Lower Case , And If The User Name Is In Lower Case Then Converted To Uppercase : ")
    if(name.isupper()) :
        print("It Is Okay , Because Your Entered User Name Is In Uppercase , Because Your Entered User Name Is : ",name)
    else :
        print("It Is Not Okay , Because Your Entered User Name Is In Lowercase , Because Your Entered User Name Is : ",name," , And Then The User Name In The Uppercase Is : ",name.upper())
get_user_name(user_name)