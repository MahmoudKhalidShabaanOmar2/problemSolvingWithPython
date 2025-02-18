# write a python program to get number from the user , and then check that it is an even , or odd number by using function methods =>
# number = int(input("please enter the number is = "))
# def check_number_if_even_else_odd(num) :
#     print("the number is = "+str(num))
#     if(num % 2 == 0) :
#         print("it is an even number , because your entered number is = "+str(num)+" , the modulus of the number by two is = "+str(num % 2))
#     else :
#         print("it is an odd number , because your entered number is = "+str(num)+" , the modulus of the number by two is = "+str(num % 2))
# check_number_if_even_else_odd(number)

def check_number_if_even_else_odd(num) :
    print("the number is = "+str(num))
    if(num %2 == 0) :
        return ("it is an even number , because your entered number is = "+str(num)+" , the modulus of the number by two is = "+str(num % 2))
    else :
        return ("it is an odd number , because your entered number is = "+str(num)+" , the modulus of the number by two is = "+str(num % 2))
number = int(input("please enter the number is = "))
check_number = check_number_if_even_else_odd(number)
print(check_number)