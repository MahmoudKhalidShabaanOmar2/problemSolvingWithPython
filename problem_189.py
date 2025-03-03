# write a python program to get the current(NOW) date by using user request =>
from datetime import datetime
date_value = input("please enter the date value is : ")
if((date_value == "Yes") or (date_value == "yes") or (date_value == "YES")) :
    current_NOW_date = datetime . now()
    print("the current(NOW) date is : "+str(current_NOW_date)) 
elif((date_value == "NO") or (date_value == "no") or (date_value == "NO")) :
    print("there is no current(NOW) date")
else :
    print("please enter valid date value to get the current(NOW) date")    