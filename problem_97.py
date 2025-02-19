# write a python program to get two numbers from the user , and then find the minimum number =>
# frist_num = float(input("please enter the frist number is = "))
# second_num = float(input("please enter the second number is = "))
# print("the different values of the two numbers is : \n")
# print("the frist number is = "+str(frist_num))
# print("the second number is = "+str(second_num))
# if(frist_num < second_num) :
#     print("the frist number is the minimum number , and the frist number is = "+str(frist_num))
# else :
#     print("the second number is the minimum number , and the second number is = "+str(second_num))
    
frist_num = float(input("please enter the frist number is = "))
second_num = float(input("please enter the second number is = "))
print("the different values of the two numbers is : \n")
print("the frist number is = "+str(frist_num))
print("the second number is = "+str(second_num))
minimum_num = min(frist_num , second_num)
print("the minimum number between the two numbers is = "+str(minimum_num))