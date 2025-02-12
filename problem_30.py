# write a python program to get the two tables of the two different numbers =>
frist_number = int(input("please enter the frist number is = "))
second_number = int(input("please enter the second number is = "))
print("the frist number is = "+str(frist_number))
print("generating the table of the frist number is : \n")
for fri_num in range(1 , 11) :
    print(str(fri_num)+" * "+str(frist_number)+" = "+str(fri_num * frist_number))
print("the second number is = "+str(second_number))
print("generating the table of the second number is : \n")
for sec_num in range(1 , 11) :
    print(str(sec_num)+" * "+str(second_number)+" = "+str(sec_num * second_number))