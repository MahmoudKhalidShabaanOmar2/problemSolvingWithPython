# write a python program to make average calculator by using different functions methods =>
# number_of_terms = int(input("please enter the numbers of the terms is = "))
# lista_of_numbers = []
# sum_of_all_numbers = 0 
# def make_average_calculator(num_of_terms , list_of_num , sum_of_num) :
#     for i in range(num_of_terms) :
#         list_of_num . append(int(input("please enter the all numbers to store in the list of the numbers is = ")))
#     for num in list_of_num : 
#         print(num)
#         sum_of_num += num 
#     print("the sum of the all numbers is = "+str(sum_of_num))
#     average_of_sum_of_num = sum_of_num / num_of_terms 
#     print("the average of the sum of the all numbers is = "+str(average_of_sum_of_num))
# make_average_calculator(number_of_terms , lista_of_numbers , sum_of_all_numbers)

# def make_average_calculator(num_of_terms , list_of_num , sum_of_num) :
#     for num in list_of_num :
#         print(num)
#         sum_of_num += num 
#     print("the sum of the all numbers is = "+str(sum_of_num))
#     average_of_sum_of_num = sum_of_num / num_of_terms 
#     return("the average of the sum of the all numbers is = "+str(average_of_sum_of_num))
# numbers_of_terms = int(input("please enter the numbers of the terms is = "))
# lista_of_numbers = []
# sum_of_all_numbers = 0
# for i in range(5) :
#     lista_of_numbers . append(int(input("please enter the all numbers to store in the list of the numbers is = ")))
# average = make_average_calculator(numbers_of_terms , lista_of_numbers , sum_of_all_numbers)
# print(average)

# def make_average_calculator(num_of_terms , list_of_num , sum_of_num) :
#     if(num_of_terms > 0) :
#         for num in list_of_num :
#             print(num)
#             sum_of_num += num 
#         print("the sum of the all numbers is = "+str(sum_of_num))
#         if(sum_of_num > 0) :
#             average_of_sum_of_num = sum_of_num / num_of_terms 
#             return("the average of the sum of the all numbers is = "+str(average_of_sum_of_num))
#         else :
#             return("there is no average of this numbers , because the sum of the all number in the list is a zero , or negative number")
#     else :
#         return("please enter a valid numbers of terms to get the sum of the all number from the list of the numbers to make average calculator")
# numbers_of_terms = int(input("please enter the numbers of terms is = "))
# lista_of_numbers = []
# sum_of_all_numbers = 0 
# for i in range(numbers_of_terms) :
#     lista_of_numbers . append(int(input("please enter the numbers to store in the list of the numbers is = ")))
# average = make_average_calculator(numbers_of_terms , lista_of_numbers , sum_of_all_numbers)
# print(average)

numbers_of_terms = int(input("please enter the numbers of the terms is = "))
lista_of_numbers = []
sum_of_all_numbers = 0
def make_average_calculator(list_of_num , num_of_terms , sum_of_num) :
    for i in range(num_of_terms) :
        list_of_num . append(int(input("please enter the all numbers in the list of the numbers to get the sum of the all numbers to get the average of the sum of the all numbers is = ")))
    if(num_of_terms > 0) :
        for num in list_of_num :
            print(num)
            sum_of_num += num 
        print("the sum of the all numbers is = "+str(sum_of_num))
        if(sum_of_num > 0) :
            average_of_sum_of_num = sum_of_num / num_of_terms 
            print("the average of the sum of the all numbers is = "+str(average_of_sum_of_num))
        else :
            print("there is no average of the sum of all of this numbers , because the sum of the all numbers is a zero , or negative number")
    else :
        print("please enter valid number of terms to get the sum of the all numbers to get the average of the all numbers")
make_average_calculator(lista_of_numbers , numbers_of_terms , sum_of_all_numbers)    