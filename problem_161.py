# write a python program to get numbers of seconds from the user , and then converted to numbers of hours by using different functions methods =>
# num_of_seconds = int(input("please enter the number of the seconds is = "))
# def get_num_of_hours(seconds) :
#     print("the number of the seconds is  = "+str(seconds)+" seconds")
#     num_of_hours = num_of_seconds / (60 * 60)
#     print("the numbers of the hours is = "+str(num_of_hours)+" hours , because your entered number of seconds is = "+str(num_of_seconds)+" seconds")
# get_num_of_hours(num_of_seconds)

# def get_num_of_hours(seconds) :
#     print("the number of the seconds is = "+str(seconds)+" seconds")
#     num_of_hours = seconds / (60 * 60)
#     return("the number of the hours is = "+str(num_of_hours)+" , because your entered num of the seconds is = "+str(seconds)+" seconds")
# num_of_seconds = int(input("please enter the number of the seconds is = "))
# hours = get_num_of_hours(num_of_seconds)
# print(hours)

# def get_num_of_hours(seconds) :
#     print("the number of the seconds is = "+str(seconds)+" seconds")
#     if(seconds > 0) :
#         num_of_hours = seconds / (60 * 60)
#         return("the numbers of the hours is = "+str(num_of_hours)+" , because your entered numbers of the seconds is = "+str(seconds)+" seconds")
#     else :
#         return("there is no numbers of the hours , because your entered numbers of the second is = "+str(seconds)+" seconds")
# num_of_seconds = int(input("please enter the number of the seconds is = "))
# hours = get_num_of_hours(num_of_seconds)
# print(hours)

num_of_seconds = int(input("please enter the number of the seconds is = "))
def get_num_of_hours(seconds) :
    print("the number of the seconds is = "+str(seconds)+" seconds")
    num_of_hours = num_of_seconds / (60 * 60)
    if(num_of_seconds > 0) :
        print("the number of the hours is = "+str(num_of_hours)+" hours , because your entered numbers of seconds is = "+str(seconds)+" seconds")
    else :
        print("there is no number of the hours , because your entered numbers of the seconds is = "+str(seconds)+" seconds")
get_num_of_hours(num_of_seconds)