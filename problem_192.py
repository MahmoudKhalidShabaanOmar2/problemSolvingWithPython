# write a python program to get percentage calculator by using different function methods =>
# pre_number = int(input("please enter the pre number is = "))
# amount_number = int(input("please enter the amount number is = "))
# def make_percentage_calculator(p_num , a_num) :
#     print("the pre number is = "+str(p_num))
#     print("the amount number is = "+str(a_num))
#     percentage_calculator = (p_num * a_num) / 100
#     print("the result of the percentage calculator is = "+str(percentage_calculator)+"%")
# make_percentage_calculator(pre_number , amount_number)

# def make_percentage_calculator(p_num , a_num) :
#     print("the pre number is = "+str(p_num))
#     print("the amount number is = "+str(a_num))
#     percentage_calculator = (p_num * a_num) / 100
#     return("the result of the percentage calculator is = "+str(percentage_calculator)+"%")
# pre_number = int(input("please enter the pre number is = "))
# amount_number = int(input("please enter the amount number is = "))
# percentage = make_percentage_calculator(pre_number , amount_number)
# print(percentage)

# pre_number = int(input("please enter the pre number is = "))
# amount_number = int(input("please enter the amount number is = "))
# def make_percentage_calculator(p_num , a_num) :
#     print("the pre number is = "+str(p_num))
#     print("the amount number is = "+str(a_num))
#     if((p_num > 0) and (a_num > 0)) :
#         percentage_calculator = (p_num * a_num) / 100
#         print("the result of the percentage calculator is = "+str(percentage_calculator)+"%")
#     elif((p_num == 0) or (a_num == 0)) :
#         print("there is no result of the percentage calculator")
#     else :
#         print("please enter valid pre number , and valid amount number to get percentage calculator")
# make_percentage_calculator(pre_number , amount_number)

def make_percentage_calculator(p_num , a_num) :
    print("the pre number is = "+str(p_num))
    print("the amount number is = "+str(a_num))
    if((p_num > 0) and (a_num > 0)) :
        percentage_calculator = (p_num * a_num) / 100
        return ("the result of the percentage calculator is = "+str(percentage_calculator)+"%")
    elif((p_num == 0) and (a_num == 0)) :
        return("the result of the percentage calculator is = 0")
    else :
        return("please enter a valid pre number , or valid amount number")
pre_num = int(input("please enter the frist number is = "))
amount_num = int(input("please enter the amount number is = "))
percentage = make_percentage_calculator(pre_num , amount_num)
print(percentage)