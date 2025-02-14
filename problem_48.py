# write a python program that performs all compound assignment operations on an integer by using function methods =>
number = int(input("please enter the number is = "))
def get_all_compound_assignment_operations(num) :
    print("the number is = "+str(num))
    num += 10
    print("the result of the addition compound assignment operation is = "+str(num))
    num -= 10
    print("the result of the subtraction compound assignment operation is = "+str(num))
    num *= 10
    print("the result of the multplication compound assignment operation is = "+str(num))
    num /= 10 
    print("the result of the division compound assignment operation is = "+str(num))
    num %= 10
    print("the result of the modulus compound assignment operation is = "+str(num))
    num **= 10
    print("the result of the square compound assignment operation is = "+str(num))
get_all_compound_assignment_operations(number)