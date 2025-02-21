# write a python program to get number from the user , and then get the square of the number by using different functions methods =>
# number = int(input("please enter the number is = "))
# def get_square_of_num(num) :
#     print("the number is = "+str(num))
#     # square_of_num = num * num 
#     # square_of_num = num ** 2
#     square_of_num = pow(num , 2)
#     print("the square of the number is = "+str(square_of_num))
# get_square_of_num(number)

def get_square_of_num(num) :
    print("the number is = "+str(num))
    square_of_num = num * num 
    return("the square of the number is = "+str(square_of_num))
number = int(input("please enter the number is = "))
square = get_square_of_num(number)
print(square)