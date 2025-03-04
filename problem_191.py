# write a python program to make a percentage calculator =>
# pre_number = int(input("please enter the pre number is = "))
# amount_number = int(input("please enter the amount number is = "))
# print("the pre number is = "+str(pre_number))
# print("the amount number is = "+str(amount_number))
# percentage_calculator = (pre_number * amount_number) / 100
# print("the result of the percentage calculator is = "+str(percentage_calculator)+"%")

pre_number = int(input("please enter the pre number is = "))
amount_number = int(input("please enter the amount number is = "))
print("the pre number is = "+str(pre_number))
print("the amount number is = "+str(amount_number))
if((pre_number > 0) and (amount_number > 0)) :
    percentage_calculator = (pre_number * amount_number) / 100
    print("the result of the percentage calculator is = "+str(percentage_calculator)+"%")
elif((pre_number == 0) or (amount_number == 0)) :
    print("the result of the percentage calculator is = 0")
else :
    print("please enter valid pre number , or valid amount number to get the result of the percentage calculator")