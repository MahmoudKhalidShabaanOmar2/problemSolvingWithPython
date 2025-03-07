# write a python program to get different numbers from the user , and store in the list , and then find the maximum number by using function methods =>
# num_of_terms = int(input("please enter the numbers of the terms is = "))
# lista_of_numbers = []
# def get_maximum_number(list_of_num , terms) :
#     for i in range(terms) :
#         num = int(input("please enter the different numbers to store in the list of the numbers is = "))
#         list_of_num . append(num)
#     print("the list of the different number is  : "+str(list_of_num))
#     maximum_num_between_list_numbers = max(list_of_num)
#     print("the maximum number between the different numbers in the list of the numbers is = "+str(maximum_num_between_list_numbers))
# get_maximum_number(lista_of_numbers , num_of_terms)

def get_maximum_number(list_of_num , terms) :
    for i in range(terms) :
        num = int(input("please enter the different numbers to store in the list of the numbers is = "))
        list_of_num . append(num)
    print("the list of the diifferent numbers is = "+str(list_of_num))
    maximum_num_between_list_numbers = max(list_of_num)
    return("the maximum number between the different numbers in the list of the numbers is = "+str(maximum_num_between_list_numbers))
lista_of_numbers = []
num_of_terms = int(input("please enter the numbers of the terms is = "))
max_num = get_maximum_number(lista_of_numbers , num_of_terms)
print(max_num)