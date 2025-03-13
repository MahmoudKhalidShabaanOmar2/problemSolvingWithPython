# write a python program to find scholarship for student in addmission in the college on the basis of the student marks => 
# follow this criteria =>
# student_marks = 1100 => free education 
# student_marks > 1000 => 80% monthly fees deduction
# student_marks > 900  => 60% monthly fees deduction
# student_marks > 800  => 40% monthly fees deduction 
# student_marks > 700  => 30% monthly fees deduction 
# student_marks > 600  => there is no scholarship
student_marks = int(input("please enter the total marks of the student is = "))
if(student_marks == 1100) :
    print("congratulations , you have free education")
elif(student_marks > 1000) :
    print("congratulations , you have 80% monthly fees deduction")
elif(student_marks > 900) :
    print("congratulations , you have 60% monthly fees deduction")
elif(student_marks > 800) :
    print("congratulations , you have 40% monthly fees deduction")
elif(student_marks > 700) :
    print("congratulations , you have 30% monthly fees deduction")
elif(student_marks > 600) :
    print("good luck , there is no scholarship")
else :
    print("please enter a valid total student marks")