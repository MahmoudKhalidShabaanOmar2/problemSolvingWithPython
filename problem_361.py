# write a python program to get list of student names , and then display the list of the student names , and at the end displaying only student names that ends with "N" , Or "n" =>
lista_of_student_names = []
numbers_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of Terms Is = ",str(numbers_of_terms)," Terms")
for i in range(numbers_of_terms) :
    student_names = input(f"Please Enter The Name Of The Student {i + 1} Is : ")
    lista_of_student_names.append(student_names)
def get_lista_of_student_names(list_of_stud_names) :
    print("The List Of The Student Names Is : ",str(list_of_stud_names))
    for student_name in list_of_stud_names :
        print(student_name)
    print("The List Of The Student Names That Ends With \"N\" Or \"n\" Is : ")
    for student_name_ends_with_N_n in list_of_stud_names :
        if((student_name_ends_with_N_n.endswith("N")) or (student_name_ends_with_N_n.endswith("n"))) :
            print(student_name_ends_with_N_n)
get_lista_of_student_names(lista_of_student_names)