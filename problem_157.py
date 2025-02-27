# write a python program to get two numbers from the user , and then swapping the values of the two numbers without using temporary value =>
frist_num = int(input("please enter the frist number is = "))
second_num = int(input("please enter the second number is = "))
print("the different values of the two numbers before swapping the vaules of the two numbers without using temporary value is : \n")
print("the frist number is = "+str(frist_num))
print("the second number is = "+str(second_num))
# frist_num , second_num = second_num , frist_num 

# second_num , frist_num = frist_num , second_num 

# frist_num = frist_num + second_num 
# second_num = frist_num - second_num 
# frist_num = frist_num - second_num 

# second_num = second_num + frist_num 
# frist_num = second_num - frist_num 
# second_num = second_num - frist_num 

# frist_num = frist_num * second_num 
# second_num = frist_num / second_num 
# frist_num = frist_num / second_num 

# second_num = second_num * frist_num 
# frist_num = second_num / frist_num 
# second_num = second_num / frist_num 

# frist_num = frist_num ^ second_num 
# second_num = frist_num ^ second_num 
# frist_num = frist_num ^ second_num 

second_num = second_num ^ frist_num 
frist_num = second_num ^ frist_num 
second_num = second_num ^ frist_num 
print("the different values of the two number after swapping the values of the two numbers without using temporary value is : \n")
print("the frist number is = "+str(frist_num))
print("the second number is = "+str(second_num))