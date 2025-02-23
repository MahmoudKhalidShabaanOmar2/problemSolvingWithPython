# write a python program to get five numbers from the user , and then store them in list , and multiply , and add all numbers from the list of the numbers , and then display list for the user , and get the length of the list also =>
lista_of_numbers = []
# for i in range(5) :
    # lista_of_numbers . append(int(input("please enter the numbers to store in the list of the numbers is = ")))
lista_of_numbers = [int(input("please enter the numbers to store in the list of the numbers is = ")) for i in range(5)]
print("the list of the numbers is : "+str(lista_of_numbers))
print("the length of the list of the numbers is = "+str(len(lista_of_numbers))+" numbers")
sum_of_all_numbers_in_list = 0 
mul_of_all_numbers_in_list = 1 
for j in lista_of_numbers :
    # sum_of_all_numbers_in_list += j
    mul_of_all_numbers_in_list *= j 
sum_of_all_numbers_in_list = sum(lista_of_numbers)
print("the sum of the all numbers in the list of the numbers is = "+str(sum_of_all_numbers_in_list))
print("the multiplication of the all numbers in the list of the numbers is = "+str(mul_of_all_numbers_in_list))