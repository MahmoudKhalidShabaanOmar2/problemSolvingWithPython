# write a python program to get ten name of the students from the user in a list , and display that students name in descending order by using different function methods =>
# lista_of_student_names = []
# # for i in range(10) :
#     # lista_of_student_names . append(input("please enter the name of the students to store in the list of the student name is : "))
# lista_of_student_names = [input("please enter the name of the student to store in the list of the student name is : ") for i in range(10)]
# def get_lista_of_student_names(list_of_name) :
#     print("the list of the student name in the ascending (properly) order is : \n")
#     for j in list_of_name : 
#         print("\""+j+"\"")
#     list_of_name . reverse()
#     print("the list of the student name in the descending (reversing) order is : \n")
#     for k in list_of_name :
#         print("\""+k+"\"")
# get_lista_of_student_names(lista_of_student_names)

def get_lista_of_student_names(list_of_name) :
    print("the list of the student name in the ascending (properly) order is : \n")
    for j in list_of_name :
        print("\""+j+"\"")
    print("the list of the student name in the descending (reversing) order is : \n")
    list_of_name . reverse()
    for k in list_of_name :
        print("\""+k+"\"")
    return("")
lista_of_student_names = []
# for i in range(10) :
    # lista_of_student_names . append(input("please enter the name of the student to store in the list of the student name is : "))
lista_of_student_names = [input("please enter the name of the students to store in the list of the student names is : ") for i in range(10)]
student_name = get_lista_of_student_names(lista_of_student_names)
print(student_name)
        
    
        