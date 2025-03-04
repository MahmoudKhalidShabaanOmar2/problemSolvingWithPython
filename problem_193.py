# write a python program to get decimal number , and then converted to binary number =>
# decimal_number = int(input("please enter the decimal number is = "))
# print("the decimal number is = "+str(decimal_number)+"D")
# binary_number = ""
# if (decimal_number == 0) :
#     binary_number = "0"
#     print("the binary number is = "+str(binary_number)+"B")
# else :
#     while (decimal_number > 0) :
#         remainder = decimal_number % 2
#         binary_number = str(remainder) + binary_number 
#         decimal_number //= 2
#     print("the binary number is = "+str(binary_number)+"B")

# decimal_number = int(input("please enter the decimal number is = "))
# print("the decimal number is = "+str(decimal_number)+"D")
# binary_number = format(decimal_number , "b")
# print("the binary number is = "+binary_number+"B")

decimal_number = int(input("please enter the decimal number is = "))
print("the decimal number is = "+str(decimal_number)+"D")
binary_number = bin(decimal_number)[2:]
print("the binary number is = "+binary_number+"B")