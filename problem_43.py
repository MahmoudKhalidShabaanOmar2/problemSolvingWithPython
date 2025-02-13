# write a python program to get six numbers in the list , and then find the sum of that numbers =>
# lista_of_numbers = []
# for i in range(6) :
    # lista_of_numbers . append(int(input("please enter the numbers to store in the list of the numbers is = ")))
lista_of_numbers = [int(input("please enter the numbers to store in the list of the numbers is = ")) for i in range(6)]
print("the list of the numbers is = "+str(lista_of_numbers))
print("the length of the list of the numbers is = "+str(len(lista_of_numbers))+" numbers")
# sum_of_all_numbers = 0 
# for j in lista_of_numbers :
    # sum_of_all_numbers += j
sum_of_all_numbers = sum(lista_of_numbers) 
print("the sum of the all numbers in the list is = "+str(sum_of_all_numbers))