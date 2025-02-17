# write a python program to get total marks of the student if total marks less than 40 , it display "fail" otherwise display "pass" =>
student_marks = float(input("please enter the total marks of the student is = "))
if(student_marks >= 40) :
    print("congratulations , you pass , because your marks of the student is = "+str(student_marks)+" marks")
else :
    print("good luck , you fail , because your your marks of the student is = "+str(student_marks)+" marks , and you need "+str(40 - student_marks)+" marks to pass in this subject")