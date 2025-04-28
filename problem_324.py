# write a python program to get ten float data types from the user in a list , and then the system should convert all float data types with integer data types => 
lista_of_float_numbers = []
for i in range(5) :
    float_num = float(input(f"Please Enter The Float Number {i + 1} To Store In The List Of The Numbers Is = "))
    lista_of_float_numbers.append(float_num)
print("The List Of The Float Numbers Is : "+str(lista_of_float_numbers))
for j in lista_of_float_numbers :
    print(j)
lista_of_integer_numbers = [int(num) for num in lista_of_float_numbers]
print("The List Of The Integer Numbers Is : "+str(lista_of_integer_numbers))
for k in lista_of_integer_numbers : 
    print(k)