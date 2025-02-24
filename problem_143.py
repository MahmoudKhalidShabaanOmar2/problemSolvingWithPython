# write a python program to get starting number as large number , and ending number as lower number from the user and then display all numbers from large number to ending number in the properly sequence , and then find the sum of the all numbers =>
starting_number_as_large_number = int(input("please enter the frist number as large number is = "))
ending_number_as_lower_number = int(input("please enter the ending number as lower number is = "))
print("the starting number as large number is = "+str(starting_number_as_large_number))
print("the ending number as lower number is = "+str(ending_number_as_lower_number))
print("generate all numbers from starting number as large number is = "+str(starting_number_as_large_number)+" to the ending number as lower number is = "+str(ending_number_as_lower_number)+" in the properly(ascending) sequence is : ")
sum_of_all_numbers = 0 
for num in range(starting_number_as_large_number , ending_number_as_lower_number - 1 , -1) :
    print(num)
    sum_of_all_numbers += num 
print("the sum of the all numbers from starting number as large number is = "+str(starting_number_as_large_number)+" to ending number as lower number is = "+str(ending_number_as_lower_number)+" is = "+str(sum_of_all_numbers))