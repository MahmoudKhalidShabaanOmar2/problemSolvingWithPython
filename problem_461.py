# write a python program to get the list of the student record , and then the user be able to update any student record in the running time peocessing by using function method =>
numbers_of_records = int(input("Please Enter The Number Of Records Is : "))
lista_of_student_records = []
def get_updated_student_records(nums_of_records , list_of_stud_records):
    print(f"The Number Of The Student Records Is = {nums_of_records} Student Records")
    for i in range(nums_of_records):
        student_record = input(f"Please Enter The Student Record ({i + 1}) Is : ")
        list_of_stud_records.append(student_record)
    print("The Original List Of The Student Records Is : ",str(list_of_stud_records))
    index_number = int(input("Please Enter The Index Number Is = "))
    print(f"The Index Number Is = {index_number}")
    updated_student_record = input("Please Enter The Updated Student Record Is : ")
    print("The Updated Student Record Is : ",updated_student_record)
    if(0 <= index_number <= len(list_of_stud_records)):
        print("Student Records Updated Successfully")
        list_of_stud_records[index_number] = updated_student_record 
        print("The Updated List Of The Student Records Is : ",str(list_of_stud_records))
    else:
        print("Please Enter A Valid Index Number.")
get_updated_student_records(numbers_of_records , lista_of_student_records)