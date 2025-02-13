# write a python program to get three numbers from the user , and then get the maximum number =>
# frist_num = float(input("please enter the frist number is = "))
# second_num = float(input("please enter the second number is = "))
# third_num = float(input("please enter the third number is = "))
# print("the different values of the three numbers is : \n")
# print("the frist number is = "+str(frist_num))
# print("the second number is = "+str(second_num))
# print("the third_num is = "+str(third_num))
# maximum_num_between_three_numbers = max(frist_num , second_num , third_num)
# print("the maximum number between the three numbers is = "+str(maximum_num_between_three_numbers))

frist_num = float(input("please enter the frist number is = "))
second_num = float(input("please enter the second number is = "))
third_num = float(input("please enter the third number is = "))
print("the different values of the two number is : \n")
print("the frist number is = "+str(frist_num))
print("the second number is = "+str(second_num))
print("the third number is = "+str(third_num))
if((frist_num > second_num) and (frist_num > third_num)) :
    print("the frist number is grater than the second number , and third number , because the frist number is = "+str(frist_num))
elif((second_num > frist_num) and (second_num > third_num)) :
    print("the second number is grater than the frist number , and third number , because the second number is = "+str(second_num))
elif((third_num > frist_num) and (third_num > second_num)) :
    print("the third number is grater than the frist number , and second number , because the third number id = "+str(third_num))
else :
    print("the frist number is equal to second number , and third number , because the frist number is = "+str(frist_num)+" , second number is = "+str(second_num)+" , and at the end the third number is = "+str(third_num))