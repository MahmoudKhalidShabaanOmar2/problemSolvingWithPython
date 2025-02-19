# write a python program to get student marks from the user , and then display the student grade by using function methods using this criteria =>
# student_marks >= 95 , A+ grade 
# student_marks >= 80 , A grade
# student_marks >= 70 , B grade 
# student_marks >= 60 , C grade
# student_marks , lower than 60 F grade
# def get_student_grade(stud_marks) :
#     print("the student marks is = \""+str(stud_marks)+"\"")
#     if(stud_marks >= 95) :
#         return("your grade is \"A+\" , because your student marks is = \""+str(stud_marks)+" marks\"")
#     elif(stud_marks >= 80) :
#         return("your grade is \"A\" , because your student marks is = \""+str(stud_marks)+" marks\"")
#     elif(stud_marks >= 70) :
#         return("your grade is \"B\" , because your student marks is = \""+str(stud_marks)+" marks\"")
#     elif(stud_marks >= 60) :
#         return("your grade is \"C\" , because your student marks is = \""+str(stud_marks)+" marks\"")
#     else :
#         return("your grade is \"F\" , because your student marks is = \""+str(stud_marks)+" marks\" , and you need \""+str(60 - stud_marks)+" marks\" to pass in all subjects")
# student_marks = int(input("please enter the student marks is = "))
# get_grade = get_student_grade(student_marks)
# print(get_grade)

student_marks = int(input("please enter the student marks is = "))
def get_student_grade(stud_marks) :
    print("the student marks is = \""+str(stud_marks)+" marks\"")
    if(stud_marks >= 95) :
        print("your grade is \"A+\" , because your student marks is = \""+str(stud_marks)+" marks\"")
    elif(stud_marks >= 80) :
        print("your grade is \"A\" , because your student marks is = \""+str(stud_marks)+" marks\"")
    elif(stud_marks >= 70) :
        print("your grade is \"B\" , because your student marks is = \""+str(stud_marks)+" marks\"")
    elif(stud_marks >= 60) :
        print("your grade is \"C\" , because your student marks is = \""+str(stud_marks)+" marks\"")
    else :
        print("your grade is \"F\" , because your student marks is = \""+str(stud_marks)+" marks\" , and you need \""+str(60 - stud_marks)+" marks\" to pass in all subjects")
get_student_grade(student_marks)