# write a python program to get the list of the student rcords that the user be able to delete any student record in the running time processing by using function method =>
numbers_of_records = int(input("Please Enter The Number Of Records Is = "))
lista_of_student_record = []
def get_lista_of_student_records(nums_of_records , list_of_stud_records):
    print(f"The Number Of Student Records Is = {str(nums_of_records)} Records")
    for i in range(nums_of_records):
        student_record = input(f"Please Enter The Student Record ({i + 1}) Is : ")
        list_of_stud_records.append(student_record)
    print("The Original List Of The Student Records Is : ",str(list_of_stud_records))
    removed_student_record = input("Please Enter The Student Record That You Want To Delete From The Original List Of The Student Records Is : ")
    print("The Student Record That You Want To Remove From The Original Student Record Is : ",student_record)
    list_of_stud_records.remove(removed_student_record)
    print("The Updated List Of The Student Records Is : ",str(list_of_stud_records))
get_lista_of_student_records(numbers_of_records , lista_of_student_record)