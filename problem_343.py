# write a python program to get list of student names , and then you should display all student names from the list of student names except student name that end with "n" , or "N" =>
lista_of_student_names = []
num_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of Terms Is = ",str(num_of_terms))
for i in range(num_of_terms) :
    student_names = input(f"Please Enter The Student Name {i + 1} Is : ")
    lista_of_student_names . append(student_names)
print("The List Of The Student Names Is : "+str(lista_of_student_names)) 
for j in lista_of_student_names :
    print(j)
print("The List Of All Student Names That Ends With \"n\" , Or \"N\" Is : ")
for k in lista_of_student_names :
    if((k.endswith("N")) or (k.endswith("n"))) :
        print(k)