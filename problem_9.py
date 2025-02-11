# write a python program to get student name , and student age from the user to check wether it is able to take participation in the votting , or not if student age is grater than , or equal to 18 years then you can take participation in the votting , and else you can not take participation in the votting =>
student_name = input("please enter the name of the student is : ")
student_age = float(input("please enter the  age of the student is = "))
print("the name of the student is : \""+student_name+"\"")
print("the total marks of the student is = \""+str(student_age)+"\"")
if(student_age >= 18) :
    print("HI \""+student_name+"\" , you can take participation in the votting , because the age of the student is = \""+str(student_age)+" years\"")
else :
    print("SORRY \""+student_name+"\" , you can not take participation in the votting , because the age of the student is = \""+str(student_age)+" years\" , and you need "+str(18 - student_age)+" years\"")