# write a python program to create a file , and then get number from the user , and then do all assignment operations on this number by using function method =>
createFile = open("getAllAssignmentOperationsOnTwoNumbers.txt" , "w+")
number = int(input("please enter the number is = "))
def getAllAssignmentOperationsOnNumber(cFile , num) :
    cFile.write("The Number Is = "+str(num)+"\n") 
    num += 10
    cFile.write("The Result Of The Addition Assignment Operation Is = "+str(num)+"\n")
    num -= 10
    cFile.write("The Result Of The Subtraction Assignment Operation Is = "+str(num)+"\n")
    num *= 10
    cFile.write("The Result Of The Multiplication Assignment Operation Is = "+str(num)+"\n")
    num /= 10
    cFile.write("The Result Of The Division Assignment Operation Is = "+str(num)+"\n")
    num %= 10 
    cFile.write("The Result Of The Modulus Assignment Operation Is = "+str(num)+"\n")
    num **= 10 
    cFile.write("The result Of The Square Assignment Operation Is = "+str(num)+"\n")
    cFile.close()
getAllAssignmentOperationsOnNumber(createFile , number)