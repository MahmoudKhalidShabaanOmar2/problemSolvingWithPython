# write a python program to get two numbers from the user , and then find the maximum number =>
# frist_num = float(input("please enter the frist number is = "))
# second_num = float(input("please enter the second number is = "))
# print("the different values of the two numbers is : \n")
# print("the frist number is = "+str(frist_num))
# print("the second number is = "+str(second_num))
# if(frist_num > second_num) :
#     print("the frist number is the maximum number"+" , and the frist number is = "+str(frist_num))
# else :
#     print("the second number is the maximum number , and the second number is = "+str(second_num))

frist_num = float(input("please enter the frist number is = "))
second_num = float(input("please enter the second number is = "))
print("the different values of the two numbers is : \n")
print("the frist mumber is = "+str(frist_num))
print("the second number is = "+str(second_num))
maximum_num = max(frist_num , second_num)
print("the maximum number between the two numbers is = "+str(maximum_num))