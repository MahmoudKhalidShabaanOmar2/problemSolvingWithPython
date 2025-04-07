# write a python program to create file , and then get two numbers from the user , and then get all arthimetic operations on the two numbers =>
createFile = open("getAllArthimeticOperationsOntwoNumbers.txt" , "w+")
fristNumber = int(input("please enter the frist number is = "))
secondNumber = int(input("please enter the second number is = "))
def getAllArthimeticOperationsOnTwoNumbers(cFile , friNum , secNum) :
    cFile.write("The Frist Number Is = "+str(friNum)+"\n")
    cFile.write("The Second Number Is = "+str(secNum)+"\n")
    addition_of_nums = friNum + secNum 
    cFile.write("The Addition Of The Numbers Is = "+str(addition_of_nums)+"\n")
    subtraction_of_nums = friNum - secNum 
    cFile.write("The Subtraction Of The Numbers Is = "+str(subtraction_of_nums)+"\n")
    multiplication_of_nums = friNum * secNum 
    cFile.write("The Multiplication Of The Numbers Is = "+str(multiplication_of_nums)+"\n")
    division_of_nums = friNum / secNum 
    cFile.write("The Division Of The Numbers Is = "+str(division_of_nums)+"\n")
    modulus_of_nums = friNum % secNum 
    cFile.write("The Modulus Of The Numbers Is = "+str(modulus_of_nums)+"\n")
getAllArthimeticOperationsOnTwoNumbers(createFile , fristNumber , secondNumber)