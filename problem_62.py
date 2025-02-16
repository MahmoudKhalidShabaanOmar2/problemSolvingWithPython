# write a python program to get five numbers from the user in array , and then find the multiplication of the all numbers from the array of the numbers =>
# import array as arr 
# array_of_numbers = arr . array("i" , [])
# array_of_numbers = []
# for i in range(5) :
    # array_of_numbers . append(int(input("please enter the all numbers to store in the array of the numbers is = ")))
array_of_numbers = [int(input("please enter the all numbers to store in the array of the numbers is = ")) for i in range(5)]
mul_of_all_numbers_in_array = 1
print("the array of the numbers is : \n")
for j in range(5) :
    print(array_of_numbers[j])
    mul_of_all_numbers_in_array *= array_of_numbers[j]
print("the multiplication of the all numbers in the array of the number is = "+str(mul_of_all_numbers_in_array))