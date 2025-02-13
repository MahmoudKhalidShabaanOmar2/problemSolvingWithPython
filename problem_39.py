# write a python program to get three numbers from the user , and then get the maximum number by using function methods =>
# frist_num = float(input("please enter the frist number is = "))
# second_num = float(input("please enter the second number is = "))
# third_num = float(input("please enter the third number is = "))
# def get_maximum_num_between_three_numbers(fri_num , sec_num , thi_num) :
#     print("the different values of the three numbers is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     print("the third number is = "+str(thi_num))
#     maximum_num = max(fri_num , sec_num , thi_num)
#     print("the maximum number between the three numbers is = "+str(maximum_num))
# get_maximum_num_between_three_numbers(frist_num , second_num , third_num)
    
# frist_num = float(input("please enter the frist number is = "))
# second_num = float(input("please enter the second number is = "))
# third_num = float(input("please enter the third number is = "))
# def get_maximum_num_between_three_numbers(fri_num , sec_num , thi_num) :
#     print("the different values of the three numbers is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     print("the third number is = "+str(thi_num))
#     if((fri_num > sec_num) and (fri_num > thi_num)) : 
#         print("the frist number is grater than the second number , and third number , because the frist number is = "+str(fri_num))
#     elif((sec_num > fri_num) and (sec_num > thi_num)) :
#         print("the second number is grater than the frist number , and third number , because the second number is = "+str(sec_num))
#     elif((thi_num > fri_num) and (thi_num > sec_num)) :
#         print("the third number is grater than the frist number , and second number , because the third number is = "+str(thi_num))
#     else :
#         print("the frist number is equal to the second  , and third number , because the frist number is = "+str(fri_num)+" , the second number is = "+str(sec_num)+" , and at the end the third number is = "+str(thi_num))
# get_maximum_num_between_three_numbers(frist_num , second_num , third_num)

def get_maximum_num_between_three_numbers(fri_num , sec_num , thi_num) :
    print("the different values of the three numbers is : \n")
    print("the frist number is = "+str(fri_num))
    print("the second number is = "+str(sec_num))
    print("the third number is = "+str(thi_num))
    maximum_num_between_three_numbers = max(fri_num , sec_num , thi_num) 
    return ("the maximum number between the three numbers is = "+str(maximum_num_between_three_numbers))
frist_num = float(input("please enter the frist number is = "))
second_num = float(input("please enter the second number is = "))
third_num = float(input("please enter the third number is = "))
max_num = get_maximum_num_between_three_numbers(frist_num , second_num , third_num)
print(max_num)