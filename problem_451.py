# write a python program to get the list of the student records , and the user be able to update any student record on the run time processing =>
numbers_of_records = int(input("Please Enter The Number Of Records Is = "))
print("The Number Of Records Is = "+str(numbers_of_records)," Records")
lista_of_student_records = []
for i in range(numbers_of_records):
    student_record = input(f"Please Enter The Student Record ({i + 1}) Is : ")
    lista_of_student_records.append(student_record)
print("The Original List Of The Student Record Is : ",str(lista_of_student_records))
updated_student_record = input("Please Enter The Student Record Is : ")
print("The Updated Student Record Is : ",updated_student_record)
index_number = int(input("Please Enter The Index Number Is = "))
print("The Index Number Is = ",str(index_number))
if(0 <= index_number <= len(lista_of_student_records)):
    print("The Lista Of The Student Records Updated Successfully")
    lista_of_student_records[index_number] = updated_student_record 
    print("The Updated Student Record Is : ",str(lista_of_student_records))
else:
    print("Please Enter Valid Index Number")