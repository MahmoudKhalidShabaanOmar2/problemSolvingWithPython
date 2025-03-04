# write a python program to convert from decimal number to binary_number by using different functions methods => 
# decimal_number = int(input("please enter the decimal number is = "))
# binary_number = ""
# def get_binary_number_from_decimal_number(dec_num , bin_num) :
#     print("the decimal number is = "+str(dec_num)+"D")
#     if (dec_num == 0) :
#         bin_num = "0"
#         print("the binary number is = "+bin_num+"B")
#     else :
#         while (dec_num > 0) :
#             remainder = dec_num % 2 
#             bin_num = str(remainder) + bin_num 
#             dec_num //= 2
#         print("the binary number is = "+str(bin_num)+"B")
# get_binary_number_from_decimal_number(decimal_number , binary_number)
        
# def get_binary_number_from_decimal_number(dec_num , bin_num) :
#     print("the decimal number is = "+str(dec_num)+"D")
#     if(dec_num == "0") :
#         bin_num = 0 
#         return("the binary number is = "+str(bin_num)+"B")
#     else :
#         while(dec_num > 0) :
#             remainder = dec_num % 2
#             bin_num = str(remainder) + bin_num 
#             dec_num //= 2
#         return("the binary number is = "+str(bin_num)+"B")
# decimal_number = int(input("please enter the decimal number is = "))
# binary_number = ""
# binary_number_from_decimal_number = get_binary_number_from_decimal_number(decimal_number , binary_number)
# print(binary_number_from_decimal_number)

# decimal_number = int(input("please enter the decimal number is = "))
# def get_binary_number_from_decimal_number(dec_num) :
#     print("the decimal number is = "+str(dec_num)+"D")
#     # binary_number = bin(dec_num)[2:]
#     binary_number = format(dec_num , "b")
#     print("the binary number is = "+binary_number+"B")
# get_binary_number_from_decimal_number(decimal_number)

# def get_binary_number_from_decimal_number(dec_num) :
#     print("the decimal number is = "+str(dec_num)+"D")
#     # binary_number = format(dec_num , "b")
#     binary_number = bin(dec_num)[2:]
#     return("the binary number is = "+str(binary_number)+"B")
# decimal_number = int(input("please enter the decimal number is = "))
# bin_num_from_dec_num = get_binary_number_from_decimal_number(decimal_number)
# print(bin_num_from_dec_num)

# decimal_number = int(input("please enter the decimal number is = "))
# binary_number = ""
# def get_binary_number_from_decimal_number(dec_num , bin_num) :
#     print("the decimal number is = "+str(dec_num)+"D")
#     if(dec_num >= 0) :
#         # bin_num = format(dec_num , "b")
#         bin_num = bin(dec_num)[2:]
#         print("the binary number is = "+bin_num+"B")
#     else :
#         print("please enter valid decimal number to get the binary number")
# get_binary_number_from_decimal_number(decimal_number , binary_number)

def get_binary_number_from_decimal_number(dec_num , bin_num) :
    print("the decimal number is = "+str(dec_num))
    if(dec_num >= 0) :
        # bin_num = format(dec_num , "b") 
        bin_num = bin(dec_num)[2:]
        return("the binary number is = "+bin_num+"B")
    else :
        return("please enter valid decimal number to get the binary number of this decimal number")
decimal_number = int(input("please enter the decimal number is = "))
binary_number = ""
bin_num_from_dec_num = get_binary_number_from_decimal_number(decimal_number , binary_number)
print(bin_num_from_dec_num)