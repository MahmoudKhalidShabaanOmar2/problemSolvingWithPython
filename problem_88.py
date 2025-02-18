# write a python program to get number from the user , and then check that it is divisible by five , or six , or not =>
num = int(input("please enter the number is = "))
print("the number is = "+str(num))
if((num %5 == 0) and (num %6 == 0)) :
    print("it is divisible by five , and six , because your entered number is = "+str(num)+" , and the modulus of the number by five is = "+str(num % 5)+" , and the modulus of the number by six is = "+str(num % 6))
else :
    print("it is not divisible by five , or six because your entered number is = "+str(num)+" , and the modulus of the number by five is = "+str(num % 5)+" , or the modulus of the number by six is = "+str(num % 6))