# write a python program to get five number from the user , and then store all numbers in tuple , get the sum and multiplication of the all numbers in the tuple , and then display result for the user and also get the length of the tuple of the numbers by using different functions methods =>
# lista_of_numbers = []
# for i in range(5) :
#     lista_of_numbers . append(int(input("please enter the numbers to store in the list of the numbers is = ")))
# print("the list of the numbers is : "+str(lista_of_numbers))
# print("the length of the list of the numbers is = ")
# tuples_of_numbers = tuple(lista_of_numbers)
# def get_sum_mul_of_all_numbers_in_tuple(tup_of_num) :
#     print("the tuple of the numbers is : "+str(tup_of_num))
#     print("the length of the tuple of the numbers is = "+str(len(tup_of_num))+" numbers")
#     sum_of_all_numbers_in_tuple = 0 
#     mul_of_all_numbers_in_tuple = 1 
#     for j in tup_of_num : 
#         sum_of_all_numbers_in_tuple += j 
#         mul_of_all_numbers_in_tuple *= j
#     print("the sum of the all numbers in the tuple of the numbers is = "+str(sum_of_all_numbers_in_tuple))
#     print("the multiplication of the all numbers in the tuple of the numbers is = "+str(mul_of_all_numbers_in_tuple))
# get_sum_mul_of_all_numbers_in_tuple(tuples_of_numbers)

def get_sum_mul_of_all_numbers_in_tuple(tup_of_num , list_of_num) :
    print("the list of the numbers is : "+str(list_of_num))
    print("the length of the list of the numbers is = "+str(len(list_of_num))+" numbers")
    print("the tuple of the numbers is : "+str(tup_of_num))
    print("the length of the tuple of the numbers is = "+str(len(tup_of_num))+" numbers")
    sum_of_all_numbers_in_tuple = 0 
    mul_of_all_numbers_in_tuple = 1 
    for j in tup_of_num :
        # sum_of_all_numbers_in_tuple += j
        mul_of_all_numbers_in_tuple *= j
    sum_of_all_numbers_in_tuple = sum(tup_of_num)
    return("the sum of the all numbers in the tuple of the numbers is = "+str(sum_of_all_numbers_in_tuple)+" , and the multiplication of the all numbers in the tuple of the numbers is = "+str(mul_of_all_numbers_in_tuple))
lista_of_numbers = []
# for i in range(5) :
    # lista_of_numbers . append(int(input("please enter the numbers to store in the tuple of the numbers is = ")))
lista_of_numbers = [int(input("please enter the numbers to store in the list of the numbers is = ")) for i in range(5)]
tuples_of_numbers = tuple(lista_of_numbers) 
sum_mul = get_sum_mul_of_all_numbers_in_tuple(tuples_of_numbers , lista_of_numbers)
print(sum_mul)