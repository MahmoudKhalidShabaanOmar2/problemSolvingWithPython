# write a python program to get numbers of hours from the user , and then converted to seconds by using different function methods =>
# num_of_hours = float(input("please enter the number of the hours is = "))
# def get_num_of_seconds(hours) :
#     print("the number of the hours is = "+str(hours)+" hours")
#     num_of_seconds = hours * 60 * 60  
#     print("the number of the seconds is = "+str(num_of_seconds)+" seconds , because your entered numbers of hours is = "+str(num_of_hours)+" hours")
# get_num_of_seconds(num_of_hours)

# def get_num_of_seconds(hours) :
#     print("the number of the hours is = "+str(hours)+" hours")
#     num_of_seconds = hours * 60 * 60 
#     return("the number of the seconds is = "+str(num_of_seconds)+" seconds , because your entered numbers of hours is = "+str(hours)+" hours")
# num_of_hours = float(input("please enter the numbers of the hours is = "))
# seconds = get_num_of_seconds(num_of_hours)
# print(seconds)

# num_of_hours = float(input("please enter the number of the hours is = "))
# def get_num_of_seconds(hours) :
#     print("the number of the hours is = "+str(hours)+" hours")
#     if(hours > 0) :
#         num_of_seconds = hours * 60 * 60
#         print("the numbers of the seconds is = "+str(num_of_seconds)+" , because your entered numbers of the hours is = "+str(hours)+" hours")
#     else :
#         print("there is no numbers of the seconds , because your entered numbers of the hours is = "+str(hours)+" hours")
# get_num_of_seconds(num_of_hours)

def get_num_of_seconds(hours) :
    print("the number of the seconds is = "+str(hours)+" hours")
    if(hours > 0) :
        num_of_seconds = hours * 60 * 60 
        return("the numbers of the seconds is = "+str(num_of_seconds)+" seconds , because your entered numbers of the hours is = "+str(hours)+" hours")
    else :
        return("there is no numbers of the seconds , because your entered numbers of the hours is = "+str(hours)+" hours")
num_of_hours = float(input("please enter the numbers of the hours is = "))
seconds = get_num_of_seconds(num_of_hours)
print(seconds)    