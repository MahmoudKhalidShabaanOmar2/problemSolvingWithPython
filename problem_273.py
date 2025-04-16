# write a python program to get numbers from user in a list , and then display the list of the numbers , and at the end display only divisible numbers by three by using function methods =>
# lista_of_numbers = []
# number_of_terms = int(input("Please Enter The Number Of Terms Is = "))
# for i in range(number_of_terms) :
#     numbers = int(input("Please Enter All Numbers To Store In The List Of Numbers Is = "))
#     lista_of_numbers . append(numbers)
# def get_list_of_numbers(list_of_num) :
#     print("The List Of All Numbers Is : "+str(list_of_num))
#     for j in list_of_num :
#         print(j)
#     numbers_divisble_by_3_only = [numbers for numbers in list_of_num if(numbers %3 == 0)]
#     print("List Of All Number That Numbers Divisible By Three Only Is : "+str(numbers_divisble_by_3_only))
#     for k in numbers_divisble_by_3_only :
#         print(k)
# get_list_of_numbers(lista_of_numbers)    

def get_list_of_numbers(list_of_num) :
    print("The List Of All Numbers Is : "+str(list_of_num))
    for j in list_of_num :
        print(j)
    numbers_divisible_by_3_only = [numbers for numbers in list_of_num if(numbers %3 == 0)] 
    return("The List Of All Numbers That Numbers Divisible By Three Is : "+str(numbers_divisible_by_3_only))
lista_of_numbers = []
number_of_terms = int(input("Please Enter The Number Of Terms Is = "))
for i in range(number_of_terms) :
    numbers = int(input("Please Enter All Numbers To Store In The List Of The Numbers Is = "))
    lista_of_numbers . append(numbers)
displaying_list_of_numbers = get_list_of_numbers(lista_of_numbers)
print(displaying_list_of_numbers)