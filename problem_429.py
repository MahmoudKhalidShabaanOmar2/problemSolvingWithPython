# write a python program to get five numbers , and then store them in list of numbers , and at the end get the square of all numbers =>
lista_of_numbers = []
for num in range(5):
    numbers = int(input(f"Please Enter The Number("+str(num+1)+") Is = "))
    lista_of_numbers.append(numbers)
print("The List Of All Numbers Is : ",str(lista_of_numbers))
for j in lista_of_numbers:
    print(j)
print("The List Of The Square Of All Numbers Is : ")
for n in lista_of_numbers:
    print(n * n)