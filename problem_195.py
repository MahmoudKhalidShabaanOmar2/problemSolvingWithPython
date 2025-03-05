# write a python program to make an average calculator =>
# numbers_of_terms = int(input("please enter the numbers of the terms is = "))
# lista_of_numbers = []
# sum_of_all_numbers = 0 
# for j in range(numbers_of_terms) :
#     lista_of_numbers . append(int(input("please enter the numbers to store in the list of the numbers to get the sum of the all numbers , and then get the average of the all numbers is = ")))
# for num in lista_of_numbers :
#     print(num)
#     # sum_of_all_numbers += num 
# sum_of_all_numbers = sum(lista_of_numbers)
# print("the sum of the all numbers in the list of the number is = "+str(sum_of_all_numbers))
# average_of_sum_of_all_numbers = sum_of_all_numbers / numbers_of_terms 
# print("the average of the sum of the all numbers is = "+str(average_of_sum_of_all_numbers))

numbers_of_terms = int(input("please enter the numbers of the terms is = "))
lista_of_numbers = []
sum_of_all_numbers = 0 
if (numbers_of_terms > 0) :
    for i in range(numbers_of_terms) :
        lista_of_numbers . append(int(input("please enter the numbers to store in the list of the number to get the sum of the all numbers , and then get the average of the all numbers is = ")))
    for num in lista_of_numbers :
        print(num)
        sum_of_all_numbers += num 
    print("the sum of the all numbers in the list of the numbers is = "+str(sum_of_all_numbers))
    if(sum_of_all_numbers > 0) :
        average_of_sum_of_all_numbers = sum_of_all_numbers / numbers_of_terms 
        print("the average of the sum of the all numbers is = "+str(average_of_sum_of_all_numbers))
    else :
        print("there is no average because the sum of the all numbers is a zero , or negative number")
else :
    print("please enter valid numbers of terms to get the average of the sum of the all numbers")