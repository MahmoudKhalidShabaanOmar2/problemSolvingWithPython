# write a python program to get ten student identify in the list , and then check if student iddentify duplication , or not duplicated =>
lista_of_student_identifies = []
for i in range(10) :
    stud_id = int(input("please enter the student identify to store in the list of the student identify is : "))
    lista_of_student_identifies . append(stud_id)
def check_student_identify(list_of_stud_ids) :
    print("the list of the student identifies is : "+str(list_of_stud_ids))
    for j in list_of_stud_ids :
        if(list_of_stud_ids . count(j) > 1) :
            return True 
    return False
result_of_checking_duplication = check_student_identify(lista_of_student_identifies) 
if(result_of_checking_duplication) :
    print("There Is \"Duplication\" in the list of the stduent identifies")
else :
    print("there is \"No Duplication\" in the list of the student identifies")