# write a python program to get five numbers from the user in array and sum all numbers and display =>
# import array as arr 
# array_of_numbers = arr . array("i" , [])
# array_of_numbers = []
# for i in range(5) :
    # array_of_numbers . append(int(input("please enter the all numbers to store in the array of the numbers is = ")))
array_of_numbers = [int(input("please enter the all numbers to store in the list of the numbers is = ")) for i in range(5)]
print("the array of the numbers is : \n")
# sum_of_all_numbers_in_array = 0
for j in range(5) :
    print(array_of_numbers[j])
    # sum_of_all_numbers_in_array += array_of_numbers[j]
sum_of_all_numbers_in_array = sum(array_of_numbers)
print("the sum of the all numbers in the array of the numbers is = "+str(sum_of_all_numbers_in_array))