# write a python program to get number from the user , and then check number wether it is a positive , negative , or equal to zero =>
num = float(input("please enter the number is = "))
print("the number is = "+str(num))
if(num > 0) :
    print("it is a positive number , because your entered number is = "+str(num))
elif(num == 0) :
    print("it is equal to zero , because your entered number is = "+str(num))
else :
    print("it is a negative number , because your entered number is = "+str(num))
