# write a python program to get different student information from the user by using function method =>
student_name = input("please enter the name of the student is : ")
student_father_name = input("please enter the name of the father of the student is : ")
student_cnic = input("please enter computerized national identify card of the student is : ")
student_age = float(input("please enter the age of the student is = "))
student_contact_number = input("please enter the contact number of the student is : ")
def get_different_information_of_student(stud_name , stud_bab_name , stud_cnic , stud_age , stud_phone_num) :
    print("the different information of the student is : \n")
    print("the name of the student is : \""+stud_name+"\"")
    print("the name of the father of the student is : \""+stud_bab_name+"\"")
    print("the computerized national identify card of the student is : \""+stud_cnic+"\"")
    print("the age of the student is = \""+str(stud_age)+" years\"")
    print("the phone number of the student is : \""+str(stud_phone_num)+"\"")
get_different_information_of_student(student_name , student_father_name , student_cnic , student_age , student_contact_number)