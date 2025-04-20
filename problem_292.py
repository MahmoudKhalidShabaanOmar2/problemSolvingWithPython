# write a python program to get student names in the list of student names , and then display only student names that start with "n" , or "N" =>
lista_of_student_names = []
numbers_of_student_names = int(input("Please Enter The Number Of The Student Names Is = "))
for i in range(numbers_of_student_names) :
    student_names = input(f"Please Enter The Name Of The Student {i + 1} Is : ")
    lista_of_student_names.append(student_names)
print("The List Of All Student Names Is : ")
for j in lista_of_student_names :
    print(j)
print("The List Of All Student Names That Start With \"N\" , Or \"n\" Only Is : ")
for k in lista_of_student_names :
    if((k.startswith("n")) or (k.startswith("N"))) :
        print(k)