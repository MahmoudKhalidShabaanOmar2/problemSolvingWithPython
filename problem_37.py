# write a python program to get two numbers and get the maximum number between the two numbers by using function methods =>
# frist_num = float(input("please enter the frist number is = "))
# second_num = float(input("please enter the second number is = "))
# def get_maximum_number(fri_num , sec_num) :
#     print("the different values of the two numbers is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     maximum_num_between_two_numbers = max(fri_num , sec_num)
#     print("the maximum number between the two numbers is = "+str(maximum_num_between_two_numbers))
# get_maximum_number(frist_num , second_num)

# frist_num = float(input("please enter the frist number is = "))
# second_num = float(input("please enter the second number is = "))
# def get_maximum_number(fri_num , sec_num) : 
#     print("the different values of the two numbers is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     if(fri_num > sec_num) :
#         print("the frist number is grater than the second number , because the frist number is = "+str(fri_num))
#     elif(fri_num == sec_num) :
#         print("the frist number is equal to second number , because the frist number is = "+str(fri_num)+" , and the second number is = "+str(second_num))
#     else :
#         print("the second number is grater than the frist number , because the second number is = "+str(sec_num))
# get_maximum_number(frist_num , second_num)

# def get_maximum_number(fri_num , sec_num) :
#     print("the different values of the two numbers is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     maximum_num = max(fri_num , sec_num)
#     return("the maximum number between the two numbers is = "+str(maximum_num))
# frist_num = float(input("please enter the frist number is = "))
# second_num = float(input("please enter the second number is = "))
# maximum_num_between_two_numbers = get_maximum_number(frist_num , second_num)
# print(maximum_num_between_two_numbers)

def get_maximum_number(fri_num , sec_num) :
    print("the different values of the two numbers is : \n")
    print("the frist number is = "+str(fri_num))
    print("the second number is = "+str(sec_num))
    if(fri_num > sec_num) :
        print("the frist number is grater than the second number , because the frist number is = "+str(fri_num))
    elif(fri_num == sec_num) :
        print("the frist number is equal to second number because the frist number is = "+str(fri_num)+" , and the second number is = "+str(sec_num))
    else :
        print("the second number is grater than the frist number , because the second number is = "+str(sec_num))
frist_num = float(input("please enter the frist number is = "))
second_num = float(input("please enter the second number is = "))
maximum_num_between_two_numbers = get_maximum_number(frist_num , second_num)
print(maximum_num_between_two_numbers)