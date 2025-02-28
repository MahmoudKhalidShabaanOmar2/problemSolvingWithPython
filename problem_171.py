# write a python program to get the difference between two dates into hours =>
from datetime import datetime 
frist_date = input("please enter the frist date is : ")
second_date = input("please enter the second date is : ")
date_format = "%m/%d/%Y"
print("the frist date is : \""+frist_date+"\"")
print("the second date is : \""+second_date+"\"")
print("the date format is : \""+date_format+"\"")
fri_date = datetime . strptime(frist_date , date_format)
sec_date = datetime . strptime(second_date , date_format)
difference_between_two_dates_into_hours = (fri_date - sec_date) * 24
print("the difference between the two dates into hours is = \""+str(difference_between_two_dates_into_hours)+" hours\"")