# write a python program to get list of students names from the user , and then displaying only student names that starts with "f" , or "F" by using function method => 
lista_of_student_names = []
number_of_terms = int(input("Please Enter The Number Of Student Names Is = "))
print("The Number Of The Student Names Is = ",str(number_of_terms)," Student Names")
for i in range(number_of_terms) :
    student_names = input(f"Please Enter The Student Name {i + 1} Is : ")
    lista_of_student_names.append(student_names)
def get_lista_of_student_names(list_of_stud_names) :
    print("The List Of The Student Names Is : ",str(list_of_stud_names))
    for student_name in list_of_stud_names :
        print(student_name)
        lista_of_student_names_start_with_f_F = []
        if((student_name.startswith("F")) or (student_name.startswith("f"))) :
            lista_of_student_names_start_with_f_F.append(student_name)
        print("The List Of The Student Name That Start With \"f\" , Or \"F\" Is : ",str(lista_of_student_names_start_with_f_F))
get_lista_of_student_names(lista_of_student_names)    