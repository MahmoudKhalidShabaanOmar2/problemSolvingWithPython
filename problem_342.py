# write a python program to display all students names except that start with "F" , Or "f" =>
lista_of_student_names = []
num_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of Terms Is = ",str(num_of_terms)," Terms")
for i in range(num_of_terms) :
    student_names = input(f"Please Enter The Student Name {i + 1} Is : ")
    lista_of_student_names.append(student_names)
print("The List Of The Student Names Is : ",str(lista_of_student_names))
for j in lista_of_student_names :
    print(j)
print("The List Of All Names That Does Not Start With F , Or f Is : ")
for k in lista_of_student_names :
    if(not(k.startswith("F"))) :
        print(k)