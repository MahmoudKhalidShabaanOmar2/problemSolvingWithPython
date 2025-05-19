# write a python program to get list of different student names , and then display only student names that start with "A" , Or "a" by using function method =>
lista_of_student_names = []
number_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of Terms Is = ",str(number_of_terms)," Terms")
for i in range(number_of_terms) :
    student_names = input(f"Please Enter The Student Name {i + 1} Is : ")
    lista_of_student_names.append(student_names)
def get_list_of_student_names(list_of_stud_names) :
    print("The List Of The Student Names Is : ")
    for name in list_of_stud_names :
        print(name)
    print("The List Of The Student Names That Start With \"A\" Is : ")
    for stud_name_start_with_A in list_of_stud_names :
        if(stud_name_start_with_A.startswith("A") ) :
            print(stud_name_start_with_A)
get_list_of_student_names(lista_of_student_names)