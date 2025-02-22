# write a python program to get six numbers from the user in list , and then get the square of the frist three numbers , and get cube of the second three numbers =>
lista_of_num = []
for i in range(6) :
    num = int(input("please enter the numbers to store in the list of the numbers is = "))
    lista_of_num . append(num)
print("the list of the number is : "+str(lista_of_num))
# square_of_frist_three_numbers = [num * num for num in lista_of_num[0:3]]
# square_of_frist_three_numbers = [pow(num , 2) for num in lista_of_num[0:3]]
square_of_frist_three_numbers = [num ** 2 for num in lista_of_num[:3]]
print("the square of the frist three numbers from the list of the six numbers is : "+str(square_of_frist_three_numbers))
# cube_of_second_three_numbers = [num * num * num for num in lista_of_num[3:7]]
# cube_of_second_three_numbers = [pow(num , 3) for num in lista_of_num[3:7]]
cube_of_second_three_numbers = [num ** 3 for num in lista_of_num[3:7]]
print("the cube of the second three numbers from the list of the six numbers is : "+str(cube_of_second_three_numbers))