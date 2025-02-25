# write a python program to get find two numbers from the user , and then find the square of the two number , and at the end find the sum of the square of the two numbers by using different functions methods  =>
# frist_number = int(input("please enter the frist number is = "))
# second_number = int(input("please enter the second number is = "))
# def get_square_of_numbers(fri_num , sec_num) :
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     addition_of_two_numbers = fri_num + sec_num 
#     print("the addition of the two numbers is = "+str(addition_of_two_numbers))
#     # square_of_fri_num = fri_num * fri_num 
#     # square_of_fri_num = fri_num ** 2
#     square_of_fri_num = pow(fri_num , 2)
#     print("the square of the frist number is = "+str(square_of_fri_num))
#     # square_of_sec_num = sec_num * sec_num 
#     # square_of_sec_num = sec_num ** 2
#     square_of_sec_num = pow(sec_num , 2)
#     print("the square of the second number is = "+str(square_of_sec_num))
#     addition_of_square_of_two_numbers = square_of_fri_num + square_of_sec_num 
#     print("the addition of the square of the two numbers is = "+str(addition_of_square_of_two_numbers))
# get_square_of_numbers(frist_number , second_number)

def get_square_of_numbers(fri_num , sec_num) :
    print("the frist number is = "+str(fri_num))
    print("the second number is = "+str(sec_num))
    addition_of_two_numbers = fri_num + sec_num 
    print("the addition of the two numbers is = "+str(addition_of_two_numbers))
    # square_of_fri_num = fri_num * fri_num 
    # square_of_fri_num = fri_num ** 2
    square_of_fri_num = pow(fri_num , 2)
    print("the square of the frist number is = "+str(square_of_fri_num))
    # square_of_sec_num = sec_num * sec_num 
    # square_of_sec_num = sec_num ** 2 
    square_of_sec_num = pow(sec_num , 2)
    print("the square of the second number is = "+str(square_of_sec_num))
    addition_of_square_of_numbers = square_of_fri_num + square_of_sec_num 
    return("the addition of the square of the two numbers is = "+str(addition_of_square_of_numbers))
frist_number = int(input("please enter the frist number is = "))
second_number = int(input("please enter the second number is = "))
addition_of_squ_of_num = get_square_of_numbers(frist_number , second_number)
print(addition_of_squ_of_num)