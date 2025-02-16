# write a python program to get two numbers , and arthimetic operations from the user to perform all arthimetic operations =>
frist_num = float(input("please enter the frist number is = "))
second_num = float(input("please enter the second number is = "))
arthimetic_operation = input("please enter the arthimetic operation is : ")
if(arthimetic_operation == "+") :
    print("the result of the addition arthimetic operation of the two numbers is = "+str(frist_num + second_num))
elif(arthimetic_operation == "-") :
    print("the result of the subtraction arthimetic operation of the two numbers is = "+str(frist_num - second_num))
elif(arthimetic_operation == "*") :
    print("the result of the multplication arthimetic operation of the two numbers is = "+str(frist_num * second_num))
elif(arthimetic_operation == "/") :
    print("the result of the division arthimetic operation of the two numbers is = "+str(frist_num / second_num))
elif(arthimetic_operation == "%") :
    print("the result of the modulus arthimetic operation of the two numbers is = "+str(frist_num % second_num))
elif(arthimetic_operation == "**") :
    print("the result of the square arthimetic operation of the two numbers is = "+str(frist_num ** second_num))
else :
    print("please enter one of the valid arthimetic operation to perform this arthimetic operation on the two numbers")
