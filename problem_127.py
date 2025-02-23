# write a python program to get five number from the user , and then store all numbers in tuple , get the sum and multiplication of the all numbers in the tuple , and then display result for the user and also get the length of the tuple of the numbers =>
lista_of_numbers = []
# for i in range(5) :
    # lista_of_numbers . append(int(input("please enter the numbers to store in the list of the numbers is = ")))
lista_of_numbers = [int(input("please enter the numbers to store in the list of the numbers is = ")) for i in range(5)]
print("the list of the numbers is : "+str(lista_of_numbers))
print("the length of the list of the numbers is = "+str(len(lista_of_numbers))+" numbers")
tuples_of_numbers = tuple(lista_of_numbers)
print("the tuple of the numbers is : "+str(tuples_of_numbers))
print("the length of the tuple of the numbers is = "+str(len(tuples_of_numbers))+" numbers")
sum_of_all_numbers_in_tuple = 0
mul_of_all_numbers_in_tuple = 1 
for j in tuples_of_numbers :
    # sum_of_all_numbers_in_tuple += j
    mul_of_all_numbers_in_tuple *= j 
sum_of_all_numbers_in_tuple = sum(tuples_of_numbers)
print("the sum of the all numbers in the tuple of the numbers is = "+str(sum_of_all_numbers_in_tuple))
print("the multiplication of the all numbers in the tuple of the numbers is = "+str(mul_of_all_numbers_in_tuple))