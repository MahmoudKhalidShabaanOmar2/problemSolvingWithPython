# write a python program to get student name , and student marks in a list , and then display the list of student name with student marks , and at the end display the second student name with student marks By Using Function =>
# lista_of_student_name_with_marks = []
# numbers_of_students = int(input("Please Enter The Numbers Of The Students Is = "))
# for i in range(numbers_of_students) :
#     print(f"\nDifferent Information Of The Student {i + 1} Is : \n")
#     student_name = input(f"Please Enter The Name Of The Student {i + 1} Is : ")
#     student_marks = int(input(f"Please Enter The Total Marks Of The Student {i + 1} Is : "))
#     student_information = {"student_name" : student_name , "student_marks" : student_marks}
#     lista_of_student_name_with_marks . append(student_information)
# def get_lista_of_student_name_with_marks(list_of_stud_name_with_marks) :
#     for student in list_of_stud_name_with_marks : 
#         print(f"The Name Of The Student Is : {student['student_name']} , And The Total Marks Of The Student Is = {student['student_marks']} Marks")
#     if(len(list_of_stud_name_with_marks) >= 2) :
#         second_student_name_with_marks = list_of_stud_name_with_marks[1] 
#         print(f"The Name Of The Student Is : {second_student_name_with_marks['student_name']} , And The Total Marks Of The Student Is = {second_student_name_with_marks['student_marks']} Marks")
#     else :
#         print("There Is No Second Student Name With Student Marks")
# get_lista_of_student_name_with_marks(lista_of_student_name_with_marks)

def get_lista_of_student_name_with_marks(list_of_stud_name_with_marks) :
    for student in list_of_stud_name_with_marks :
        print(f"The Name Of The Student Is : {student['student_name']} , And The Total Marks Of The Student Is = {student['student_marks']} Marks")
    if(len(list_of_stud_name_with_marks) >= 2) :
        second_student_name_with_marks = list_of_stud_name_with_marks[1] 
        return(f"The Name Of The Student Is : {student['student_name']} , And The Total Marks Of The Student Is = {student['student_marks']} Marks")
    else :
        return("There Is No Second Student Name With Student Marks")
    return("")
lista_of_student_name_with_marks = []
numbers_of_students = int(input("Please Enter The Numbers Of The Students Is = "))
for i in range(numbers_of_students) :
    print(f"\nDifferent Information Of The Student {i + 1} Is : \n")
    student_name = input(f"Please Enter The Name Of The Student {i + 1} Is : ") 
    student_marks = int(input(f"Please Enter The Total Marks Of The Student {i + 1} Is : "))
    student_information = {"student_name" : student_name , "student_marks" : student_marks}
    lista_of_student_name_with_marks . append(student_information)
displaying_lista_of_student_name_with_marks = get_lista_of_student_name_with_marks(lista_of_student_name_with_marks)
print(displaying_lista_of_student_name_with_marks)
