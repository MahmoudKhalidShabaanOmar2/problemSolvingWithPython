# write a python to get five numbers from the users , and then store in the list , and at the end getting the cube of this number =>
lista_of_numbers = []
for num in range(5) :
    numbers = int(input(f"Please Enter The Number("+str(num+1)+") Is = "))
    lista_of_numbers.append(numbers)
print("The List Of The Numbers Is = ",str(lista_of_numbers))
for list_num in lista_of_numbers :
    print(list_num)
print("The Cube Of All List Numbers Is : ")
for j in lista_of_numbers : 
    print(j * j * j)