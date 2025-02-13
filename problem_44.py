# write a python program to get six numbers in tuple , and find the sum of the all numbers =>
# lista_of_numbers = []
# for i in range(6) :
    # lista_of_numbers . append(int(input("please enter the numbers to store in the list of the numbers is = ")))
lista_of_numbers = [int(input("please enter the numbers to store in the list of the numbers is = ")) for i in range(6)]
print("the list of the numbers is = "+str(lista_of_numbers))
print("the length of the list of the numbers is = "+str(len(lista_of_numbers))+" numbers")
# sum_of_all_numbers_in_list = 0
# for j in lista_of_numbers :
    # sum_of_all_numbers_in_list += j 
sum_of_all_numbers_in_list = sum(lista_of_numbers)
print("the sum of the all numbers in the list is = "+str(sum_of_all_numbers_in_list))
tuple_of_numbers = tuple(lista_of_numbers) 
print("the tuple of the numbers is = "+str(tuple_of_numbers))
print("the length of the tuple of the numbers is = "+str(len(tuple_of_numbers))+" numbers")
# sum_of_all_numbers_in_tuple = 0
# for k in tuple_of_numbers :
    # sum_of_all_numbers_in_tuple += k
sum_of_all_numbers_in_tuple = sum(tuple_of_numbers)
print("the sum of the all numbers in the tuple is = "+str(sum_of_all_numbers_in_tuple))