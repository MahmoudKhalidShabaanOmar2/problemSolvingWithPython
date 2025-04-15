# write a python program to get student name with student marks in a list , and then display student name with student marks By Using Function Method=>
# lista_of_student_name_with_marks = []
# numbers_of_students = int(input("Please Enter The Number Of The Students Is = "))
# for i in range(numbers_of_students) :
#     print(f"Please Enter Different Information Of The Student {i + 1} Is : ")
#     student_name = input(f"Please Enter The Name Of The Student {i + 1} Is : ")
#     student_marks = int(input(f"Please Enter The Total Marks Of The Student {i + 1} Is = "))
#     student_information = {"student_name" : student_name , "student_marks" : student_marks}
#     lista_of_student_name_with_marks.append(student_information)
# def get_lista_of_student_name_with_marks(list_of_stud_name_with_marks) :
#     print("\nThe List Of The Student Name With Student Marks Is : \n")
#     for student in list_of_stud_name_with_marks :
#         print(f"The Name Of The Student Is : {student['student_name']} , And The Total Marks Of The Student Is = {student['student_marks']} Marks")
# get_lista_of_student_name_with_marks(lista_of_student_name_with_marks)

def get_lista_of_student_name_with_marks(list_of_stud_name_with_marks) :
    print("\nThe List Of The Student Name With Student Marks Is : \n")
    for student in list_of_stud_name_with_marks :
        print(f"The Name Of The Student Is : {student['student_name']} , And The Total Marks Of The Student Is = {student['student_marks']} Marks")
    return("")
lista_of_student_name_with_marks = []
numbers_of_students = int(input("Please Enter The Number Of The Students Is = "))
for i in range(numbers_of_students) :
    student_name = input("Please Enter The Name Of The Student Is : ")
    student_marks = int(input("Please Enter The Total Marks Of The Student Is = "))
    student_information = {"student_name" : student_name , "student_marks" : student_marks}
    lista_of_student_name_with_marks.append(student_information)
displaying_list_of_student_name_with_marks = get_lista_of_student_name_with_marks(lista_of_student_name_with_marks)
print(displaying_list_of_student_name_with_marks)        