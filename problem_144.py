# write a python program to get starting number as large number , and ending number as lower number from the user , and then display all numbers from starting number as large number to ending number as lower number in the properly sequence , and find the sum of the all numbers by using function method=>
starting_number_as_large_number = int(input("please enter the starting number as large number is = "))
ending_number_as_lower_number = int(input("please enter the ending number as lower number is = "))
def generate_all_numbers_from_large_to_ending_num_and_sum_of_all_numbers(starting_num_as_large_num , ending_num_as_lower_num) :
    print("the starting number as large number is = "+str(starting_num_as_large_num))
    print("the ending number as lower number is = "+str(ending_num_as_lower_num))
    print("generating all numbers from the starting number as large number is = "+str(starting_num_as_large_num)+" to the ending number as lower number is = "+str(ending_num_as_lower_num)+" in the properly sequence is : ")
    sum_of_all_numbers = 0
    for num in range(starting_num_as_large_num , ending_num_as_lower_num - 1 , -1) :
        print(num)
        sum_of_all_numbers += num 
    print("the sum of the all numbers from the starting number as large number is = "+str(starting_num_as_large_num)+" to the ending number as lower number is = "+str(ending_num_as_lower_num)+" is = "+str(sum_of_all_numbers))
generate_all_numbers_from_large_to_ending_num_and_sum_of_all_numbers(starting_number_as_large_number , ending_number_as_lower_number)
    