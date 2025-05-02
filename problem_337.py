# write a python program to multiplication numbers from the list of the numbers That Number Grater Than 5 , and less than 10=>
lista_of_numbers = []
num_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of Terms Is = ",str(num_of_terms)," Terms")
for i in range(num_of_terms) :
    numbers = int(input(f"Please Enter The Number {i + 1} Is = "))
    lista_of_numbers.append(numbers)
mul_of_numbers = 1 
for j in lista_of_numbers :
    if((j > 5) and (j < 10)) :
        mul_of_numbers *= j
print("The List Of All Numbers Is : "+str(lista_of_numbers))
print("The Multiplication Of All Numbers Than Number Grater Than 5 , And Less Than 10 From The List Of Numbers Is = ",str(mul_of_numbers))