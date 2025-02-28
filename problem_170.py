# write a python program to get the difference between two dates into days by using functions methods =>
# from datetime import datetime 
# frist_date = input("please enter the frist date is : ")
# second_date = input("please enter the second date is : ")
# date_formatting = "%m/%d/%Y"
# def get_difference_between_dates_into_days(f_date , s_date , date_format) :
#     print("the frist date is : \""+f_date+"\"")
#     print("the second date is : \""+s_date+"\"")
#     print("the date format is : \""+date_format+"\"")
#     fri_date = datetime . strptime(f_date , date_formatting)
#     sec_date = datetime . strptime(s_date , date_formatting)
#     difference_between_two_dates = fri_date - sec_date
#     print("the difference between the two dates is : \""+str(difference_between_two_dates)+"\"")
# get_difference_between_dates_into_days(frist_date , second_date , date_formatting)

from datetime import datetime 
def get_difference_between_dates_into_days(f_date , s_date , date_format) :
    print("the frist date is : \""+f_date+"\"")
    print("the second date is : \""+s_date+"\"")
    print("the date format is : \""+date_format+"\"")
    fri_date = datetime . strptime(f_date , date_format)
    sec_date = datetime . strptime(s_date , date_format)
    difference_between_two_dates_into_days = fri_date - sec_date
    return("the difference between two dates into days is : \""+str(difference_between_two_dates_into_days)+"\"")
frist_date = input("please enter the frist date is : ")
second_date = input("please enter the second date is : ")
date_formatting = "%m/%d/%Y"
difference_between_dates = get_difference_between_dates_into_days(frist_date , second_date , date_formatting)
print(difference_between_dates)