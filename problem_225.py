# write a python program to find the sum of two numbers (that the two numbers must be positive numbers , and less than 50 also) =>
frist_num = int(input("please enter the frist number is = "))
second_num = int(input("please enter the second number is = "))
print("the different values of the two numbers is : \n")
print("the value of the frist number is = "+str(frist_num))
print("the value of the second number is = "+str(second_num))
if(((frist_num > 0) and (second_num > 0)) and ((frist_num < 50) and (second_num < 50))) :
    sum_of_frist_number_second_number = frist_num + second_num 
    print("the result of the sum of the frist number , and second number is = "+str(sum_of_frist_number_second_number))
else :
    print("there is no result of the sum of the frist number , and second number")