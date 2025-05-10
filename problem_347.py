# write a python program to get number from the user , and then get the next number , and then get the sum of the number , and next number , and then get the previous of the number , and then get the sum of the number , and previous number , and at the end get the sum of the next number , and previous number by using function method =>
number = int(input("Please Enter The Number Is = "))
def get_previous_next_number(num) :
    print("The Number Is = ",str(num))
    previous_number = num - 1
    print("The Previous Number Is = ",str(previous_number))
    sum_of_number_previous_number = num + previous_number 
    print("The Sum Of The Number , And Previous Number Is = ",str(sum_of_number_previous_number))
    next_number = num + 1 
    print("The Next Number Is = ",str(next_number))
    sum_of_number_next_number = num + next_number 
    print("The Sum Of The Number , And Next Number Is = ",str(sum_of_number_next_number))
get_previous_next_number(number)