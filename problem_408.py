# write a python program to get the list of the student names , and user can be able to delete any student name from the list of student names by using function method =>
lista_of_student_names = []
for i in range(10):
    student_names = input(f"Please Enter The Student Name ("+str(i+1)+") Is :")
    lista_of_student_names.append(student_names)
def get_list_of_student_names(list_of_stud_names):
    print("The List Of The student Names Is : ",str(list_of_stud_names))
    stud_name = input("Please Enter The student Name Is : ")
    list_of_stud_names.remove(stud_name)
    print("The Updated , Or New List Of The Student Name Is : ",str(list_of_stud_names))
get_list_of_student_names(lista_of_student_names)