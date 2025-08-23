# write a python program to store student records , and the user be to deleted and student name in the run time process by using function =>
lista_of_student_records = ["ahmed" , "mohamed" , "ali" , "tarek" , "moahmed" , "karim" , "khalid"]
def get_lista_of_student_records(list_of_stud_record) :
    print("The List Of The Student Records Is : ",str(list_of_stud_record))
    for record in list_of_stud_record:
        print(record)
    removed_student_record = input("Please Enter The Removed Student Record Is : ")
    print("The Removed Student Record Is : ",removed_student_record)
    list_of_stud_record.remove(removed_student_record)
    print("The List Of The Student Record After Removing Your Entered Student Record")
    for record in list_of_stud_record:
        print(record)
get_lista_of_student_records(lista_of_student_records)