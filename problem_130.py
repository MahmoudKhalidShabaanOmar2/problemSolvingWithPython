# write a python program to get student name , and student age from the user , and then make sure that username only contains alphnumeric character to take addmission in the shcool if student age is grater than , or equal to five by using different function methods =>
student_name = input("please enter the name of the student is : ")
student_age = float(input("please enter the age of the student is = "))
def check_student_addmission_in_school(stud_name , stud_age) :
    print("the name of the student is : \""+stud_name+"\"")
    print("the age of the student is = \""+str(stud_age)+" years\"")
    if((stud_name . isalnum()) and (stud_age >= 0)) :
        print("Okay , because your entered student name is \"OKAY\" , because your entered student name is : \""+stud_name+"\" , because student name only contains alphabetic characters , or numeric characters , and it does not contain special character , and you can take addmission in the shcool , because your entered student age is = "+str(student_age)+" years")
    else :
        print("Sorry , because your entered student name is \"NOT OKAY\" , because your entered student name is : \""+student_name+"\" , because student name does not only container ")
    