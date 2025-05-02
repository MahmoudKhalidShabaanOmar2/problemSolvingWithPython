# write a python program to add even numbers from the list of numbers =>
lista_of_numbers = []
num_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of Terms Is = ",str(num_of_terms))
for i in range(num_of_terms) :
    numbers = int(input(f"Please Enter The Number {i + 1} Is = "))
    lista_of_numbers.append(numbers)
sum_of_even_numbers = 0 
for j in lista_of_numbers :
    if(j %2 == 0) :
        sum_of_even_numbers += j
print("The List Of All Numbers Is : "+str(lista_of_numbers))
print("The Sum Of The Even Number Only From The List Of Numbers Is = ",str(sum_of_even_numbers))