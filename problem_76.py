# write a python program to get number from the user , and then check that it is an even , or odd number and then find that number square by using function methods =>
# number = int(input("please enter the number is = "))
# # square_of_number = number * number
# # square_of_number = pow(number , 2)
# square_of_number = number ** 2
# def check_number_if_even_else_odd_and_get_square_of_num(num , square_of_num) :
#     print("the number is = "+str(num))
#     print("the square of the number is = "+str(square_of_num))
#     if(num %2 == 0) :
#         print("it is an even number , because your entered number is = "+str(num)+" , the modulus of the number by two is = "+str(num % 2)+" , and the square of the number is = "+str(square_of_num))
#     else :
#         print("it is an odd number , because your entered number is = "+str(num)+" , the modulus of the number by two is = "+str(num % 2)+" , and the square of the number is = "+str(square_of_num))
# check_number_if_even_else_odd_and_get_square_of_num(number , square_of_number)

def check_number_if_even_else_odd_and_get_square_of_num(num , square_of_num) :
    print("the number is = "+str(num))
    print("the square of the number is = "+str(square_of_num))
    if(num %2 == 0) :
        return("it is an even number , because your entered number is = "+str(num)+" , the modulus of the number by two is = "+str(num % 2)+" , and the square of the number is = "+str(square_of_num))
    else :
        return("it is an odd number , because your entered number is = "+str(num)+" , the modulus of the number by two is = "+str(num % 2)+" , and the square of the number is = "+str(square_of_num))
number = int(input("please enter the number is = "))
# square_of_number = number * number 
# square_of_number = pow(number , 2)
square_of_number = number ** 2
check_num_get_square_of_num = check_number_if_even_else_odd_and_get_square_of_num(number , square_of_number)
print(check_num_get_square_of_num)