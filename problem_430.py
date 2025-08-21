# write a python program to get five numbers in a list , and then get the number by power three by using list comprehenssion method =>
lista_of_numbers = []
for num in range(5):
    number = int(input("Please Enter The Number("+str(num+1)+") Is = "))
    lista_of_numbers.append(number)
print("The List Of All Numbers Is = ",str(lista_of_numbers))
cube_of_all_numbers_in_lista_of_numbers = [num * num * num for num in lista_of_numbers]
print(cube_of_all_numbers_in_lista_of_numbers)