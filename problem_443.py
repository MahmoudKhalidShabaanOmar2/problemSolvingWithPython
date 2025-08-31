# write a python program to get number from the user , and then get the previous , and next number by using function =>
number = int(input("Please Enter The Number Is = "))
def getPreviousAndNextNumber(num): 
    print("The Number Is = ",str(num))
    previous_number = num - 1
    print("The Previous Number Is = ",str(previous_number))
    next_number = num + 1
    print("The Next Number Is = ",str(next_number))
getPreviousAndNextNumber(number)