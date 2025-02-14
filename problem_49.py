# write a python program to get all compound assignment operations on an integer number , and then get the sum of the all compound assignment operations =>
num = int(input("please enter the number is = "))
print("the number is = "+str(num))
results_of_all_compound_assignment_operations = [num]
num += 10
print("the result of the addition compound assignment operation is = "+str(num))
results_of_all_compound_assignment_operations . append(num)
num -= 10
print("the result of the subtraction compound assignment operation is = "+str(num))
results_of_all_compound_assignment_operations . append(num)
num *= 10
print("the result of the multiplication compound assignment operation is = "+str(num))
results_of_all_compound_assignment_operations . append(num)
num /= 10
print("the result of the division compound assignment operation is = "+str(num))
results_of_all_compound_assignment_operations . append(num)
num **= 10
print("the result of the square compound assignment operation is = "+str(num))
results_of_all_compound_assignment_operations . append(num)
print("the results of the all compound assignment operations is = "+str(results_of_all_compound_assignment_operations))
sum_of_all_results_of_all_compound_assignment_operations = sum(results_of_all_compound_assignment_operations)
print("the sum of the all results of the all compound assignment operations is = "+str(sum_of_all_results_of_all_compound_assignment_operations))