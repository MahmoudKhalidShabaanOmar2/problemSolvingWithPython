# write a python program to get the difference between the two dates into hours by using different function methods =>
# from datetime import datetime 
# frist_date = input("please enter the frist date is : ")
# second_date = input("please enter the second date is : ")
# date_formatting = "%m/%d/%Y"
# def get_difference_between_two_dates_into_hours(f_date , s_date , date_format) :
#     print("the frist date is : \""+f_date+"\"")
#     print("the second date is : \""+s_date+"\"")
#     print("the date format is : \""+date_format+"\"")
#     fri_date = datetime . strptime(f_date , date_format)
#     sec_date = datetime . strptime(s_date , date_format)
#     difference_between_two_dates_into_hours = (fri_date - sec_date) * 24
#     print("the difference between the two dates into hours is = \""+str(difference_between_two_dates_into_hours)+" hours\"")
# get_difference_between_two_dates_into_hours(frist_date , second_date , date_formatting)

from datetime import datetime 
def get_difference_between_two_dates_into_hours(f_date , s_date , date_format) :
    print("the frist date is : \""+f_date+"\"")
    print("the second date is : \""+s_date+"\"")
    print("the date format is : \""+date_format+"\"")
    fri_date = datetime . strptime(f_date , date_format)
    sec_date = datetime . strptime(s_date , date_format)
    difference_between_two_dates_into_hours = (fri_date - sec_date) * 24
    return("the difference between the two dates into hours is = \""+str(difference_between_two_dates_into_hours)+" hours\"")
frist_date = input("please enter the frist date is : ")
second_date = input("please enter the second date is : ")
date_formatting = "%m/%d/%Y"
difference_dates = get_difference_between_two_dates_into_hours(frist_date , second_date , date_formatting)
print(difference_dates)