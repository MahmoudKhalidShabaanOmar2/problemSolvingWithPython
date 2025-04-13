# write a python program to get name with marks of the student in a list , and then display the second list of the student , and then display student name , and student marks =>
lista_of_different_student_name_with_marks = []
numbers_of_students = int(input("Please Enter The Numbers Of Students Is = "))
for i in range(numbers_of_students) :
    print(f"\nDifferent Iformation For The Student {i + 1} Is : ")
    student_name = input("Please Enter The Name Of The Student Is : ")
    student_marks = int(input("Please Enter The Total Marks Of The Student Is : "))
    student_information = {"student_name" : student_name , "student_marks" : student_marks}
    lista_of_different_student_name_with_marks . append(student_information)
print("The Second Position Of The Student Information From The List Of The Different Student Information Is : ")
if(len(lista_of_different_student_name_with_marks) >= 2) :
    second_student_information_position = lista_of_different_student_name_with_marks[1]
    print(f"The Name Of The Second Student Is : {second_student_information_position['student_name']} , And The Total Marks Of The Second Student Is :{second_student_information_position['student_marks']} Marks")
else :
    print("")
print("\nThe List Of The Different Information Of The Student Is : ")
for student in lista_of_different_student_name_with_marks : 
    print(f"The Name Of The Student Is : {student['student_name']} , And The Total Marks Of The Is : {student['student_marks']} Marks")