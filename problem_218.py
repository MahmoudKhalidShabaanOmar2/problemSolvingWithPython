# write a python program to find the minimum number between the numbers in the list of the different numbers by using function methods =>
# lista_of_numbers = []
# num_of_terms = int(input("please enter the numbers of the terms is = "))
# def get_minimum_number(list_of_num , terms) :
#     for i in range(terms) :
#         num = int(input("please enter the different numbers to store in the list of the different numbers is = "))
#         list_of_num . append(num)
#     print("the list of the different numbers is = "+str(list_of_num))
#     minimum_num_between_list_numbers = min(list_of_num)
#     print("the minimum number between the different numbers in the list of the numbers is = "+str(minimum_num_between_list_numbers))
# get_minimum_number(lista_of_numbers , num_of_terms)

def get_minimum_number(list_of_num , terms) :
    for i in range(5) :
        num = int(input("please enter the different numbers to store in the list of the different numbers is = "))
        list_of_num . append(num)
    print("the list of the different numbers is = "+str(list_of_num))
    minimum_num_between_list_numbers = min(list_of_num)
    return("the minimum number between the different numbers in the list of the numbers is = "+str(minimum_num_between_list_numbers))
lista_of_numbers = []
num_of_terms = int(input("please enter the numbers of the terms is = "))
min_num = get_minimum_number(lista_of_numbers , num_of_terms)
print(min_num)