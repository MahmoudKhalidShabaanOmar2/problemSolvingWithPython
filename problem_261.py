# write a python program to store five student names in a list , and check if the frist student name is the same of the last student name from the list of student names =>
lista_of_student_names = []
for i in range(5) :
    student_names = input(f"Please Enter The Name Of The Student {i + 1} Is : ")
    lista_of_student_names.append(student_names)
print("\nThe List Of The Student Names Is : ")
print(lista_of_student_names)
print("\nCheck If The Frist Student Name Is The Same Of The Last Student Name")
if(lista_of_student_names[0] == lista_of_student_names[-1]) :
    print("The Frist Student Name Is The Same Of The Last Student Name , Because The Frist Name Is : "+str(lista_of_student_names[0]) , " And The Last Name Of The Student Is : "+str(lista_of_student_names[-1]))
else :
    print("The Frist Student Name Is Not The Same Of The Last Student Name , Because The Frist Name Is : "+str(lista_of_student_names[0]), " , And The Last Name Of The Student Is : "+str(lista_of_student_names[-1]))