# write a python program to get student name , and student age from the user , and then make sure that username only contains alphnumeric character to take addmission in the shcool if student age is grater than , or equal to five =>
student_name = input("please enter the name of the student is : ")
student_age = float(input("please enter the age of the student is = "))
print("the name of the student is : \""+student_name+"\"")
print("the student age is = \""+str(student_age)+" years\"")
if((student_name . isalnum()) and (student_age >= 5)) :
    print("Okay , your entered student name is \"OKAY\" , because your entered name is : \""+student_name+"\" , and student name only contains alphabetic , or numeric characters , and it does not container special character , and you can take addmission in the shcool , because your entered student age is = "+str(student_age))
else :
    print("Sorry , your entered student name is \"NOT OKAY\" , because your entered name is : \""+student_name+"\" , and student name does not only contain alphabtic , and numeric characerts , and also container special characters , and you can not take addmission in the shcool , because your entered student age is = "+str(student_age)+" , and you need "+str(5 - student_age)+" years to take addmission in the college")