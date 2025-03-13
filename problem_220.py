# write a python program to find scholarship for student in addmission in a college on the basis student marks by using functions methods => follow this criteria =>
# student marks == 1100 => free education 
# student_marks > 1000 => 80% monthly fees deduction
# student_marks > 900  => 60% monthly fees deduction
# student_marks > 800  => 40% monthly fees deduction
# student_marks > 700  => 30% monthly fees deduction
# student_marks > 600  => there is no scholarship
# def get_monthly_fees_education(stud_mark) : 
#     print("the total marks of the student is = "+str(stud_mark)+" marks")
#     if(stud_mark == 1100) :
#         return("congratulations , you have free education")
#     elif(stud_mark > 1000) :
#         return("congratulations , you have 80% monthly fees deduction")
#     elif(stud_mark > 900) :
#         return("congratulations , you have 60% monthly fees deduction")
#     elif(stud_mark > 800) :
#         return("congratulations , you have 40% monthly fees deduction")
#     elif(stud_mark > 700) :
#         return("congratulations , you have 30% monthly fees deduction")
#     elif(stud_mark > 600) :
#         return("good luck , there is no sholarship")
#     else :
#         return("please enter a valid total marks of the student")
# student_marks = int(input("please enter the total marks of the student is = "))
# fees_education = get_monthly_fees_education(student_marks)
# print(fees_education)

student_marks = int(input("please enter the total marks of the student is = "))
def get_monthly_fees_education(stud_mark) :
    print("the total marks of the student is = "+str(stud_mark)+" marks")
    if(stud_mark == 1100) :
        print("congratulations , you have free education") 
    elif(stud_mark > 1000) :
        print("congratulations , you have 80% monthly fees deduction")
    elif(stud_mark > 900) :
        print("congratulations , you have 60% monthly fees deduction")
    elif(stud_mark > 800) :
        print("congratulations , you have 40% monthly fees deduction")
    elif(stud_mark > 700) :
        print("congratulations , you have 30% monthlt fees deduction")
    elif(stud_mark > 600) :
        print("good luck , there is no scholarship")
    else :
        print("please enter a valid total marks of the student")
get_monthly_fees_education(student_marks)
        