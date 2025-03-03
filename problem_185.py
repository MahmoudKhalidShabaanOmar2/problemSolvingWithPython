# write a python program to get number from the user , and then get the factorial of the number by using factorial() function =>
# import math 
# number = int(input("please enter the number is = "))
# print("the number is = "+str(number))
# factorial_of_number = math . factorial(number)
# print("the factorial of the number is = "+str(factorial_of_number)+" , because your entered number is = "+str(number))

import math 
number = int(input("please enter the number is = "))
print("the number is = "+str(number))
if(number >= 0) :
    factorial_of_number = math . factorial(number)
    print("the factorial of the number is = "+str(factorial_of_number)+" , because your entered number is = "+str(number))
else :
    print("there is no factorial of the number , because your entered number is = "+str(number))