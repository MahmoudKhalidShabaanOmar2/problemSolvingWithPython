# write a python program to get ten numbers from user in a list , and then get the sum , and product of all numbers from the list of the numbers by using function methods =>
# lista_of_numbers = []
# for i in range(10) :
#     numbers = int(input("Please Enter Numbers To Store In The List Of The Numbers Is = "))
#     lista_of_numbers.append(numbers)
# def get_list_of_numbers(list_of_num) :
#     print("The List Of All Numbers Is = "+str(list_of_num))
#     sum_of_all_numbers = 0 
#     mul_of_all_numbers = 1
#     for j in list_of_num :
#         print(j)
#         # sum_of_all_numbers += j 
#         mul_of_all_numbers *= j
#     sum_of_all_numbers = sum(list_of_num)
#     print("The Sum Of All Numbers From The List Of All Numbers Is = ",str(sum_of_all_numbers))
#     print("The Multiplication Of All Numbers From The List Of All Numbers Is = ",str(mul_of_all_numbers))
# get_list_of_numbers(lista_of_numbers)
def get_list_of_numbers(list_of_num) :
    print("The List Of All Numbers Is : "+str(list_of_num))
    sum_of_all_numbers = 0 
    mul_of_all_numbers = 1 
    for j in list_of_num :
        print(j)
        sum_of_all_numbers += j 
        mul_of_all_numbers *= j
    return("The Sum Of All Numbers Is = "+str(sum_of_all_numbers)," , And The Multiplication Of All Numbers Is = "+str(mul_of_all_numbers))
lista_of_numbers = []
for i in range(10) :
    numbers = int(input("Please Enter All Numbers To Store In The List Of The Numbers Is = "))
    lista_of_numbers.append(numbers)
displaying_list_of_all_numbers = get_list_of_numbers(lista_of_numbers)
print(displaying_list_of_all_numbers)