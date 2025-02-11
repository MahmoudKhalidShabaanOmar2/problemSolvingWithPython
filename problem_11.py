# write a python program to get student name , and student total marks from the user , and check if student total marks is grater than , or equal to 60 , you can take addmission in the college =>
student_name = input("please enter the name of the student is : ")
student_total_marks = float(input("please enter the total marks of the student is = "))
print("the name of the student is : \""+student_name+"\"")
print("the total marks of the student is = \""+str(student_total_marks)+" marks")
if(student_total_marks >= 60) :
    print("HI \""+student_name+"\" , you can take addmission in the college , because the total marks of the student is = \""+str(student_total_marks)+" marks\"")
else :
    print("SORRY \""+student_name+"\" , you can not take addmission in the college , because the total marks of the student is = \""+str(student_total_marks)+" marks\" , and you need \""+str(60 - student_total_marks)+"\" marks to take addmission in the college")