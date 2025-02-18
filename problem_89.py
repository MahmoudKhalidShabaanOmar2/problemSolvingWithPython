# write a python program to get number from the user , and then check it is divisible by two , and three by using function methods =>
# number = int(input("please enter the number is = "))
# def check_number(num) :
#     print("the number is = "+str(num))
#     if((num %2 == 0) and (num %3 == 0)) :
#         print("it is divisible by two , and three , because your entered number is = "+str(num)+" , and the modulus of the number by two is = "+str(num % 2)+" , and the modulus of the number by three is = "+str(num % 3))
#     else :
#         print("it is not divisible by two , or three , because your entered number is = "+str(num)+" , and the modulus of the number by two is = "+str(num % 2)+" , or the modulus of the number by three is = "+str(num % 3))
# check_number(number)

def check_number(num) :
    print("the number is = "+str(num)) 
    if((num %2 == 0) and (num %3 == 0)) :
        return("it is divisible by two , and three , because your entered number is = "+str(num)+" , and the modulus of the number by two is = "+str(num % 2)+" , and the modulus of the number by three is = "+str(num % 3))
    else :
        return("it is not divisible by two , or three , because your entered number is = "+str(num)+", and the modulus of the number by two is = "+str(num % 2)+" , or the modulus of the number by three is = "+str(num % 3))
number = int(input("please enter the number is = "))
check_num = check_number(number)
print(check_num)