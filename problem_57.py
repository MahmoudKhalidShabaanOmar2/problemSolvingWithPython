# write a python program to get three numbers from the user , and solve this equation (e = a + b + ac / b * (2a + 3b)) =>
frist_num = float(input("please enter the frist number is = "))
second_num = float(input("please enter the second number is = "))
third_num = float(input("please enter the third number is = "))
print("the different values of the three numbers is : \n")
print("the frist number is = "+str(frist_num))
print("the second number is = "+str(second_num))
print("the third number is = "+str(third_num))
result_of_equation_of_numbers = frist_num + second_num + third_num * frist_num / second_num * (2 * frist_num + 3 * second_num)
print("the result of the equation of the different numbers is = "+str(result_of_equation_of_numbers))