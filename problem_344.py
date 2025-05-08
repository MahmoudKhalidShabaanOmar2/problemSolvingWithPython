# write a python program to get list of student names then display the list of student names except the student name that starts with "F" , or "f" , and student name ends with "N" , and "n" =>
lista_of_student_names = []
num_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of The Terms Is = ",str(num_of_terms)," Terms")
for i in range(num_of_terms) :
    student_names = input(f"Please Enter The Student Name {i + 1} Is : ")
    lista_of_student_names.append(student_names)
print("The List Of The Student Name Is : "+str(lista_of_student_names))
for j in lista_of_student_names :
    print(j)
print("The List Of The Student Name Except The Student Names That Starts With \"f\" Or \"F\" , and ends with \"N\" , or \"n\" Is : ")
for k in lista_of_student_names :
    if((k.startswith("f") or k.startswith("F")) and (k.endswith("n") or k.endswith("N"))) :
        print(k)