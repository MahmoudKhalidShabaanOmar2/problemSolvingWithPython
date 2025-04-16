# write a python program to get numbers from the user in a list of numbers , and then store in a tuple of numbers , and then check if the frist number from the tuple of the number is equal to the last number from the tuple of the number by using function method => 
# lista_of_numbers = []
# number_of_terms = int(input("Please Enter All Numbers To Store In The List Of The Numbers Is = "))
# for i in range(5) :
#     numbers = int(input("Please Enter All Numbers To Store In The List Of The Numbers Is = "))
#     lista_of_numbers.append(numbers)
# print("The LIst Of The Numbers Is : "+str(lista_of_numbers))
# for k in lista_of_numbers : 
#     print(k)
# tuples_of_numbers = tuple(lista_of_numbers) 
# def get_tuple_of_numbers(tup_of_num) :
#     print("The Tuple Of All Numbers Is : "+str(tup_of_num))
#     print("Check If The Frist Number From The Tuple Of The Number Is Equal To The Last Number From The Tuple Of The Number Is : ")
#     if(tup_of_num[0] == tup_of_num[-1]) :
#         print("The Frist Number From The Tuple Of The Number Is Equal To The Last Number From The Tuple Of The Number")
#     else :
#         print("The Frist Number From The Tuple Of The Number Is Not Equal To The Last Number From The Tuple Of The Number")
# get_tuple_of_numbers(tuples_of_numbers)

def get_tuple_of_numbers(list_of_num , tup_of_num) :
    print("The List Of All Numbers Is : "+str(list_of_num))
    for j in list_of_num :
        print(j)
    tup_of_num = tuple(list_of_num)
    print("The Tuple Of All Numbers Is : "+str(tup_of_num))
    for i in tup_of_num :
        print(i)
    print("check If The Frist Number From The Tuple Of The Number Is Equal To The Last Number From The Tuple Of The Number")
    if(tup_of_num[0] == tup_of_num[-1]) :
        return("The Frist Number From The Tuple Of The Numbers Is Equal To The Last Number From The Tuple Of The Number")
    else :
        return("The Frist Number From The Tuple Of The Numbers Is Not Equal To The Last Number From The Tuple Of The Number")
lista_of_numbers = []
number_of_terms = int(input("Please Enter The Number Of Terms Is = "))
for k in range(number_of_terms) :
    numbers = int(input("Please Enter All Numbers To Store In The List Of The Numbers Is = "))
    lista_of_numbers.append(numbers)
tuples_of_numbers = ()
displaying_tuples_of_numbers = get_tuple_of_numbers(lista_of_numbers , tuples_of_numbers)
print(displaying_tuples_of_numbers)