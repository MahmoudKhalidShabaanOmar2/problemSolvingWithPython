# write a python program to get name of the student , if student name is "xyz" then do not allow him to take addmission =>
student_name = input("please enter the name of the student is : ")
print("the name of the student is : \""+student_name+"\"")
if(student_name == "XYZ" or student_name == "xyz") :
    print("good luck , you can not take addmission , because your entered student name is : \""+student_name+"\" , and please enter one of the valid student name like \"mahmoud\"")
else :
    print("congratulations , you can take addmission , because your entered student name is : \""+student_name+"\"")