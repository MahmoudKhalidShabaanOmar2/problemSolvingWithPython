# write a python program to get two numbers from the user to get the sum of the two numbers (that the frist number must be positive , and frist number  is less than 50 , and second number is a negative number , and the second number is grater tham 20 ) by using different function methods =>
# frist_number = int(input("please enter the frist number is = "))
# second_number = int(input("please enter the second number is = "))
# def get_sum_of_two_numbers(fri_num , sec_num) :
#     print("the different values of the two numbers is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     if(((fri_num > 0) and (fri_num < 50)) and ((sec_num < 0) and (sec_num > -20))) :
#         sum_of_two_numbers = fri_num + sec_num 
#         print("the sum of the frist number , and second number is = "+str(sum_of_two_numbers))
#     else :
#         print("please enter a valid two numbers , there is no sum of the two numbers")
# get_sum_of_two_numbers(frist_number , second_number)

def get_sum_of_two_numbers(fri_num , sec_num) :
    print("the different values of the two numbers is : \n")
    print("the value of the frist number is = "+str(fri_num))
    print("the value of the second number is = "+str(sec_num))
    if(((fri_num > 0) and (fri_num < 50)) and ((sec_num < 0) and (sec_num > -20))) :
        sum_of_two_numbers = fri_num + sec_num 
        return("the sum of the two numbers is = "+str(sum_of_two_numbers))
    else :
        return("please enter a valid two numbers , there is no sum of the two numbers")
frist_number = int(input("please enter the frist number is = "))
second_number = int(input("please enter the second number is = "))
sum_of_numbers = get_sum_of_two_numbers(frist_number , second_number)
print(sum_of_numbers)