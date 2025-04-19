# write a python program to get student names in the list of the student names , and then get the student name that start with letter "F" =>
lista_of_student_names = []
numbers_of_student_names = int(input("Please Enter The Numbers Of The Student Is = "))
print("The Number Of The Students Is = ",str(numbers_of_student_names)+" Student Names")
for i in range(numbers_of_student_names) :
    student_names = input(f"Please Enter The Name Of The Student {i + 1} Is : ")
    lista_of_student_names . append(student_names)
print("The Name Of The Students Is : "+str(lista_of_student_names))
for j in lista_of_student_names :
    if(j.startswith("f") or j.startswith("F")) :
        print(j)