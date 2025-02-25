# write a python program to get two numbers from the user , and then swap the value of the two numbers by using temporary value =>
frist_num = int(input("please enter the frist number is = "))
second_num = int(input("please enter the second number is = "))
print("the two values of the two numbers before swapping the two values of the two numbers is : \n")
print("the frist number is = "+str(frist_num))
print("the second number is = "+str(second_num))
# temporary_value = frist_num 
# frist_num = second_num 
# second_num = temporary_value
temporary_value = second_num 
second_num = frist_num 
frist_num = temporary_value  
print("the two values of the two numbers after swapping the two values of the two numbers is : \n")
print("the frist number is = "+str(frist_num))
print("the second number is = "+str(second_num))
