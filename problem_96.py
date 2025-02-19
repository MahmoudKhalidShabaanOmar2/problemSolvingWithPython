# write a python program to get two numbers from the user and then display the maximum number between the two numbers by using different functions methods =>
# frist_number = float(input("please enter the frist number is = "))
# second_number = float(input("please enter the second number is = "))
# print("the different values of the two numbers is : \n")
# def get_maximum_num(fri_num , sec_num) :
#     print("the different values of the two numbers is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     if(fri_num > sec_num) :
#         print("the frist number is the maximum number , and the frist number is = "+str(fri_num))
#     else :
#         print("the second number is the maximum number , and the second number is = "+str(sec_num))
# get_maximum_num(frist_number , second_number)

# frist_number = float(input("please enter the frist number is = "))
# second_number = float(input("please enter the second number is = "))
# def get_maximum_num(fri_num , sec_num) :
#     print("the different values of the two numbers is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     maximum_number = max(fri_num , sec_num)
#     print("the maximum number between the two number is = "+str(maximum_number))
# get_maximum_num(frist_number , second_number)

# def get_maximum_num(fri_num , sec_num) :
#     print("the different values of the two numbers is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     if(fri_num > sec_num) :
#         return("the frist number is the maximum number , and the frist number is = "+str(fri_num))
#     else :
#         return("the second number is the maximum number , and the second number is = "+str(sec_num))
# frist_number = float(input("please enter the frist number is = "))
# second_number = float(input("please enter the second number is = "))
# max_num = get_maximum_num(frist_number , second_number)
# print(max_num)

def get_maximum_num(fri_num , sec_num) :
    print("the different values of the two numbers is : \n")
    print("the frist number is = "+str(fri_num))
    print("the second number is = "+str(sec_num))
    maximum_number = max(fri_num , sec_num)
    return("the maximum number between the two numbers is = "+str(maximum_number))
frist_number = float(input("please enter the frist number is = "))
second_number = float(input("please enter the second number is = "))
max_num = get_maximum_num(frist_number , second_number)
print(max_num)