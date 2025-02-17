# write a python program to get two numbers , and arthimetic operations from the user to perform all arthimetic operations by using function methods =>
frist_number = float(input("please enter the frist number is = "))
second_number = float(input("please enter the second number is = "))
arthimetic_operation = input("please enter the arthimetic operation is : ")
def get_all_arthimetic_operations_on_two_numbers(fri_num , sec_num , arthi_oper) :
    print("the frist number is = "+str(fri_num))
    print("the second number is = "+str(sec_num))
    print("the arthimetic operation is : "+arthi_oper)
    if(arthi_oper == "+") :
        print("the result of the addition arthimetic operation on the two numbers is = "+str(fri_num + sec_num))
    elif(arthi_oper == "-") :
        print("the result of the subtraction arthimetic operation on the two numbers is = "+str(fri_num - sec_num))
    elif(arthi_oper == "*") :
        print("the result of the multiplication arthimetic operation on the two numbers is = "+str(fri_num * sec_num))
    elif(arthi_oper == "/") :
        print("the result of the division arthimetic operation on the two numbers is = "+str(fri_num / sec_num))
    elif(arthi_oper == "%") :
        print("the result of the modulus arthimetic operation on the two numbers is = "+str(fri_num % sec_num))
    elif(arthi_oper == "**") :
        print("the result of the square arthimetic operation on the two numbers is = "+str(fri_num ** sec_num))
    else :
        print("please enter one of the valid arthimetic operation to perform this arthimetic operation on the two numbers")
get_all_arthimetic_operations_on_two_numbers(frist_number , second_number , arthimetic_operation)
    
