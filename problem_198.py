# write a python program to convert from binary to decimal number by using function methods =>
# binary_number = input("please enter the binary number is = ")
# decimal_number = 0
# def get_decimal_number_from_binary_number(bin_num , dec_num) :
#     print("the binary number is = "+str(bin_num)+"B")
#     for num in range(len(bin_num)) :
#         dec_num += int(bin_num[-(num + 1)]) * (2 ** num)
#     print("the decimal number is = "+str(dec_num)+"D") 
# get_decimal_number_from_binary_number(binary_number , decimal_number)
    
# def get_decimal_number_from_binary_number(bin_num , dec_num) :
#     print("the binary number is = "+str(bin_num)+"B")
#     for num in range(len(bin_num)) :
#         dec_num += int(bin_num[-(num + 1)]) * (2 ** num)
#     return("the decimal number is = "+str(dec_num)+"D")
# binary_number = input("please enter the binary number is = ")
# decimal_number = 0 
# binary_number_from_decimal_number = get_decimal_number_from_binary_number(binary_number , decimal_number)
# print(binary_number_from_decimal_number)

# binary_number = input("please enter the binary number is = ")
# decimal_number = 0 
# def get_decimal_number_from_binary_number(bin_num , dec_num) :
#     print("the binary number is = "+str(bin_num)+"B")
#     dec_num = int(bin_num , 2)
#     print("the decimal number is = "+str(dec_num)+"D")
# get_decimal_number_from_binary_number(binary_number , decimal_number)

def get_decimal_number_from_binary_number(bin_num , dec_num) :
    print("the binary number is = "+bin_num+"B")    
    dec_num = int(bin_num , 2)
    return("the decimal number is = "+str(dec_num)+"D")
binary_number = input("please enter the binary number is = ")
decimal_number = 0 
decimal_number_from_binary_number = get_decimal_number_from_binary_number(binary_number , decimal_number)
print(decimal_number_from_binary_number)