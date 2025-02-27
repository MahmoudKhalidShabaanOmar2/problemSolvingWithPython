# write a python program to get hours and then converted to seconds =>
# num_of_hours = float(input("please enter the numbers of the hours is = "))
# print("the numbers of the hours is = "+str(num_of_hours)+" hours")
# num_of_seconds = num_of_hours * 60 * 60 
# print("the numbers of the seconds is = "+str(num_of_seconds)+" seconds")

num_of_hours = float(input("please enter the numbers of the hours is = "))
print("the numbers of the hours is = "+str(num_of_hours)+" hours")
if(num_of_hours > 0) :
    num_of_seconds = num_of_hours * 60 * 60 
    print("the numbers of the hours is = "+str(num_of_seconds)+" seconds , because your entered number of hours is = "+str(num_of_hours)+" hours")
else :
    print("there is no number of the seconds because your entered number of the hours is = "+str(num_of_hours)+" hours")