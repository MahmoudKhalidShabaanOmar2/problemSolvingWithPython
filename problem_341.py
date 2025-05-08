#   write a python program to get list of numbers , and then get the multiplication of only odd numbers from the list of the numbers =>
lista_of_numbers = []
num_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of The Terms Is = ",str(num_of_terms)," Terms")
for i in range(num_of_terms) :
    numbers = int(input(f"Please Enter The Number {i + 1} Is = "))
    lista_of_numbers.append(numbers)
print("The List Of All Numbers Is : ",str(lista_of_numbers))
mul_of_odd_numbers = 1
for j in lista_of_numbers :
    if(j %2 != 0) :
        mul_of_odd_numbers *= j 
print("The Multiplication Of All Odd Numbers Only From The List Of The Numbers Is = ",str(mul_of_odd_numbers))