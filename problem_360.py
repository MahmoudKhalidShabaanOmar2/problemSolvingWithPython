# write a python program to get list of student names , and then displaying the student names that ends with Y , Or y by using function methods =>
lista_of_student_names = []
number_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Numbers Of Terms Is = ",str(number_of_terms)," Terms")
for i in range(number_of_terms) :
    student_names = input(f"Please Enter The Student Name {i + 1} Is : ")
    lista_of_student_names.append(student_names)
def get_lista_of_student_names(list_of_stud_names) :
    print("The List Of The Student Names Is : ")
    for student_names in list_of_stud_names :
        print(student_names)
    print("The List Of The Student Names That Ends With \"Y\" , Or \"y\" Is : ")
    for student_names_ends_with_Y_y in list_of_stud_names :
        if((student_names_ends_with_Y_y.endswith("Y")) or (student_names_ends_with_Y_y.endswith("y"))) :
            print(student_names_ends_with_Y_y)
get_lista_of_student_names(lista_of_student_names)