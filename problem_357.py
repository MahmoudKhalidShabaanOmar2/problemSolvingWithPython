# write a python program to get list of student names and then display only student names that ends with "F" , or "f" by using function method =>
lista_of_student_names = []
number_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of The Terms Is = ",str(number_of_terms)," Terms")
for i in range(number_of_terms) :
    student_names = input(f"Please Enter The Student Name {i + 1} Is : ")
    lista_of_student_names.append(student_names)
def get_lista_of_student_names(list_of_stud_names) :
    print("The List Of The Student Names Is : ",str(list_of_stud_names))
    for student_name in list_of_stud_names :
        print(student_name)
    print("The List Of The Student Names That Ends With \"F\" , Or \"f\" Is : ")
    for i in lista_of_student_names :
        if((i.endswith("F")) or (i.endswith("f"))) :
            print(i)
get_lista_of_student_names(lista_of_student_names)