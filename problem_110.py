# write a python program to get ten name of the students from the user in a list , and display that students name in descending order with removing the frist and last student name by using different function meethods =>
# lista_of_student_names = []
# # for i in range(10) :
# #     lista_of_student_names . append(input("please enter the name of the student name to store in the list of the student names is : "))
lista_of_student_names = [input("please enter the student names to store in the list of the student names is : ") for i in range(10)]
def get_lista_of_student_names(list_of_stud_names) : 
    print("the list of the student name before removing the frist , and last student names in the ascending(properly) order is : \n")
    for j in list_of_stud_names :
        print("\""+j+"\"")
    print("the list of the student names before removing the frist , and last student names in the reversing(descending) order is : \n")
    list_of_stud_names . reverse()
    for k in list_of_stud_names :
        print("\""+k+"\"")
    print("the list of the student names after removing the frist , and last student names in the ascending(properly) order is : \n") 
    list_of_stud_names . reverse()
    # list_of_stud_names . pop(0)
    list_of_stud_names . remove(list_of_stud_names[0])
    # list_of_stud_names . pop()
    list_of_stud_names . remove(list_of_stud_names[8])
    for n in list_of_stud_names :
        print("\""+n+"\"")
    print("the list of the student names after removing the frist , and last student names in the descending(reversing) order is : \n")
    list_of_stud_names . reverse()
    for m in list_of_stud_names :
        print("\""+m+"\"")
get_lista_of_student_names(lista_of_student_names)    