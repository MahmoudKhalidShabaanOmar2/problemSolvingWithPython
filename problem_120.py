# write a python program to get six numbers from the user in list , and then get the square of the frist three numbers , and get cube of the second three numbers by using different function methods =>
# lista_of_numbers = []
# for i in range(6) :
#     num = int(input("please enter the numbers to store in the list of the numbers is = "))
#     lista_of_numbers . append(num)
# def get_square_of_frist_3_num_and_cube_of_second_3_num(list_of_num) :
#     print("the list of the numbers is : "+str(list_of_num))
#     # square_of_frist_three_numbers = [num * num for num in list_of_num[0:3]]
#     # square_of_frist_three_numbers = [num ** 2 for num in list_of_num[0:3]]
#     square_of_frist_three_numbers = [pow(num , 2) for num in list_of_num[:3]]
#     print("the square of the frist three numbers from the list of the six numbers is : "+str(square_of_frist_three_numbers))
#     # cube_of_second_three_numbers = [num * num * num for num in list_of_num[3:7]]
#     # cube_of_second_three_numbers = [num ** 3 for num in list_of_num[3:7]]
#     cube_of_second_three_numbers = [pow(num , 3) for num in list_of_num[3:7]]
#     print("the cube of the second three numbers from the list of the six numbers is : "+str(cube_of_second_three_numbers))
# get_square_of_frist_3_num_and_cube_of_second_3_num(lista_of_numbers)

def get_square_of_frist_3_num_and_cube_of_second_3_num(list_of_num) :
    print("the list of the numbers is : "+str(list_of_num))
    # square_of_frist_three_numbers = [num * num for num in list_of_num[0:3]]
    # square_of_frist_three_numbers = [num ** 2 for num in list_of_num[0:3]]
    square_of_frist_three_numbers = [pow(num , 2) for num in list_of_num[:3]]
    print("the square of the frist three numbers from the list of the six numbers is : "+str(square_of_frist_three_numbers))
    # cube_of_second_three_numbers = [num * num * num for num in list_of_num[3:7]]
    # cube_of_second_three_numbers = [num ** 3 for num in list_of_num[3:7]]
    cube_of_second_three_numbers = [pow(num , 3) for num in list_of_num[3:7]]
    return("the cube of the second three numbers from the list of the six numbers is : "+str(cube_of_second_three_numbers))
lista_of_numbers = []
for i in range(6) :
    num = int(input("please enter the numbers to store in the list of the numbers is = "))
    lista_of_numbers . append(num)
square_and_cube = get_square_of_frist_3_num_and_cube_of_second_3_num(lista_of_numbers)
print(square_and_cube)