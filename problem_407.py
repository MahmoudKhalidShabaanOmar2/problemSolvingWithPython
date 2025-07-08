# write a python program to store a student records , user will be able to delete any student from record on the run time =>
lista_of_student_names = [] 
for i in range(10):
    student_names = input(f"Please Enter The Student Name("+str(i + 1)+") Is : ")
    lista_of_student_names.append(student_names)
print("The List Of The Student Names Is : ",str(lista_of_student_names))
stud_name = input("Please Enter The Student Name Is : ")
lista_of_student_names.remove(stud_name)
print("The Updated , Or New List Of The Student Names Is : ",str(lista_of_student_names))