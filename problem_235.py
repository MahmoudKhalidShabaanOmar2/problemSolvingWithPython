# write a python program to create an exisiting file , get the number from the user , and then do all assignment operations in the number =>
number = int(input("please enter the number is = "))
createFile = open("assignmentOperationsOnNum.txt" , "w+")
createFile.write("The Number Is = "+str(number)+"\n")
number += 5 
createFile.write("The Addition Assignment Operation Of The Number Is = "+str(number)+"\n")
number -= 5
createFile.write("The Subtraction Assignment Operation Of The Number Is = "+str(number)+"\n")
number *= 5 
createFile.write("The Multiplication Assignment Operation Of The Number Is = "+str(number)+"\n")
number /= 5
createFile.write("The Division Assignment Operation Of The Number Is = "+str(number)+"\n")
number %= 5 
createFile.write("The Modulus Assignment Operation Of The Number Is = "+str(number)+"\n")
number **= 5
createFile.write("The Square Assignment Operation Of The Number Is = "+str(number)+"\n")