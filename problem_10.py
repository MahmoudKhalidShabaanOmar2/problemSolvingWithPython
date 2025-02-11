# write a python program to get student name , and student age from the user to check wether it is able to take participation in the votting , or not if student age is grater than , or equal to 18 years then you can take participation in the votting , and else you can not take participation in the votting using function methods=>
# student_name = input("please enter the name of the student is : ")
# student_age = float(input("please enter the age of the student is = "))
# def check_participation_in_votting(stud_name , stud_age) :
#     print("the name of the student is : \""+stud_name+"\"")
#     print("the age of the student is \""+str(stud_age)+" years\"")
#     if(stud_age >= 18) :
#         print("HI \""+stud_name+"\" , you can take participation in the votting , because the age of the student is = \""+str(stud_age)+" years\"")
#     else :
#         print("SORRY \""+stud_name+"\" , you can not take participation in the votting , because the age of the student is = \""+str(stud_age)+" years\" , and you need "+str(18 - stud_age)+" years\" to take participation in the votting")
# check_participation_in_votting(student_name , student_age)

def check_participation_in_votting(stud_name , stud_age) :
    print("the name of the student is \""+stud_name+"\"")
    print("the age of the student is = \""+str(stud_age)+" years\"")
    if(stud_age >= 18) :
        return("HI \""+stud_name+"\" , you can take participation in the votting , because the age of the student is = \""+str(stud_age)+" years\"")
    else :
        return("SORRY \""+stud_name+"\" , you can not take participation in the votting , because the age of the student is = \""+str(stud_age)+" years\" , and you need "+str(18 - stud_age)+" to take participation in the votting")
student_name = input("please enter the name of the stduent is : ")
student_age = float(input("please enter the age of the student is = "))
participation_in_votting = check_participation_in_votting(student_name , student_age)
print(participation_in_votting)