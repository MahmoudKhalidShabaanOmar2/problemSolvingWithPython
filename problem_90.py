# write a python program to get number , and then check that the number is divisible by five , and six by using functions methods =>
# number = int(input("please enter the number is = "))
# def check_number(num) :
#     print("the number is = "+str(num))
#     if((num %5 == 0) and (num %6 == 0)) :
#         print("it is divisible by six , and five , because your entered number is = "+str(num)+" , and the modulus of the number by five is = "+str(num % 5)+" , and the modulus of the number by six is = "+str(num % 6))
#     else :
#         print("it is not divisible by six , or five , because your entered number is = "+str(num)+" , and the modulus of the number by five is = "+str(num % 5)+" , or the modulus of the number by six is = "+str(num % 6))
# check_number(number)

def check_num(num) :
    print("the number is = "+str(num))
    if((num %5 == 0) and (num %6 == 0)) :
        return("it is divisible by five , and six , because your entered number is = "+str(num)+" , and the modulus of the number by five is = "+str(num % 5)+" , and the modulus of the number by six is = "+str(num % 6))
    else :
        return("it is not divisible by five , or six , because your entered number is = "+str(num)+" , and the modulus of the number by five is = "+str(num % 5)+" , or the modulus of the number by six is = "+str(num % 6))
