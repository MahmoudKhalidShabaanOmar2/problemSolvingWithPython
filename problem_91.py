# write a python program to get student marks from the user , and then display the student grade using this criteria =>
# student_marks >= 95 , A+ grade 
# student_marks >= 80 , A grade
# student_marks >= 70 , B grade 
# student_marks >= 60 , C grade
# student_marks , lower than 60 F grade
student_marks = float(input("please enter the marks of the student is = "))
print("the student marks is = \""+str(student_marks)+" marks\"")
if(student_marks >= 95) :
    print("your grade is \"A+\" , because your student marks is = \""+student_marks+" marks\"")
elif(student_marks >= 80) :
    print("your grade is \"A\" , because your student marks is = \""+str(student_marks)+" marks\"")
elif(student_marks >= 70) :
    print("your grade is \"B\" , because your student marks is = \""+str(student_marks)+" marks\"")
elif(student_marks >= 60) :
    print("your grade is \"C\" , because your student marks is = \""+str(student_marks)+" marks\"")
else :
    print("your grade is \"F\" , because your student marks is = \""+str(student_marks)+" marks\" , and you need \""+str(60 - student_marks)+" marks\" to pass in all subjects")