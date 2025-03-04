# write a python program to get the current(NOW) date by using user request by using different function methods =>
# from datetime import datetime 
# date_value = input("please enter the value of the date is : ")
# def get_currentNOW_date(d_val) :
#     print("the date value is : "+d_val) 
#     if((d_val == "Yes") or (d_val == "yes") or (d_val == "YES")) :
#         currentNOWDate = datetime . now()
#         print("the current (NOW) date is : "+str(currentNOWDate))
#     elif((d_val == "No") or (d_val == "no") or (d_val == "NO")) :
#         print("there is no current (NOW) date")
#     else :
#         print("please enter valid date value to get current (NOW) date")
# get_currentNOW_date(date_value)

from datetime import datetime 
def get_currentNOW_date(d_val) :
    print("the date value is : "+d_val)
    if((d_val == "Yes") or (d_val == "yes") or (d_val == "YES")) :
        currentNow_date = datetime . now()
        return ("the current (NOW) Date Is : "+str(currentNow_date))
    elif((d_val == "No") or (d_val == "no") or (d_val == "NO")) :
        return("there is no current (NOW) date")
    else :
        return ("please enter valid date value to get the current (NOW) date")
date_value = input("please enter the value of the date is : ")
currentNowDate = get_currentNOW_date(date_value)
print(currentNowDate)