# write a python program to get five student names in a tuple of student names , and then check if the frist character of the frist student name is the same of the frist character of the last student name => 
lista_of_student_names = []
for i in range(5) :
    student_names = input(f"Please Enter The Different Student Names {i + 1} To Store In The List Is : ")
    lista_of_student_names . append(student_names)
print("\nThe List Of The Student Names Is : ")
print(lista_of_student_names)
tuples_of_student_names = tuple(lista_of_student_names)
print("\nThe Tuple Of The Student Names Is : ")
print("The Tuple Of The Student Names Is : "+str(tuples_of_student_names))
frist_char_frist_student_name = tuples_of_student_names[0][0] . lower()
print("The Frist Character Of The Frist Student Name Is : "+frist_char_frist_student_name)
frist_char_last_student_name = tuples_of_student_names[-1][0] . lower()
print("The Frist Character Of The Last Student Name Is : "+frist_char_last_student_name)
print("\nCheck If The Frist Character Of The Frist Student Name Is The Same Of The Frist Character Of The Last Student Name")
if(frist_char_frist_student_name == frist_char_last_student_name) :
    print("The Frist Character Of The Frist Student Name Is The Same Of The Frist Character Of The Last Student Name")
else :
    print("The Frist Character Of The Frist Student Name Is Not The Same Of The Frist Character Of The Last Student Name")