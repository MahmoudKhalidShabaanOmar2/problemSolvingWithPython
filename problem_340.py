# write a python program to add odd numbers only from the list of the numbers =>
lista_of_numbers = []
num_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of Terms Is = ",str(num_of_terms)," Terms")
for i in range(num_of_terms) :
    numbers = int(input(f"Please Enter The Number {i + 1} Is = "))
    lista_of_numbers.append(numbers)
print("The List Of The Numbers Is : "+str(lista_of_numbers))
sum_of_odd_numbers = 0 
for j in lista_of_numbers : 
    if(j %2 != 0) :
        sum_of_odd_numbers += j 
print("The Sum Of All Odd Numbers From The List Of The Numbers Is = ",str(sum_of_odd_numbers))