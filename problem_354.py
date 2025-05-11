# write a python program to append numbers in the list of the numbers that divisible by five , and seven from a range from 10 to 100 by using function methods =>
lista_of_numbers_from_10_to_100 = []
for nums in range(10 , 101) :
    lista_of_numbers_from_10_to_100.append(nums)
def get_lista_of_numbers_from_10_to_100(list_of_nums_from_10_to_100) :
    print("The List Of The Numbers From 10 To 100 In The Properly (Ascending) Sequence Is : ",str(list_of_nums_from_10_to_100))
    for j in list_of_nums_from_10_to_100 :
        print(j)
    lista_of_numbers_from_10_to_100_that_divisible_by_7_5 = []
    for k in list_of_nums_from_10_to_100 :
        if((k %5 == 0) and (k %7 ==0)) :
            lista_of_numbers_from_10_to_100_that_divisible_by_7_5.append(k)
    print("The List Of The Numbers From 10 To 100 That Divisible By Five , And Seven In The Properly (Ascending) Sequence Is : ",str(lista_of_numbers_from_10_to_100_that_divisible_by_7_5))
    for i in lista_of_numbers_from_10_to_100_that_divisible_by_7_5 :
        print(i)
get_lista_of_numbers_from_10_to_100(lista_of_numbers_from_10_to_100)
    