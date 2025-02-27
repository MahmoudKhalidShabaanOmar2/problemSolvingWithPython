# write a python program to get two numbers from the user , and then swapping the two values of the two numbers by using temporary values by using different function methods =>
# frist_number = int(input("please enter the frist number is = "))
# second_number = int(input("please enter the second number is = "))
# def swapping_values_of_numbers(fri_num , sec_num) :
#     print("the two values of the two numbers before swapping the two values of the two numbers by using temporary value is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     # temporary_value = fri_num 
#     # fri_num = sec_num 
#     # sec_num = temporary_value 
#     temporary_num = sec_num 
#     sec_num = fri_num 
#     fri_num = temporary_num 
#     print("the different two values of the two numbers after swaaping the two values of the numbers by using temporary value is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
# swapping_values_of_numbers(frist_number , second_number)

def swapping_values_of_numbers(fri_num , sec_num) :
    print("the two values of the two numbers before swapping the two values of the two numbers by using temporary value is : \n")
    print("the frist number is = "+str(fri_num))
    print("the second number is = "+str(sec_num))
    # temporary_value = fri_num 
    # fri_num = sec_num 
    # sec_num = temporary_value 
    temporary_value = sec_num 
    sec_num = fri_num 
    fri_num = temporary_value 
    print("the two values of the two numbers after swapping the two values of the two numbers by using temporary value is : \n")
    print("the frist number is = "+str(fri_num))
    return("the second number is = "+str(sec_num))
frist_number = int(input("please enter the frist number is = "))
second_number = int(input("please enter the second number is = "))
swapping_numbers = swapping_values_of_numbers(frist_number , second_number)
print(swapping_numbers)