# write a python program to get student name , and five student subjects from the user in array , and then find the total marks of the all subjects , and then display marks of the all subjects =>
# import array as arr 
# array_of_subjects_marks = arr . array("i" , [])
# array_of_subjects_marks = []
# for i in range(5) :
    # array_of_subjects_marks . append(int(input("please enter the marks of the all subjects to store in the array of the student subjects marks is = ")))
array_of_subjects_marks = [int(input("please enter the marks of the all subjects to store in the array of the student subjects marks is = ")) for i in range(5)]
student_name = input("please enter the name of the student is : ")
print("the marks of the all subjects of the student is : ")
total_marks_of_all_subjects = 0
for marks in range(5) :
    print(str(array_of_subjects_marks[marks])+" marks")
    total_marks_of_all_subjects += array_of_subjects_marks[marks]
print("Hi \""+student_name+"\"")
print("the marks of the introduction to programming is = \'"+str(array_of_subjects_marks[0])+" marks\'")
print("the marks of the introduction to computer science is = \'"+str(array_of_subjects_marks[1])+" marks\'")
print("the marks of the mathmaticas is = \'"+str(array_of_subjects_marks[2])+" marks\'")
print("the marks of the digital system is = \'"+str(array_of_subjects_marks[3])+" marks\'")
print("the marks of the physics is = "+str(array_of_subjects_marks[4])+" marks\'")
print("the total marks of the all subects is = "+str(total_marks_of_all_subjects)+" marks\'")
