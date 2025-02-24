# write a python program to get starting number , and ending number from the user as input , and then generate all numbers in the properly sequence by using function method =>
starting_number = int(input("please enter the starting number is = "))
ending_number = int(input("please enter the ending number is = "))
def generate_all_numbers_from_starting_to_ending_number(start_num , end_num) :
    print("the starting number is = \" "+str(start_num)+" \"")
    print("the ending number is = \" "+str(end_num)+" \"")
    print("generating all numbers from starting number is = \" "+str(start_num)+" \" to the ending number is = \""+str(end_num)+" \" in the properly(ascending) sequence is : ")
    for num in range(start_num , end_num + 1) :
        print(num)
generate_all_numbers_from_starting_to_ending_number(starting_number , ending_number)
        