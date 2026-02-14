# write a returned function to get a lista of student records , and then make the user able to remove a record on the running time process by using python language =>
def removed_student_record(list_of_stud_records):
    for different_record in range(10):
        student_record = input(f"Please Enter The Student Record {different_record + 1} Is : ")
        list_of_stud_records.append(student_record)
    print("The List Of The Student Records Before Removing Is : ",str(list_of_stud_records))
    for record in list_of_stud_records:
        print(record)
    removed_student_record = input("Please Enter The Removed Student Record Is : ")
    list_of_stud_records.remove(removed_student_record)
    print("The List Of The Student Record After REmoving Is : ",str(list_of_stud_records))
    for record in list_of_stud_records: 
        print(record)
        return("")
    
lista_of_student_record = []
removing_student_record = removed_student_record(lista_of_student_record)
print(removing_student_record)