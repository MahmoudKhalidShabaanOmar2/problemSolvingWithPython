# write a python program to get ten numbers from the user in a list , find their sum , and products , then add both result to display for the user =>
# lista_of_numbers = []
# for i in range(10) :
    # numbers = int(input("Please Enter The Numbers To Store In The List Of The Numbers Is = "))
    # lista_of_numbers.append(numbers)
lista_of_numbers = [int(input("Please Enter All Numbers To Store In The List Of The Numbers Is = ")) for i in range(10)]
print("The List Of The Numbers Is = ",str(lista_of_numbers))
# sum_of_numbers = 0 
sum_of_numbers = sum(lista_of_numbers)
pro_of_numbers = 1 
for num in lista_of_numbers : 
    # sum_of_numbers += num 
    pro_of_numbers *= num 
print("The Sum Of All Numbers In The List Of The Numbers Is = "+str(sum_of_numbers))
print("The Product Of All Numbers In The List Of The Numbers Is = "+str(pro_of_numbers))
final_results = sum_of_numbers + pro_of_numbers 
print("The Sum Of The Sum Of Numbers , And The Multiplication Of Numbers Is = "+str(final_results))