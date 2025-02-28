# write a python program to get the difference between the two dates into minutes by usind different function methods =>
# from datetime import datetime 
# frist_date = input("please enter the frist date is : ")
# second_date = input("please enter the second date is : ")
# date_formatting = "%m/%d/%Y"
# def get_difference_between_two_dates_into_minutes(f_date , s_date , date_format) :
#     print("the frist date is : \""+f_date+"\"")
#     print("the second date is : \""+s_date+"\"")
#     print("the date format is : \""+date_format+"\"")
#     fri_date = datetime . strptime(f_date , date_format)
#     sec_date = datetime . strptime(s_date , date_format)
#     difference_between_two_dates_into_minutes = (fri_date - sec_date) * 24 * 60 
#     print("the difference between two dates into minutes is : \""+str(difference_between_two_dates_into_minutes)+" minutes\"")
# get_difference_between_two_dates_into_minutes(frist_date , second_date , date_formatting)

from datetime import datetime
def get_difference_between_two_dates_into_minutes(f_date , s_date , date_format) :
    print("the frist date is : \""+f_date+"\"")
    print("the second date is : \""+s_date+"\"")
    print("the date format is : \""+date_format+"\"")
    fri_date = datetime . strptime(f_date , date_format)    
    sec_date = datetime . strptime(s_date , date_format)
    difference_between_two_dates_into_minutes = (fri_date - sec_date) * 24 * 60
    return("the difference between the two dates into minutes is = \""+str(difference_between_two_dates_into_minutes)+" minutes\"")
frist_date = input("please enter the frist date is : ")
second_date = input("please enter the second date is : ")
date_format = "%m/%d/%Y"
difference_between_dates = get_difference_between_two_dates_into_minutes(frist_date , second_date , date_format)
print(difference_between_dates)
