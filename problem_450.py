# write a python program to get lista of student records , and then the user be able to delete any student record in the run time process =>
numbers_of_records = int(input("Please Enter The Number Of Records Is = "))
print(f"The Number Of Records Is = ${numbers_of_records} Records")
lista_of_student_records = []
for i in range(numbers_of_records):
    student_record = input(f"Please Enter The Student Record (${i + 1}) Is : ")
    lista_of_student_records.append(student_record)
print("The Original List Of Student Records Is : ",str(lista_of_student_records))
removed_student_record = input("Please Enter The Removed Student Record Is : ")
print(f"The Removed Student Record Is : ${removed_student_record}")
lista_of_student_records.remove(removed_student_record)
print("The Updated List Of The Student Records Is : ",str(lista_of_student_records))