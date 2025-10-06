# write a python program to get list of student record , and user can be able to update the student record at the run time process =>
numbers_of_records = int(input("Please Enter The Student Record Is = "))
print("The Number Of Records Is = ",str(numbers_of_records)," Records")
lista_of_student_records = []
for i in range(numbers_of_records):
    student_record = input(f"Please Enter The Student Record ({i + 1}) Is : ")
    lista_of_student_records.append(student_record)
print("The Original List Of The Student Records Is = ",str(lista_of_student_records))
updated_student_record = input("Please Enter The Updated Student Record Is : ")
print("The Updated Student Record Is: ",updated_student_record)
index_number = int(input("Please Enter The Index Number Is = "))
print("The Index Number Is = ",str(index_number))
if( 0 <= index_number <= len(lista_of_student_records)):
    print("The Student Record Updated Successfully.")
    lista_of_student_records[index_number] = updated_student_record 
    print("The Updated List Of The Student Records Is : ",str(lista_of_student_records))
else:
    print("Please Enter A Valid Index Number.")