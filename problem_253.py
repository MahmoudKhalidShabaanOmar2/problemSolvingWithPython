# # write a python program to get list of the different student marks , and then displaying student marks , and student names is : 
lista_of_different_students_names_with_marks = []
numbers_of_students = int(input("Please Enter The Number Of Students Is = "))
for i in range(numbers_of_students) :
    student_names = input("Please Enter The Name Of The Students Is = ")
    student_marks = int(input("Please Enter The Total Marks Of The Student Is = "))
    lista_of_different_students_names_with_marks . append({f"The Name Of The Student Is : " : student_names , "The Total Marks Of The Student Is = " : student_marks})
    print(list(lista_of_different_students_names_with_marks))