# write a python program to convert from binary number to decimal number =>
# binary_number = input("please enter the binary number is = ")
# print("the binary number is = "+binary_number+"B")
# decimal_number = 0 
# for num in range(len(binary_number)) :
    # decimal_number += int(binary_number[-(num + 1)]) * (2 ** num)
# print("the decimal number is = "+str(decimal_number)+"D")
    
# binary_number = input("please enter the binary number is = ")
# print("the binary number is = "+str(binary_number)+"B")
# decimal_number = int(binary_number , 2)
# print("the decimal number is = "+str(decimal_number)+"D")

binary_number = input("please enter the binary number is = ")
print("the binary number is = "+str(binary_number)+"B")
decimal_number = 0
for num in range(len(binary_number)) :
    if(binary_number[num] == "0" or binary_number[num] == "1") : 
        decimal_number += 2 ** (len(binary_number) - num - 1)
    print("the decimal number is = "+str(decimal_number)+"D")