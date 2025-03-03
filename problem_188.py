# write a python program to get number from the user , and then get the factorial of the number without using factorial() function by using different functions methods =>
# number = int(input("please enter the number is = "))
# def get_factorial_of_number(num) :
#     print("the number is = "+str(num))
#     factorial_of_number = 1 
#     for i in range(1 , num + 1) :
#         factorial_of_number *= i 
#     print("the factorial of the number is = "+str(factorial_of_number))
# get_factorial_of_number(number)

# def get_factorial_of_number(num) :
#     print("the number is = "+str(num))
#     factorial_of_number = 1
#     for i in range(1 , num + 1) :
#         factorial_of_number *= i 
#     return("the factorial of the number is = "+str(factorial_of_number))
# number = int(input("please enter the number is = "))
# fact_of_num = get_factorial_of_number(number)
# print(fact_of_num)

# number = int(input("please enter the number is = "))
# def get_factorial_of_number(num) :
#     print("the number is = "+str(num))
#     num = number 
#     factorial_of_number = 1 
#     while num > 0 :
#         factorial_of_number *= num 
#         num -= 1 
#     print("the factorial of the number is = "+str(factorial_of_number))
# get_factorial_of_number(number)

def get_factorial_of_number(num) :
    print("the number is = "+str(num))
    factorial_of_number = 1 
    num = number 
    while(num > 0) :
        factorial_of_number *= num 
        num -= 1 
    return("the factorial of the number is = "+str(factorial_of_number))
number = int(input("please enter the number is = "))
fact_of_num = get_factorial_of_number(number)
print(fact_of_num)