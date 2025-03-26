# write a python program to get ten student identifies numbers to check if there is a duplication , or not duplication in the list of the student identifyies by using different function methods=>
lista_of_student_identifies = []
# for i in range(10) :
#     stud_id = int(input("please enter the student identify is : "))
#     lista_of_student_identifies . append(stud_id)
lista_of_student_identifies = [int(input("please enter the student identifies to store in the list of the student identifies numbers is : ")) for i in range(10)]
def check_duplication(list_of_stud_id) :
    for j in list_of_stud_id : 
        if(list_of_stud_id . count(1) > 1) :
            return True 
    return False 
check_duplication_result = check_duplication(lista_of_student_identifies)
def check_duplication_in_list_of_student_identifies(list_of_stud_id) :
    print("the list of the student identifies numbers is : "+str(list_of_stud_id))
    for k in list_of_stud_id :
        print(k)
    if (check_duplication_result) :
        print("DUPLICATION")
    else :
        print("NO DUPLICATION")
check_duplication_in_list_of_student_identifies(lista_of_student_identifies)