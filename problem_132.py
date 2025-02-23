# write a python program to get student name , and student age from the user , and then make sure that username only contains alphnumeric character to take addmission in the shcool if student age is grater than , or equal to five , and make sure that the length of the student name is less than , or equal to eight by using different function methods =>
# student_name = input("please enter the name of the student is : ")
# student_age = int(input("please enter the age of the student is : "))
# def check_student_addmission_in_school(stud_name , stud_age) :
#     print("the name of the student is : \""+stud_name+"\"")
#     print("the age of the student is : \""+str(stud_age)+"\"")
#     if((stud_name . isalnum()) and (len(stud_name) <= 8) and (stud_age >= 5)) :
#         print("Okay , your entered student name is \"OKAY\" , because your entered student name is \""+stud_name+"\" , because student name only contains alphabetic characters , and numeric characters , and it does not container special characters , and the length of the characters of the student name is = \""+str(len(stud_name))+" characters\" , and the age of the student is = \""+str(stud_age)+"\" , and then you can take addmission in the school")
#     else :
#         print("Sorry , because your entered student name is \"NOT OKAY\" , because your entered student name is \""+stud_name+"\" , because student name does not only contain alphabetic characters , or numeric characters , and also contains special characters , and the length of the characters of the student name is = \""+str(len(stud_name))+" character , and the age of the student is = \""+str(stud_age)+" years\" , and then you can not take addmission in the school")
# check_student_addmission_in_school(student_name , student_age)

def check_student_addmission_in_school(stud_name , stud_age) :
    print("the name of the student is : \""+stud_name+"\"")
    print("the age of the student is = \""+str(stud_age)+" years\"")
    if((stud_name . isalnum()) and (len(stud_name) <= 8 ) and (stud_age >= 5)) :
        return("Okay , your entered student name is \"OKAY\" , because your entered student name is : \""+stud_name+"\" , because student name only contains alphabetic characters , or numeric characters , and it does not containe special characters , and the length of the characters of the student name is = \""+str(len(stud_name))+" characters\" , and the age of the student is = \""+str(stud_age)+"\" , and then you can not take addmission in the college")
    else :
        return("Sorry , your entered student name is \"NOT OKAY\" , because your entered student name is : \""+stud_name+"\" , because student name only contains alphabetic characters , or numeric characters , and student name also contains special characters , and the length of the characters of the student name is = \""+str(len(stud_name))+" characters\" , and the age of the student is = \""+str(stud_age)+" years\" , and then you can not take addmission in the college")
student_name = input("please enter the name of the student is : ")
student_age = float(input("please enter the age of the student is = "))
check_student_addmission = check_student_addmission_in_school(student_name , student_age)
print(check_student_addmission)
