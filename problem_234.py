# write a python program to read an exisiting file , and get two numbers from the user , and then get the sum , subtraction , multiplication , division , and at the end modulus between thw two numbers => 
fristNumber = float(input("please enter the frist number is = "))
secondNumber = float(input("please enter the second number is = "))
createFile = open("arthimeticOperationsOfTwoNumbers.txt" , "w+")
createFile.write("The Frist Number Is = "+str(fristNumber))
createFile.write("The Second Number Is = "+str(secondNumber))
sum_of_nums = fristNumber + secondNumber 
createFile.write("The Sum Of The Two Numbers Is = "+str(sum_of_nums))
sub_of_nums = fristNumber - secondNumber 
createFile.write("The Subtraction Of The Two Numbers Is = "+str(sub_of_nums))
mul_of_nums = fristNumber * secondNumber 
createFile.write("The Multiplication Of The Two Numbers Is = "+str(mul_of_nums))
div_of_nums = fristNumber / secondNumber 
createFile.write("The Division Of The Two Numbers Is = "+str(div_of_nums))
mod_of_nums = fristNumber % secondNumber 
createFile.write("The Modulus Of The Two Numbers Is = "+str(mod_of_nums))