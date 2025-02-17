# write a python program to get number from the user , and then check that it is an even , or odd number and then find that number square =>
num = int(input("please enter the number is = "))
print("the number is = "+str(num))
if(num %2 == 0) :
    # print("it is an even number , because your entered number is = "+str(num)+" , the modulus of the number by two is = "+str(num % 2)+" , and the square of the number is = "+str(num * num))
    # print("it is an even number , because your entered number is = "+str(num)+" , the modulus of the number by two is = "+str(num % 2)+" , and the square of the number is = "+str(num ** 2))
    print("it is an even number , because your entered number is = "+str(num)+" , the modulus of the number by two is = "+str(num % 2)+" , and the square of the number is = "+str(pow(num , 2)))
else :
    # print("it is an odd number , because your entered number is = "+str(num)+" the modulus of the number is = "+str(num)+" the modulus of the number by two is = "+str(num % 2)+", and the square of the number is = "+str(num * num))
    # print("it is an odd number , because your entered number is = "+str(num)+" , the modulus of the number by two is = "+str(num & 2)+" , and the square of the number is = "+str(num ** 2))
    print("it is an odd number , because your entered number is = "+str(num)+" , the modulus of the number by two is = "+str(num % 2)+" , and the square of the number is = "+str(pow(num , 2)))