# write a python program to get the user name , and then check if the user name is in lower case , and if the user name is in uppercase then converted to lower case by using function method =>
user_name = input("Please Enter The User Name Is : ")
def get_user_name(name) :
    print("The User Name Is : ",name)
    if(name.islower()) :
        print("It Is Okay , Because The User Name Is In Lowercase , Because Your Entered User Name Is : ",name)
    else :
        print("It Is Not Okay , Because The User Name Is In Upper Case , Because Your Entered User Name Is : ",name," , And Then The User Name In Lower Case Is : ",name.lower())
get_user_name(user_name)