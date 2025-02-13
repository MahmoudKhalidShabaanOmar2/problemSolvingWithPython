# write a python program to get the maximum number between two numbers =>
# frist_num = float(input("please enter the frist number is = "))
# second_num = float(input("please enter the second number is = "))
# print("the different values of the two numbers is : \n")
# print("the frist number is = "+str(frist_num))
# print("the second number is = "+str(second_num))
# maximum_num_between_two_numbers = max(frist_num , second_num)
# print("the maximum number between the two numbers is = "+str(maximum_num_between_two_numbers))

frist_num = float(input("please enter the frist number is = "))
second_num = float(input("please enter the second number is = "))
print("the different values of the two numbers is : \n")
print("the frist number is = "+str(frist_num))
print("the second number is = "+str(second_num))
if(frist_num > second_num) :
    print("the frist number is grater than the second number , because the frist number is = "+str(frist_num))
elif(frist_num == second_num) :
    print("the frist number is equal to the second number , because the frist number is = "+str(frist_num)+" , and the second number is = "+str(second_num))
else :
    print("the second number is grater than the frist number , because the second number is = "+str(second_num))