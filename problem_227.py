# write a python program to get two numbers from the user , and then get the sum of the two numbers (that frist number should be positive , and second number should be negative , frist number less than 50 , and second number grater than 20) =>
frist_number = int(input("please enter the frist number is = "))
second_number = int(input("please enter the second number is = "))
print("the different values of the two numbers is : \n")
print("the frist number is = "+str(frist_number))
print("the second number is = "+str(second_number))
if(((frist_number > 0) and (frist_number < 50)) and ((second_number < 0) and (second_number > -20))) :
    sum_of_two_numbers = frist_number + second_number 
    print("the sum of the frist number , and second number is = "+str(sum_of_two_numbers))
else :
    print("please enter a valid to numbers , there is no sum of the two numbers")