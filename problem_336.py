# write a python program to add number from list that are grater than 5 , and less than 10 =>
lista_of_numbers = []
num_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of Terms Is = ",str(num_of_terms)," Terms")
sum_of_numbers = 0
for i in range(num_of_terms) :
    numbers = int(input(f"Please Enter The Number {i + 1} Is = "))
    lista_of_numbers.append(numbers)
print("The List Of All Numbers Is : ",str(lista_of_numbers))
for j in lista_of_numbers :
    if((j > 5) and (j < 10)) :
        sum_of_numbers += j 
print("The Sum Of All Numbers That Grater Than 5 , And Less Than 10 From The List Of Numbers Is = ",str(sum_of_numbers))