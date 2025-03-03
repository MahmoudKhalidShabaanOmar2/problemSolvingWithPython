# write a python program to get number from the user to get factorial of the number by using factorial() by using different function methods =>
# import math 
# number = int(input("please enter the number is = "))
# def get_factorial_of_number(num) :
#     print("the number is = "+str(num))
#     factorial_of_num = math . factorial(num)
#     print("the factorial of the number is = "+str(factorial_of_num)+" , because your entered number is = "+str(num))
# get_factorial_of_number(number)

# import math 
# def get_factorial_of_number(num) :
#     print("the number is = "+str(num))
#     factorial_of_number = math . factorial(num)
#     return("the factorial of the number is = "+str(factorial_of_number)+" , because your entered number is = "+str(num))
# number = int(input("please enter the number is = "))
# fact_of_num = get_factorial_of_number(number)    
# print(fact_of_num)

# import math 
# number = int(input("please enter the number is = "))
# def get_factorial_of_number(num) :
#     print("the number is = "+str(num))
#     if(num >= 0) :
#         factorial_of_number = math . factorial(num)
#         print("the factorial of the number is = "+str(factorial_of_number)+" , because your entered number is = "+str(num))
#     else :
#         print("please enter valid number to get the factorial of the number , because your entered number is = "+str(num))
# get_factorial_of_number(number)

import math 
def get_factorial_of_number(num) :
    print("the number is = "+str(num))
    if(num >= 0) :
        factorial_of_number = math . factorial(num)
        return("the factorial of the number is = "+str(factorial_of_number)+" , because your entered number is = "+str(num))
    else :
        return("please enter a valid number to get the factorial of the number , because your entered number is = "+str(num))
number = int(input("please enter the number is = "))
fact_of_num = get_factorial_of_number(number)
print(fact_of_num)
