# write a python program to get student names in a list of student names , and then get the name that ends with "y" from the list of student names =>
lista_of_student_names = []
numbers_of_student_names = int(input("Please Enter The Names Of The Student Is = "))
for i in range(numbers_of_student_names) :
    student_names = input(f"Please Enter The Name Of The Student {i + 1} Is : ")
    lista_of_student_names.append(student_names)
print("The List Of All Student Names Is : "+str(lista_of_student_names))
for j in lista_of_student_names :
    print(j)
print("The List Of The Student Names That End With \"Y\" , Or \"y\" Only Is : ")
for k in lista_of_student_names :
    if((k.endswith("Y")) or (k.endswith("y"))) :
        print(k)