# write a python program to get list of the different student marks , and then displaying student marks , and student names is : 
lista_of_different_student_name_with_marks = []
numbers_of_student = int(input("Please Enter The Numbers Of The Student Is = "))
for i in range(numbers_of_student) :
    print(f"\nThe Different Information For The Student {i + 1} Is : ")
    student_name = input("Please Enter The Name Of The Student Is : ")
    student_marks = int(input("Please Enter The Total Marks Of The Student Is = "))
    student_information = {"student_name" : student_name , "student_marks" : student_marks}
    lista_of_different_student_name_with_marks . append(student_information)
print("\nThe Different Information Of Different Student Is : ")
for student in lista_of_different_student_name_with_marks : 
    print(f"The Name Of The Student Is : {student['student_name']} , And The Total Marks Of The Student Is = {student['student_marks']} Marks")