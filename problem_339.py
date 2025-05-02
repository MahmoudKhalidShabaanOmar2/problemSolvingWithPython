# write a python program to get multiplication of even numbers only from the list of numbers =>
lista_of_numbers = []
num_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of Terms Is = ",str(num_of_terms)," Terms")
for i in range(num_of_terms) :
    numbers = int(input(f"Please Enter The Number {i + 1 } Is = "))
    lista_of_numbers.append(numbers)
mul_of_even_numbers = 1
for j in lista_of_numbers :
    if(j %2 == 0) :
        mul_of_even_numbers *= j
print("The List Of All Numbers Is = ",str(lista_of_numbers))
print("The Multiplication Of All Even Numbers From The List Of Numbers Is = ",str(mul_of_even_numbers))