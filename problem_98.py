# write a python to get two numbers from the user , and then display the minimum number by using different functions methods =>
# frist_number = float(input("please enter the frist number is = "))
# second_number = float(input("please enter the second number is = "))
# def get_minimum_num(fri_num , sec_num) :
#     print("the different values of the two numbers is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     if(fri_num < sec_num) :
#         print("the frist number is the minimum number , and the frist number is = "+str(fri_num))
#     else :
#         print("the second number is the minimum number , and the second number is = "+str(sec_num))
# get_minimum_num(frist_number , second_number)

# frist_number = float(input("please enter the frist number is = "))
# second_number = float(input("please enter the second number is = "))
# def get_minimum_num(fri_num , sec_num) :
#     print("the different values of the two numbers is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     minimum_number = min(fri_num , sec_num)
#     print("the minimum number between the two numbers is = "+str(minimum_number))
# get_minimum_num(frist_number , second_number)

# def get_minimum_num(fri_num , sec_num) :
#     print("the different values of the two numbers is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     if(fri_num < sec_num) :
#         return("the frist number is the minimum number , and the frist number is = "+str(fri_num))
#     else : 
#         return("the second number is the minimum number , and the second number is = "+str(sec_num))
# frist_number = float(input("please enter the frist number is = "))
# second_number = float(input("please enter the second number is = "))
# min_num = get_minimum_num(frist_number , second_number)
# print(min_num)

def get_minimum_num(fri_num , sec_num)  :
    print("the different values of the two numbers is : \n")
    print("the frist number is = "+str(fri_num))
    print("the second number is = "+str(sec_num))
    minimum_number = min(fri_num , sec_num)
    return("the minimum number between the two numbers is = "+str(minimum_number))
frist_number = float(input("please enter the frist number is = "))
second_number = float(input("please enter the second number is = "))
min_num = get_minimum_num(frist_number , second_number)
print(min_num)