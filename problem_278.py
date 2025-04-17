# write a python program to get number from the user , and then get the next number , and get the sum of the next number , and your entered number , and at the end get the previous number , and get the sum of the previous number , and your entered number => 
number = int(input("Please Enter The Number Is = "))
print("The Number Is = ",str(number))
next_number = number + 1 
print("The Next Number Is = ",str(next_number))
sum_of_num_next_num = number + next_number 
print("The Sum Of The Number , And The Next Number Is = ",str(sum_of_num_next_num))
previous_number = number - 1 
print("The Previous Number Is = ",str(previous_number))
sum_of_num_previous_num = number + previous_number 
print("The Sum Of The Number , And The Previous Number Is = "+str(sum_of_num_previous_num))