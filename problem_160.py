# write a python program to get numbers of seconds from the user , and then converted to hours =>
# num_of_seconds = int(input("please enter the numbers of the seconds is = "))
# print("the numbers of the seconds is = "+str(num_of_seconds)+" seconds")
# num_of_hours = num_of_seconds / (60 * 60)
# print("the numbers of the hours is = "+str(num_of_hours)+" hours , because your entered numbers of the seconds is = "+str(num_of_seconds)+" seconds")

num_of_seconds = int(input("please enter the number of the seconds is = "))
print("the numbers of the seconds is = "+str(num_of_seconds)+" seconds")
if(num_of_seconds > 0) :
    num_of_hours = num_of_seconds / (60 * 60)
    print("the number of the hours is = "+str(num_of_hours)+" hours , because your entered numbers of the seconds is = "+str(num_of_seconds)+" seconds")
else :
    print("there is no numbers of the hours because your entered numbers of the seconds is = "+str(num_of_seconds)+" seconds")