# write a python program to get all arthimetic operations on the three numbers by using function methods=>
# frist_number = float(input("please enter the frist number is = "))
# second_number = float(input("please enter the second number is = "))
# third_number = float(input("please enter the third number is = "))
# def get_all_arthimetic_operations_on_two_numbers(fri_num , sec_num , thi_num) :
#     print("the values of the three numbers is : \n")
#     print("the frist number is = "+str(fri_num))
#     print("the second number is = "+str(sec_num))
#     print("the third number is = "+str(thi_num))
#     print("all arthimetic operations on the three numbers is : \n")
#     print("the result of the addition arthimetic operation on the three numbers is = "+str(fri_num + sec_num + thi_num))
#     print("the result of the subtraction arthimetic operation on the three numbers is = "+str(fri_num - sec_num - thi_num))
#     print("the result of the multiplication arthimetic operation on the three numbers is = "+str(fri_num * sec_num * thi_num))
#     print("the result of the division arthimetic operation on the three numbers is = "+str(fri_num / sec_num / thi_num))
#     print("the result of the modulus arthimetic operation on the three numbers is = "+str(fri_num % sec_num % thi_num))
# get_all_arthimetic_operations_on_two_numbers(frist_number , second_number , third_number)

def get_all_arthimetic_operations_on_three_numbers(fri_num , sec_num , thi_num) :
    print("the values of the three numbers is : \n")
    print("the frist number is = "+str(fri_num))
    print("the second number is = "+str(sec_num))
    print("the third number is = "+str(thi_num))
    add_of_num = fri_num + sec_num + thi_num
    sub_of_num = fri_num - sec_num - thi_num 
    mul_of_num = fri_num * sec_num * thi_num 
    div_of_num = fri_num / sec_num / thi_num 
    mod_of_num = fri_num % sec_num % thi_num
    print("the result of the addition arthimetic operation on three numbers is = "+str(add_of_num))
    print("the result of the subtraction arthimetic operation on three numbers is = "+str(sub_of_num))
    print("the result of the mulitplication arthimetic operation on three numbers is = "+str(mul_of_num))
    print("the result of the division arthimetic operation on three numbers is = "+str(div_of_num))
    print("the result of the modulus arthimetic operation on three numbers is = "+str(mod_of_num))
frist_number = float(input("please enter the frist number is = "))
second_number = float(input("please enter the second number is = "))
third_number = float(input("please enter the third number is = "))
arthimetic_operation_on_three_numbers = get_all_arthimetic_operations_on_three_numbers(frist_number , second_number , third_number)