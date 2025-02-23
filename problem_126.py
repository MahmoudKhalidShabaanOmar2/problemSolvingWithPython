# write a python program to get five numbers from the user , and then store them in list , and multiply , and add all numbers from the list of the numbers , and then display list for the user , and get the length of the list also by using different functions methods =>
# lista_of_numbers = []
# # for i in range(5) :
#     # lista_of_numbers . append(int(input("please enter the numbers to store in the list of the numbers is = ")))
# lista_of_numbers = [int(input("please enter the numbers to store in the list of the numbers is = ")) for i in range(5)]
# def get_sum_mul_of_all_numbers_in_list(list_of_num) :
#     print("the list of the numbers is : "+str(list_of_num))
#     print("the length of the list of the numbers is = "+str(len(list_of_num)))
#     sum_of_all_numbers_in_list = 0 
#     mul_of_all_numbers_in_list = 1
#     for j in list_of_num :
#         # sum_of_all_numbers_in_list += j 
#         mul_of_all_numbers_in_list *= j 
#     sum_of_all_numbers_in_list = sum(lista_of_numbers)
#     print("the sum of the all numbers in the list of the numbers is = "+str(sum_of_all_numbers_in_list))
#     print("the multiplication of the all numbers in the list of the numbers is = "+str(mul_of_all_numbers_in_list))
# get_sum_mul_of_all_numbers_in_list(lista_of_numbers)

def get_sum_mul_of_all_numbers_in_list(list_of_num) :
    print("the list of the numbers is : "+str(list_of_num))
    print("the length of the list of the numbers is = "+str(len(list_of_num))+" numbers")
    sum_of_all_numbers_in_list = 0 
    mul_of_all_numbers_in_list = 1 
    for j in list_of_num :
        # sum_of_all_numbers_in_list += j 
        mul_of_all_numbers_in_list *= j
    sum_of_all_numbers_in_list = sum(lista_of_numbers)
    return("the sum of the all numbers in list of the numbers is = "+str(sum_of_all_numbers_in_list)+" , and the multiplication of the all numbers in the list of the numbers is = "+str(mul_of_all_numbers_in_list))
lista_of_numbers = []
# for i in range(5) :
    # lista_of_numbers . append(int(input("please enter the numbers to store in the list of the numbers is = ")))
lista_of_numbers = [int(input("please enter the numbers to store in the list of the numbers is = ")) for i in range(5)]
mul_sum = get_sum_mul_of_all_numbers_in_list(lista_of_numbers)
print(mul_sum)