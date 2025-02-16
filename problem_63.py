# write a python program to get five numbers from the user in array and sum all numbers and display by using function methods =>
# import array as arr 
# array_of_numbers = arr . array("i" , [])
array_of_numbers = []
def get_array_of_all_numbers(arr_of_num) :
    # for i in range(5) :
        # arr_of_num . append(int(input("please enter the all numbers to store in the array of the numbers is = ")))
    arr_of_num = [int(input("please enter the all numbers to store in the array of the numbers is = ")) for i in range(5)]
    print("the array of the numbers is : \n")
    # sum_of_all_numbers_in_array = 0
    for j in range(5) :
        print(arr_of_num[j])
        # sum_of_all_numbers_in_array += arr_of_num[j]
    sum_of_all_numbers_in_array = sum(arr_of_num)
    print("the sum of the all numbers in the array of the numbers is = "+str(sum_of_all_numbers_in_array))
get_array_of_all_numbers(array_of_numbers)