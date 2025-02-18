# write a python program to get year number from the user , and then check it is a leap year , or not leap year =>
year_num = int(input("please enter the number of the year is = "))
print("the year number is = "+str(year_num))
if(year_num %4 == 0) :
    print("OKAY , it is a leap year , because your entered year number is = "+str(year_num)+" , and the modulus of the year number by four is = "+str(year_num % 4))
else :
    print("SORRY , it is not a leap year , because your entered year number is = "+str(year_num)+" , and the modulus of the year number by four is = "+str(year_num % 4))