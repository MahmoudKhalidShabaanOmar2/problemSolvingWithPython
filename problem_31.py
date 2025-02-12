# write a python program to get the table of the two different numbers by using function =>
# frist_number = int(input("please enter the frist number is = "))
# second_number = int(input("please enter the second number is = "))
# def get_table_of_two_numbers(fri_num , sec_num) :
#     print("the frist number is = "+str(fri_num))
#     print("generating the table of the frist number is : \n")
#     for x in range(1 , 11) :
#         print(str(x)+" * "+str(fri_num)+" = "+str(x * fri_num))
#     print("\n")
#     print("the second number is = "+str(sec_num))
#     print("generating table of the second number is : \n")
#     for y in range(1 , 11) :
#         print(str(y)+" * "+str(sec_num)+" = "+str(y * sec_num))
# get_table_of_two_numbers(frist_number , second_number)

def get_table_of_two_numbers(fri_num , sec_num) :
        print("the frist number is = "+str(fri_num))
        print("generating the table of the frist number is : \n")
        for x in range(1 , 11) :
            print(str(x)+" * "+str(fri_num)+" = "+str(x * fri_num)) 
        print("the second number is = "+str(sec_num))
        print("generating the table of the second number is : \n")
        for y in range(1 , 11) :
            print(str(y)+" * "+str(sec_num)+" = "+str(y * sec_num))
        return(" ")
frist_number = int(input("please enter the frist number is = "))
second_number = int(input("please enter the second number is = "))
different_tables = get_table_of_two_numbers(frist_number , second_number)
print(different_tables)