# write a python program to get two numbers from the user , and then find the cube of the two numbers , and then find the sum of the cube of the two numbers by using different functions methods =>
# frist_number = int(input("please enter the frist number is = "))
# second_number = int(input("please enter the second number is = "))
# def get_cube_of_numbers(fri_num , sec_num) :
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     addition_of_numbers = fri_num + sec_num 
#     print("the addition of the two numbers is = "+str(addition_of_numbers))
#     # cube_of_fri_num = fri_num * fri_num * fri_num 
#     # cube_of_fri_num = fri_num ** 3
#     cube_of_fri_num = pow(fri_num , 3)
#     print("the cube of the frist number is = "+str(cube_of_fri_num))
#     # cube_of_sec_num = sec_num * sec_num * sec_num 
#     # cube_of_sec_num = sec_num ** 3
#     cube_of_sec_num = pow(sec_num , 3)
#     print("the cube of the second number is = "+str(cube_of_sec_num))
#     addition_of_cube_of_numbers = cube_of_fri_num + cube_of_sec_num 
#     print("the addition of the cube of the two numbers is = "+str(addition_of_cube_of_numbers))
# get_cube_of_numbers(frist_number , second_number)

def get_cube_of_numbers(fri_num , sec_num) :
    print("the frist number is = "+str(fri_num))
    print("the second number is = "+str(sec_num))
    addition_of_two_numbers = fri_num + sec_num 
    print("the addition of the two numbers is = "+str(addition_of_two_numbers))
    # cube_of_fri_num = fri_num * fri_num * fri_num 
    # cube_of_fri_num = fri_num ** 3
    cube_of_fri_num = pow(fri_num , 3)
    print("the cube of the frist number is = "+str(cube_of_fri_num))
    # cube_of_sec_num = sec_num * sec_num * sec_num 
    # cube_of_sec_num = sec_num ** 3
    cube_of_sec_num = pow(sec_num , 3)
    print("the cube of the second number is = "+str(cube_of_sec_num))
    addition_of_cube_of_numbers = cube_of_fri_num + cube_of_sec_num 
    return("the addition of the cube of the two numbers is = "+str(addition_of_cube_of_numbers))
frist_number = int(input("please enter the frist number is = "))
second_number = int(input("please enter the second number is = "))
addition_of_cube_of_num = get_cube_of_numbers(frist_number , second_number)
print(addition_of_cube_of_num)