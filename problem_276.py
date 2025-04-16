# write a python program to get five student names in a list , and then check if the frist student name if the same of the last student name from the list of the student name by using function methods =>
# lista_of_student_names = []
# for i in range(5) :
#     student_names = input(f"Please Enter The Name Of The Student {i + 1} In The List Of The Student Names Is : ")
#     lista_of_student_names.append(student_names)
# def get_list_of_student_names(list_of_stud_name) :
#     print("The List Of The Student Name Is : "+str(list_of_stud_name))
#     for i in list_of_stud_name :
#         print(i)
#     print("Check If The Frist Student Name Is The Same Of The Last Student Name From The List Of The Student Names Is : ")
#     if(list_of_stud_name[0] == list_of_stud_name[-1]) :
#         print("The Frist Student Name Is The Same Of The Last Student Name From The List Of The Student Names")
#     else :
#         print("The Frist Student Name Is Not The Same Of The Last Student Name From The List Of The Student Name")
# get_list_of_student_names(lista_of_student_names)

def get_lista_of_student_name(list_of_stud_name) :
    print("The List Of The Student Names Is : "+str(list_of_stud_name))
    for i in list_of_stud_name :
        print(i)
    print("Check If The Frist Student Name Is The Same Of The Last Student Name From The List Of The Student Names Is : ")
    if(list_of_stud_name[0] == list_of_stud_name[-1]) :
        return("The Frist Student Name Is The Same Of The Last Student Name From The List Of The Student Names")
    else :
        return("The Frist Student Name Is Not The Same Of The Last Student Name From The List Of The Student Names")
lista_of_student_names = []
for i in range(5) :
    student_names = input("Please Enter All Student Names To Store In The List Of The Student Names Is : ")
    lista_of_student_names.append(student_names)
displaying_list_of_student_names = get_lista_of_student_name(lista_of_student_names)
print(displaying_list_of_student_names)