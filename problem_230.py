# write a python program python to get six identify student number in list , and then reversing all identify numbers of the student by using different function method =>
# # lista_of_student_identify_numbers = []
# # for i in range(6) :
# #     identify_numbers = int(input("please enter the identify numbers of the stidents is : "))
# #     lista_of_student_identify_numbers . append(identify_numbers)
# lista_of_student_identify_numbers = [int(input("please enter the student identify numbers of the student is : ")) for i in range(6)]
# def get_lista_of_student_identify_numbers(list_of_stud_id_num) : 
#     print("the list of the student identify numbers is : "+str(list_of_stud_id_num))
#     for i in list_of_stud_id_num : 
#         print(i)
#     list_of_stud_id_num . reverse()
#     print("the reversing (descending) order of the list of the different student identify numbers is : "+str(list_of_stud_id_num))
#     for j in list_of_stud_id_num :
#         print(j)
# get_lista_of_student_identify_numbers(lista_of_student_identify_numbers)

# def get_lista_of_student_identify_numbers(list_of_stud_id_num) :
#     print("the list of the student identify numbers of the student is : "+str(list_of_stud_id_num))
#     for j in list_of_stud_id_num : 
#         print(j)
#     list_of_stud_id_num . reverse()
#     print("the reversing (descending) order of the list of the student identify numbers is : "+str(list_of_stud_id_num))
#     for k in list_of_stud_id_num : 
#         print(k)
#     return("")
# # lista_of_student_identify_numbers = []
# # for i in range(6) :
# #     identify_numbers = int(input("please enter the different identify numbers of the student is : "))
# #     lista_of_student_identify_numbers . append(identify_numbers)
# lista_of_student_identify_numbers = [int(input("please enter the student identify numbers of the student is : ")) for i in range(6)]
# id_num = get_lista_of_student_identify_numbers(lista_of_student_identify_numbers)
# print(id_num)
    
def get_lista_of_student_identify_numbers(list_of_stud_id_num) :
    print("the list of the student identify numbers is : "+str(list_of_stud_id_num))
    for j in list_of_stud_id_num :
        print(j)
    list_of_stud_id_num . sort(reverse = True) 
    print("the reversing (descending) order of the list of the different student identify numbers is : "+str(list_of_stud_id_num))
    for k in list_of_stud_id_num :
        print(k)
    return("")
# lista_of_student_identify_numbers = []
# for i in range(6) :
#     identify_numbers = int(input("please enter the different identify numbers of the student is : "))
#     lista_of_student_identify_numbers . append(identify_numbers)
lista_of_student_identify_numbers = [int(input("please enter the different identify numbers of the stident is : ")) for i in range(6)]
id_num = get_lista_of_student_identify_numbers(lista_of_student_identify_numbers)
print(id_num)