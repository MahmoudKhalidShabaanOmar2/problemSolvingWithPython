# write a python program to get five students name in a list , and then check if the frist character of the frist student name if the same of the frist character of the last student name =>
lista_of_student_names = []
for i in range(5) :
    student_names = input(f"Please Enter The Names Of The Students To Store In The List Of The Student Names {i + 1} Is : ")
    lista_of_student_names.append(student_names)
print("\nThe List Of The Student Names Is : ")
print(lista_of_student_names)
frist_char_frist_student_name = lista_of_student_names[0][0].lower()
print("The Frist Character Of The Frist Student Name Is : "+frist_char_frist_student_name)
frist_char_last_student_name = lista_of_student_names[-1][0].lower()
print("The Frist Character Of The Last Student Name Is : "+frist_char_last_student_name)
if(frist_char_frist_student_name == frist_char_last_student_name) :
    print("The Frist Character Of The Frist Student Name Is The Same Of The Frist Character Of The Last Student Name")
else :
    print("The Frist Character Of The Frist Student Name Is Not The Same Of The Frist Character Of The Last Student Name")