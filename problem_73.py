# write a python program to get number from the user , and then check that it is an even , or odd number =>
num = int(input("please enter the number is = "))
print("the number is = "+str(num))
if(num %2 == 0) :
    print("it is even number , because your entered number is = "+str(num)+" , and the modulus of the number by two is = "+str(num % 2))
else :
    print("it is odd number , because your entered number is = "+str(num)+" , and the modulus of the number by two is = "+str(num % 2))