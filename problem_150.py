# write a python program to get student name , and five student subjects from the user in array , and then find the total marks of the all subjects , find average of the total marks of the all subjects also , and then display marks of the all subjects =>
import array as arr 
array_of_subjects_marks = arr . array("i" , [])
for i in  range(5) :
    array_of_subjects_marks . append(int(input("please enter the all marks of the all subjects to store in the array of the all subjects marks is = ")))
student_name = input("please enter the name of the student is : ")
print("the marks of the all subjects of the student is : ")
sum_of_total_marks_of_all_subjects = 0 
for marks in range(5) :
    print(str(array_of_subjects_marks[marks])+" marks")
    sum_of_total_marks_of_all_subjects += array_of_subjects_marks[marks]
print("HI \""+student_name+"\"")
print("the marks of the introduction to programming is = \'"+str(array_of_subjects_marks[0])+" marks\'")
print("the marks of the introduction to computer science is = \'"+str(array_of_subjects_marks[1])+" marks\'")
print("the marks of the digital ssystem is = \'"+str(array_of_subjects_marks[2])+" marks\'")
print("the marks of the mathmaticas is = \'"+str(array_of_subjects_marks[3])+" marks\'")
print("the marks of the physics is = \'"+str(array_of_subjects_marks[4])+" marks\'")
print("the total marks of the all subjects is = \'"+str(sum_of_total_marks_of_all_subjects)+" marks\'")
average_of_total_marks_of_all_subjects = sum_of_total_marks_of_all_subjects / 5 
print("the average of the total marks of the all subjects is = \'"+str(average_of_total_marks_of_all_subjects)+" marks\'")