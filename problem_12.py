# write a python program to get student name , and student total marks from the user , and check if student total marks is grater than , or equal to 60 , you can take addmission in the college by using function =>
# student_name = input("please enter the name of the student is : ")
# student_total_marks = float(input("please enter the total marks of the student is = "))
# def check_addmission_in_college(stud_name , stud_marks) :
#     print("the name of the student is : \""+stud_name+"\"")
#     print("the total marks of the student is = \""+str(stud_marks)+" marks\"")
#     if(stud_marks >= 60) :
#         print("HI \""+stud_name+"\" you can take addmission in the college , because the total marks of the student is = \""+str(stud_marks)+" marks\"")
#     else :
#         print("SORRY \""+stud_name+"\" you can not take addmission in the college , because the total marks of the student is = \""+str(stud_marks)+" marks\" , and you need \""+str(60 - stud_marks)+" marks\" to take addmission in the college")
# check_addmission_in_college(student_name , student_total_marks)

def check_addmission_in_college(stud_name , stud_marks) :
    print("the name of the student is : \""+stud_name+"\"")
    print("the total marks of the student is : \""+str(stud_marks)+"\"")
    if(stud_marks >= 60) :
        return("HI \""+stud_name+"\" , you can take addmission in the college , because the total marks of the student is = \""+str(stud_marks)+"\"")
    else :
        return("SORRY \""+stud_name+"\" , you can not take addmission in the college , because the total marks of the student is = \""+str(stud_marks)+" marks\" , and you need \""+str(60 - stud_marks)+" marks\" to take addmission in the college")
student_name = input("please enter the name of the student is : ")
student_total_marks = float(input("please enter the total marks of the student is = "))
addmission_in_college = check_addmission_in_college(student_name , student_total_marks)
print(addmission_in_college)