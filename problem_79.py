# write a python program to get number from the user , and then get the square of the number =>
# number = int(input("please enter the number is = "))
# print("the number is = "+str(number))
# # square_of_num = number * number 
# # square_of_num = number ** 2
# square_of_num = pow(number , 2)
# print("the square of the number is = "+str(square_of_num))

number = int(input("please enter the number is = "))
print("the number is = "+str(number))
if(number > 0) :
    # square_of_num = number * number 
    # square_of_num = number ** 2
    square_of_num = pow(number , 2)
    print("the square of the number is = "+str(square_of_num))
else :
    print("there is no square of the number , because your entered number is = "+str(number))

    