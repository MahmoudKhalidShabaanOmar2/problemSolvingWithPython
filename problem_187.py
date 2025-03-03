# write a python program to get number from the user , and then get the factorial of the number without using factorial() function =>
# number = int(input("please enter the number is = "))
# print("the number is = "+str(number))
# factorial_of_number = 1 
# for num in range(1 , number + 1) :
#     factorial_of_number *= num 
# print("the factorial of the number is = "+str(factorial_of_number))

number = int(input("please enter the number is = "))
print("the number is = "+str(number))
num = number 
factorial_of_number = 1 
while num > 1 :
    factorial_of_number *= num 
    num -= 1
print("the factorial of the number is = "+str(factorial_of_number))