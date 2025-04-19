# write a python program to get user name from the user , and then check if the user name is in a lowercase form or not , and if not lowercase form convert into lowercase form => 
user_name = input("Please Enter The Name Of The User Is : ")
print("The Name Of The User Is : "+user_name)
if(user_name.islower()) :
    print("The User Name In The Lowercase")
else :
    print("The User Name In The Uppercase")
    print("The Lowercase Of The User Name Is : "+user_name.lower())