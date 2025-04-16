# write a python program to get numbers from the user , and then store in the list of the numbers , then display the list of all numbers , and at the end display only numbers that divisible by three , and five by using function method =>
# lista_of_numbers = []
# number_of_terms = int(input("Please Enter The Number Of Terms Is = "))
# for i in range(number_of_terms) :
#     numbers = int(input("Please Enter The Numbers Of Terms Is = "))
#     lista_of_numbers.append(numbers)
# def get_list_of_numbers(list_of_num) :
#     print("The List Of The Numbers Is : "+str(list_of_num))
#     for j in list_of_num :
#         print(j)
#     numbers_divisible_by_3_5 = [numbers for numbers in list_of_num if((numbers %3 == 0) and (numbers %5 == 0))]
#     print("The List Of All Numbers That Numbers Divisible By Three , And Five Only Is : "+str(numbers_divisible_by_3_5))
#     for k in numbers_divisible_by_3_5 :
#         print(k)
# get_list_of_numbers(lista_of_numbers)

def get_list_of_numbers(list_of_num) :
    print("The List Of All Numbers Is : "+str(list_of_num))
    for j in list_of_num :
        print(j)
    numbers_divisible_by_3_5 = [numbers for numbers in list_of_num if((numbers %3 == 0) and (numbers %5 == 0))]
    return("The List Of All Numbers That All Numbers Divisible By Three , And Five Only Is : "+str(numbers_divisible_by_3_5))
lista_of_numbers = []    
numbers_of_terms = int(input("Please Enter The Number Of Terms Is = "))
for i in range(numbers_of_terms) :
    numbers = int(input("Please Enter All Numbers To Store In The List Of The Numbers Is = "))
    lista_of_numbers.append(numbers)
displaying_list_of_all_numbers = get_list_of_numbers(lista_of_numbers)
print(displaying_list_of_all_numbers)