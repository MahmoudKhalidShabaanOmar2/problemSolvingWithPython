# write a python program to get ten student names in a list of student name , and then check if the frist character of the frist student name is equal to the frist character of the last student name from list of student name by using function methods =>
# lista_of_student_names = []
# for i in range(10) :
#     student_names = input(f"Please Enter All Student Name {i + 1} To Store In The List Of The Student Name Is : ")
#     lista_of_student_names.append(student_names)
# def get_lista_of_student_names(list_of_stud_name) :
#     print("The List Of The Student Name Is : ")
#     for j in list_of_stud_name :
#         print(j)
#     frist_char_frist_student_name = list_of_stud_name[0][0]  . lower()
#     print("The Frist Character From The Frist Student Name Is : "+frist_char_frist_student_name)
#     frist_char_last_student_name = list_of_stud_name[-1][0] . lower()
#     print("The Frist Character From The Last Student Name Is "+frist_char_last_student_name)
#     if(frist_char_frist_student_name == frist_char_last_student_name) :
#         print("The Frist Character From The Frist Student Name Is The Same Of The Frist Character Of The Last Student Name From The List Of The Student Name")
#     else :
#         print("The Frist Character From The Frist Student Name Is Not The Same Of The Frist Character From The Last Student Name From The List Of The Student Name")
# get_lista_of_student_names(lista_of_student_names)

def get_lista_of_student_names(list_of_stud_names) :
    print("The List Of The Student Names Is : ")
    for i in list_of_stud_names :
        print(i)
    frist_char_frist_student_name = list_of_stud_names[0][0] . lower()
    print("The Frist Character From The Frist Student Name Is : "+frist_char_frist_student_name)
    frist_char_last_student_name = list_of_stud_names[-1][0] . lower()
    print("The Frist Character From The Last Student Name Is : "+frist_char_last_student_name)
    if(frist_char_frist_student_name == frist_char_last_student_name) :
        return("The Frist Character From The Frist Student Name Is The Same Of The Frist Character From The Last Student Name")
    else :
        return("The Frist Character From The Frist Student Name Is Not The Same Of The Frist Character From The Last Student Name")
lista_of_student_names = []
for i in range(10) :
    student_names = input(f"Please Enter The Student Name {i + 1} To Store In The List Of The Student Name Is : ")
    lista_of_student_names.append(student_names)
displaying_list_of_student_names = get_lista_of_student_names(lista_of_student_names)
print(displaying_list_of_student_names)    