# write a python program to get number from the user , and then check wether it is a positive , or negative number by using function methods =>
# number = float(input("please enter the number is = "))
# def check_number(num) :
#     print("the number is = "+str(num))
#     if(num > 0) :
#         print("it is a positive number , because your entered number is = "+str(num))
#     else :
#         print("it is a negative number , because your entered number is = "+str(num))
# check_number(number)

def check_number(num) :
    print("the number is = "+str(num))
    if(num > 0) :
        return("it is a positive number , because your entered number is = "+str(num))
    else :
        return("it is a negative number , because your entered number is = "+str(num))
number = float(input("please enter the number is = "))
check_num = check_number(number)
print(check_num)