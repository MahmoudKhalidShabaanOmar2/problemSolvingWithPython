# write a python program to get different information of the student like name , father name , cnic , age , and at the end contact number , and then display all information for the user , and then update the cnic , age , and at the end contact number by using function =>
student_name = input("please enter the name of the student is : ")
student_father_name = input("please enter the name of the father of the student is : ")
student_cnic = input("please enter the computerized national identify card number of the student is : ")
student_age = float(input("please enter the age of the student is = "))
student_contact_number = input("please enter the contact number of the student is : ")
def get_different_information_of_student(stud_name , stud_bab_name , stud_cnic , stud_age , stud_cont_num) :
    print("different information of the student before updating the value of the cnic , age , and at the contact number of the student is : \n")
    print("the name of the student is : \""+stud_name)
    print("the name of the father of the student is : \""+stud_bab_name+"\"")
    print("the computerized national identify card of the student is : \""+stud_cnic+"\"")
    print("the age of the student is : \""+str(stud_age)+" years\"")
    print("the contact number of the student is : \""+stud_cont_num+"\"")
    stud_cnic = input("please enter the updatting value computerized national identify card of the student is : ")
    stud_age = float(input("please enter the updatting value of the student age is = "))
    stud_cont_num = input("please enter the updatting value of the contact number of the student is : ")
    print("different information of the student after updating the value of the cnic , age , and at the end contact number of the student is : \n")
    print("the name of the student is : \""+stud_name+"\"")
    print("the name of the father of the student is : \""+stud_bab_name+"\"")
    print("the computerized national identify card of the student is : \""+stud_cnic+"\"")
    print("the age of the student is : \""+str(stud_age)+" years\"")
    print("the contact number of the student is : \""+stud_cont_num+"\"")
get_different_information_of_student(student_name , student_father_name , student_cnic , student_age , student_contact_number)